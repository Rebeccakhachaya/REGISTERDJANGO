# Generated by Django 3.2.4 on 2021-09-21 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_alter_student_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='Student_id',
        ),
        migrations.RemoveField(
            model_name='student',
            name='classroom',
        ),
        migrations.RemoveField(
            model_name='student',
            name='language',
        ),
        migrations.RemoveField(
            model_name='student',
            name='profile_pic',
        ),
        migrations.AddField(
            model_name='student',
            name='class_room',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='gurdian_contact',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='gurdian_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='student',
            name='languages',
            field=models.CharField(blank=True, choices=[('E', 'English'), ('K', 'Kiswahili'), ('F', 'French')], max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='parent_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='admission_date',
            field=models.DateField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('m', 'Male'), ('O', 'Other')], max_length=16),
        ),
        migrations.AlterField(
            model_name='student',
            name='health_records',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='student',
            name='nationality',
            field=models.CharField(choices=[('k', 'Kenyan'), ('u', 'Ugandan'), ('R', 'Rwandan'), ('S', 'Sudanese'), ('S', 'SouthSudanese')], max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='passport',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone_number',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='subject',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]