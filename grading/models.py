from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManager(UserManager):
    def get_by_natural_key(self, username):
        case_insensitive_username_field = '{}__iexact'.format(
            self.model.USERNAME_FIELD)
        return self.get(**{case_insensitive_username_field: username})

class Department(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Student(AbstractUser):
    roll_number = models.CharField(max_length=255, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    
    objects = CustomUserManager()


class Session(models.Model):
    tag = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.tag

class Course(models.Model):
    code = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    units = models.IntegerField(default=0)
    department = models.ForeignKey(Department,blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Enrollement(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)
    session = models.ForeignKey(Session, blank=True, null=True, on_delete=models.CASCADE)
    semester = models.CharField(max_length=255, choices= (
        ('First Semester', 'First Semester'),
        ('Second Semester', 'Second Semester')
    ), blank=True, null=True)
    course = models.ForeignKey(Course, related_name='courses', on_delete=models.CASCADE, blank=True, null=True)
    attendance_score = models.IntegerField(default=0)
    test_score = models.IntegerField(default=0)
    exam_score = models.IntegerField(default=0)

    def total_score(self):
        return self.attendance_score + self.test_score + self.exam_score

    def grade(self):
        if self.total_score() <= 40:
            return 'E'
        if self.total_score() <= 49:
            return 'D'
        elif self.total_score() <= 59:
            return 'C' 
        elif self.total_score() <= 69:
            return 'B'
        elif self.total_score() >= 70:
            return 'A'
        else:
            return 'F'
    
    def grade_unit(self):
        if self.grade() == 'A':
            return 5
        elif self.grade() == 'B':
            return 4
        elif self.grade() == 'C':
            return 3
        elif self.grade() == 'D':
            return 2
        elif self.grade() == 'E':
            return 1
        else:
            return 0
        
    def grade_point(self):
        return self.course.units * self.grade_unit()

    def __str__(self):
        return str(self.course)




