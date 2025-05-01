from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class User(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)