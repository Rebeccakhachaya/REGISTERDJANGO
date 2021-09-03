from django.conf import urls
from django.urls import path
from.views import register_trainer, trainer_list
from django.conf import settings
from.views import trainer_list

urlpatterns=[
    path("register/",register_trainer,name="register_trainer"),
    path("register_list/",trainer_list,name="trainer_list"),

]
