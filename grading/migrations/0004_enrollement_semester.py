# Generated by Django 2.1.4 on 2020-03-11 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grading', '0003_auto_20200310_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollement',
            name='semester',
            field=models.CharField(blank=True, choices=[('First Semester', 'First Semester'), ('Second Semester', 'Second Semester')], max_length=255, null=True),
        ),
    ]
