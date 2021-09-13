from django.db import models
from django.db.models import fields
from rest_framework import serializers
from student.models import Student

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model=Student
        fields=("first_name","last_name","age")
