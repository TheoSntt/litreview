from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
