from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    follows = models.ManyToManyField(
        'self',
        symmetrical=False,
        verbose_name='suit',
        related_name='followers',
        through='follows.UserFollows'
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
