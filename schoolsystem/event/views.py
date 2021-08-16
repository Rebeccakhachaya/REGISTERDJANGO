from django.shortcuts import render

# Create your views here.
from django import forms
from django.shortcuts import render
from.forms import EventRegistrationForm



def register_event(request):
    if request.method=="POST":
        form=EventRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=EventRegistrationForm
    return render(request,"register_event.html",{"form":form})                

