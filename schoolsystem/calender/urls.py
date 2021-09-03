from django.conf.urls import url
from . import views
from django.urls import path
from.views import Calendar, CalendarView


app_name = 'calender'
urlpatterns = [
     path("register/",views.CalendarView.as_view(),name="calender_register"),
     path('calender/',views.register_calender , name='register_calender')
]



