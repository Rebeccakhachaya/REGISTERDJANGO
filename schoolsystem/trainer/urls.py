from django.conf import urls
from django.urls import path
from.views import edit_trainer, register_trainer, trainer_list, trainer_profile
from django.conf import settings
from.views import trainer_list,register_trainer,edit_trainer,trainer_profile


urlpatterns=[
    path("register/",register_trainer,name="register_trainer"),
    path("register_list/",trainer_list,name="trainer_list"),
    path("edit/<int:id>/",edit_trainer,name="edit_trainer"),
    path("profile/<int:id>/",trainer_profile,name="trainer_profile"),
    

]


