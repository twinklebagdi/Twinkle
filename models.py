from django.contrib import auth
from django.db import models

class User (models.Model):
    user= models.OneToOneField(auth.models.User, on_delete=models.CASCADE)
    name= models.CharField(max_length=20)
    age= models.IntegerField(max_length=3, min_length=2)