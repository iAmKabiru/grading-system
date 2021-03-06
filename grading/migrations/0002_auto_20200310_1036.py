# Generated by Django 2.1.4 on 2020-03-10 10:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grading', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollement',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='grading.Course'),
        ),
        migrations.AlterField(
            model_name='enrollement',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='grading.Department'),
        ),
    ]
