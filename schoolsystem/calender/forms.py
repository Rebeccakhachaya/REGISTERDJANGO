from django import forms
from django.db import models
from django.forms import ModelForm
from.models import Event
class CalenderForm(forms.ModelForm):
    class Meta:
        model=Event
        fields="__all__"




def __init__(self,*args,**kwargs):
    super(CalenderForm,self).__init__(*args,**kwargs)
    self.fields['start_time'].input_formats=('%Y-%m-%dT%H:%M',)
    self.fields['end_time'].input_formats=('%Y-%m-%dT%H:%M',)
