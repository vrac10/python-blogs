# Generated by Django 3.2.11 on 2022-01-21 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gsoc', '0003_remove_suborgdetails_past_years'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suborgdetails',
            name='applied_but_not_selected',
        ),
        migrations.RemoveField(
            model_name='suborgdetails',
            name='mentors_student_engagement',
        ),
        migrations.RemoveField(
            model_name='suborgdetails',
            name='reason_for_participation',
        ),
        migrations.RemoveField(
            model_name='suborgdetails',
            name='students_involvement_after',
        ),
        migrations.RemoveField(
            model_name='suborgdetails',
            name='students_involvement_gsoc',
        ),
        migrations.RemoveField(
            model_name='suborgdetails',
            name='students_on_schedule',
        ),
        migrations.RemoveField(
            model_name='suborgdetails',
            name='year_of_start',
        ),
    ]