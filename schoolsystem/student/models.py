from django.db import models

from django.db.models.fields import BLANK_CHOICE_DASH, CharField
class Student(models.Model):
    first_name=models.CharField(max_length=12)
    last_name=models.CharField(max_length=20)
    age=models.PositiveSmallIntegerField()
    date_of_birth=models.DateField(default=True)
    nationality_choice=((u'k',u'KENYA'),(u'g',u'UGANDA'),(u'r','RWANDA'))
    nationality=models.CharField(max_length=12,choices=nationality_choice)
    Student_id=models.CharField(max_length=12,blank=True)
    passport=models.CharField(max_length=10)
    email=models.EmailField(default=0)
    gender_choice=((u'F',u'female'),(u'm',u'male'),(u'o','other'))
    gender=models.CharField(max_length=12,choices=gender_choice)
    subject=models.CharField(max_length=14)
    health_records=models.FileField(upload_to='documents/%Y/%m/%d')
    classroom=models.CharField(max_length=10,default=False)
    phone_number=models.CharField(max_length=12)
    admission_date=models.DateField(default=True)
    parent_contact=CharField(max_length=12)
    academic_year=models.DateField(max_length=8,default=False)
    language_choices=((u'E',u'English'),(u'K','Kiswahili'),(u'F','French'))
    Language=models.CharField(max_length=15,choices=language_choices,blank=True)
    profile_pic=models.ImageField(upload_to="images/")
    # Create your models here.
