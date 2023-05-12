from django.db import models
from tickets.models import Ticket
from reviews.models import Review
from itertools import chain


class FeedManager(models.Manager):
    def get_user_feed(self, user):
        # Calls the 2 previous functions and merge the lists
        # tickets = self.get_viewable_tickets(user)
        # reviews = self.get_viewable_reviews(user)
        followed_tickets = Ticket.objects.filter(user__in=user.follows.all())
        self_tickets = user.tickets.all()
        tickets = followed_tickets | self_tickets
        followed_reviews = Review.objects.filter(user__in=user.follows.all())
        self_reviews = user.reviews.all()
        reviews_of_followed_tickets = Review.objects.filter(ticket__in=tickets)
        reviews = followed_reviews | self_reviews | reviews_of_followed_tickets
        reviews = reviews.distinct()
        tickets_and_reviews = sorted(
            chain(tickets, reviews),
            key=lambda instance: instance.time_created,
            reverse=True
        )
        return tickets_and_reviews

    def get_users_posts(self, user):
        tickets = user.tickets.all()
        reviews = user.reviews.all()
        tickets_and_reviews = sorted(
            chain(tickets, reviews),
            key=lambda instance: instance.time_created,
            reverse=True
        )
        return tickets_and_reviews

    def get_by_natural_key(self, username):
        return self.model.objects.get_by_natural_key(username)
