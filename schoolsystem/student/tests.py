from datetime import datetime
from django.http import request
from django.test import TestCase
from .models import Student
import datetime
from django.urls import reverse

# Create your tests here.
class StudentModelTestCase(TestCase):
    def setUp(self):
        self.student=Student(first_name="mary",last_name="Atieno",age=20,health_records="file",
        gender="famale",languages="English")


    def test_full_name_contains_first_name(self):
        self.assertIn(self.student.first_name,self.student.full_name())  

    def test_full_name_contains_last_name(self):
        self.assertIn(self.student.last_name,self.student.full_name())       

    def test_year_of_birth(self):
        current_year=datetime.datetime.now().year
        year=2021-self.student.age
        self.assertEqual(year,self.student.year_of_birth())   
        

    def test_student_registration_view(self):
        url=reverse("register_student")
        data={"first_name":self.student.first_name,"last_name":self.student.last_name,
        "age":self.student.age,"health_records":self.student.health_records,"gender":self.student.gender,
        "languages":self.student.languages}
        request=Self.client.post(url,data)
        self.assertEqual(request.status_code,200)
