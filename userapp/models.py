from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    jins = models.CharField(max_length=10)
    shahar = models.CharField(max_length=100)
    davlat = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


