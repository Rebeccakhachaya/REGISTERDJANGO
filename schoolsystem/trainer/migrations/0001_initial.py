# Generated by Django 3.2.4 on 2021-08-15 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=12)),
                ('last_name', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('F', 'female'), ('m', 'male'), ('o', 'other')], max_length=12)),
                ('company_name', models.CharField(max_length=12)),
                ('course_name', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=12)),
                ('resume', models.FileField(upload_to='')),
                ('city', models.CharField(max_length=10)),
                ('image_of_the_trainer', models.ImageField(upload_to='register_trainer')),
                ('joining_date', models.DateField(max_length=8)),
                ('salary', models.BigIntegerField()),
            ],
        ),
    ]