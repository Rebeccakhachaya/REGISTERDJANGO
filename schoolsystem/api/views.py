from django.shortcuts import render
from rest_framework import viewsets
from student.models import Student
from.serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    Serializer_class=StudentSerializer

# Create your views here.
