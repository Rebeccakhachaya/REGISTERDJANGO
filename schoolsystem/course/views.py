from django import forms
from django.shortcuts import render
from .forms import CourseRegistrationForm
from.models import Course




def register_course(request):
    if request.method=="POST":
        form=CourseRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=CourseRegistrationForm()
    return render(request,"register_course.html",{"form":form}) 
def course_list(request):
     courses=Course.objects.all()
     return render(request,"course_list.html",{"courses":courses})    
      



# Create your views here.
