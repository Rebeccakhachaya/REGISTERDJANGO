from django.urls import path
from .views import edit_student, register_student, student_profile
from .views import register_student,list_student
from .views import student_profile

urlpatterns=[
             path('register/', register_student, name="register_student"),
             path('list/',list_student, name="list_student"),
             path('profile/<int:id>/', student_profile, name="student_profile"),
             path('edit/<int:id>/', edit_student, name="edit_student"),
]


