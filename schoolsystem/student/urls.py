from django.urls import path
from .views import register_student,student_profile,student_list,delete_student,edit_student

app_name="student"
urlpatterns = [
    path("register/",register_student,name="register_student"),
    path("list/", student_list, name="student_list"),
    path("edit/<int:id>/", edit_student,name="edit"),
    path("profile/<int:id>/",student_profile,name='profile'),
    path("delete/<int:id>/", delete_student, name="deletestudent"),

]