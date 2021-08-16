from django.db import models

class Trainer(models.Model):
    first_name=models.CharField(max_length=12)
    last_name=models.CharField(max_length=20)
    gender_choice=((u'F',u'female'),(u'm',u'male'),(u'o','other'))
    gender=models.CharField(max_length=12,choices=gender_choice)
    company_name=models.CharField(max_length=12)
    course_name=models.CharField(max_length=15)
    email=models.CharField(max_length=12)
    resume=models.FileField()
    city=models.CharField(max_length=10)
    image_of_the_trainer=models.ImageField(upload_to="register_trainer")
    joining_date=models.DateField(max_length=8)
    salary=models.BigIntegerField()



# Create your models here.

