from django.urls import path
from .views import addStudent, updateStudent, Students

urlpatterns = [
    path('addstudent/', addStudent),
    path('updatestudent/', updateStudent),
    path('student/', Students.as_view()),
]
