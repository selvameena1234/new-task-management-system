from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User  # or your custom User model
from django.db import models

class User(AbstractUser):
    role = models.CharField(max_length=10, choices=[
        ('admin', 'Admin'),
        ('user', 'User'),
    ])