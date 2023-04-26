from django.contrib.auth.models import AbstractUser
from django.db import models
from feed.models import FeedManager

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

    feed_manager = FeedManager()

    def get_viewable_reviews(self):
        return self.feed_manager.get_viewable_reviews(self)

    def get_viewable_tickets(self):
        return self.feed_manager.get_viewable_tickets(self)
