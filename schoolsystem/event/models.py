from django.db import models

# Create your models here.
class Event(models.Model):
    event_name=models.CharField(max_length=12 ,null=True, blank=True)
    venue=models.CharField(max_length=12,)
    agenda=models.CharField(max_length=12)
    date_of_the_event=models.DateTimeField()
    duration=models.DurationField()
    description=models.CharField(max_length=12)
    event_link=models.CharField(max_length=12)