# Generated by Django 4.1.3 on 2022-11-10 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0002_rename_subjects_subject'),
        ('lessons', '0002_rename_start_time_lessons_start_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lessons',
            new_name='Lesson',
        ),
    ]
