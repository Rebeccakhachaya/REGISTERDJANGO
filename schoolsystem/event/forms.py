from django import forms
from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from.models import Event


class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model=Event
        fields="__all__"

