from django.shortcuts import redirect, render
from .forms import StudentRegestrationForm
from .models import Student
from django.shortcuts import render
# Create your views here.
def register_student(request):
    form = StudentRegestrationForm()
    return render(request,"register_student.html",{"form":form})
def register_student(request):
    if request.method=="POST":
        form=StudentRegestrationForm(request.Post, request.FILES['document'])
        if form.is_valid():
           form.save()
        else:
            print(form.errors)
    else:
        form=StudentRegestrationForm()
    return render(request, "register_student.html", {"form":form})

def list_student(request):
    students=Student.objects.all()
    return render(request, "list_student.html",{
         "students":students
    })

def student_profile(request,id):
    student=Student.objects.get(id=id)
    return render(request,"student_profile.html",{'student':student})
def edit_student(request,id) :
    student=Student.objects.get(id=id)
    if request.method == "POST":
        form=StudentRegestrationForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("student_profile", id=student.id, )
    else:
            form=StudentRegestrationForm(instance=student)
            return render(request, "edit_student.html", {"form" : form})






