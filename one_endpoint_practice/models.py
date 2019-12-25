from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class MyChannel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    subscriberCount = models.IntegerField(blank=True, null=True)
    videoCount = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
    