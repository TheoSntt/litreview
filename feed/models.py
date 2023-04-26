from django.db import models
from tickets.models import Ticket
from reviews.models import Review


class FeedManager(models.Manager):
    def get_viewable_reviews(self, user):
        # Logic to retrieve reviews from followed users and self
        pass

    def get_viewable_tickets(self, user):
        # Logic to retrieve tickets from followed users and self
        pass
