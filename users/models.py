from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    email = models.CharField(max_length=100, null=True, unique=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_org_admin = models.BooleanField(default=False)
    is_stuff = models.BooleanField(default=False)



    def __str__(self):
        return self.email
