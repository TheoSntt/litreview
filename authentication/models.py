from django.contrib.auth.models import AbstractUser
from django.db import models
from feed.models import FeedManager


class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    feed_manager = FeedManager()
    follows = models.ManyToManyField(
        'self',
        symmetrical=False,
        verbose_name='suit',
        related_name='followers',
        through='follows.UserFollows'
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def get_feed(self):
        return User.feed_manager.get_user_feed(self)

    def get_own_posts_feed(self):
        return User.feed_manager.get_users_posts(self)
