from django.core.exceptions import ImproperlyConfigured
from django.http import request
from django.shortcuts import render
from django import forms
from .forms import StudentRegestrationForm

# Create your views here.
def register_student(request):
     form=StudentRegestrationForm()
     return render(request,"register_student.html",{"form":form})
     
