from django.contrib import admin
from .models import Student, Session, Department, Course, Enrollement
from django.contrib.auth import get_user_model
Users = get_user_model()
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


@admin.register(Users)
class StudentAdmin(UserAdmin):

    fieldsets = (
        (None, {'fields': ('email',)}),
        (_('Personal info'), {'fields': ('username', 'roll_number','first_name', 'last_name',
                                          'department', 'is_staff', 'is_active', 'groups')}),
    )
   
    add_fieldsets = (
        (None, {'fields': ('email',)}),
        (_('Personal info'), {'fields': ('first_name', 'last_name',
                                         'username', 'roll_number', 'department', 'is_staff', 'is_active', 'groups', 'password1', 'password2')}),
    )

    list_display = ('username','first_name', 'last_name', 'email', 'roll_number', 'department')

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('tag',)



@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'units', 'department')

@admin.register(Enrollement)
class EnrollementAdmin(admin.ModelAdmin):
    list_display = ('student','session', 'semester', 'course', 'attendance_score', 'test_score', 'exam_score', 'total_score', 'grade', 'grade_unit', 'grade_point')
    

