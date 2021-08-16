from django.conf import urls
from django.conf.urls import url
from django.urls import path
from.views import register_course
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path("register/",register_course,name="register_course")
]





