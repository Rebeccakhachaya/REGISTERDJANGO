# Generated by Django 3.2.4 on 2021-09-27 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_auto_20210921_0712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='date_of_birth',
        ),
    ]