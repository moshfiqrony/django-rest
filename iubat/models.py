from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class StudentProfile(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    firstname = models.CharField(max_length=50, blank=True, null=True)
    lastname = models.CharField(max_length=50, blank=True, null=True)
    personal_email = models.EmailField(max_length=100, blank=False, null=False)
