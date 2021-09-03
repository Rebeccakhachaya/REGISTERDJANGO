from django.db import models

from django.db.models.fields import BLANK_CHOICE_DASH, CharField
class Student(models.Model):
    first_name=models.CharField(max_length=12)
    last_name=models.CharField(max_length=20)
    age=models.PositiveSmallIntegerField()
    date_of_birth=models.DateField(blank=True,null=True)
    nationality_choice=((u'kenya',u'KENYA'),(u'uganda',u'UGANDA'),(u'Rwanda','RWANDA'))
    nationality=models.CharField(max_length=12,choices=nationality_choice)
    Student_id=models.CharField(max_length=12,blank=True)
    passport=models.CharField(max_length=10)
    email=models.EmailField(default=0)
    gender_choice=((u'F',u'female'),(u'm',u'male'),(u'o','other'))
    gender=models.CharField(max_length=12,choices=gender_choice)
    subject=models.CharField(max_length=14,blank=True,null=True)
    health_records=models.FileField(upload_to='documents/%Y/%m/%d')
    classroom=models.CharField(max_length=10,blank=True,null=True)
    phone_number=models.CharField(max_length=12)
    admission_date=models.DateField(blank=True,null=True)
    parent_contact=CharField(max_length=12,blank=True,null=True)
    academic_year=models.DateField(max_length=8,blank=True,null=True)
    language_choices=((u'English',u'English'),(u'Kiswahili','Kiswahili'),(u'French','French'))
    language=models.CharField(max_length=15,choices=language_choices,blank=True)
    profile_pic=models.ImageField(upload_to="images/")
    # Create your models here.
