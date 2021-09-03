from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH, CharField

class Course(models.Model):
    course_name=models.CharField(max_length=20)
    course_code=models.CharField(max_length=6)
    trainer_id=models.CharField(max_length=6)
    description=models.CharField(max_length=30)
    syllabus=models.CharField(max_length=12)
    course_channel=models.CharField(max_length=15)
    course_email=models.EmailField()


# Create your models here.
