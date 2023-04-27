from django.db import models
from tickets.models import Ticket
from reviews.models import Review
from itertools import chain


class FeedManager(models.Manager):
    # def get_viewable_tickets(self, user):
    #     # Logic to retrieve tickets from followed users and self
    #     user_tickets=user.tickets.all()
    #     followed_tickets = Ticket.objects.filter(user__in=user.follows.all())
    #     viewable_tickets = user_tickets.union(followed_tickets)
    #     return viewable_tickets

    # def get_viewable_reviews(self, user):
    #     # Logic to retrieve reviews from followed users and self
    #     user_reviews=user.reviews.all()
    #     followed_reviews = Review.objects.filter(user__in=user.follows.all())
    #     viewable_reviews = user_reviews.union(followed_reviews)
    #     return viewable_reviews
    
    def get_user_feed(self, user):
        # Calls the 2 previous functions and merge the lists
        # tickets = self.get_viewable_tickets(user)
        # reviews = self.get_viewable_reviews(user)
        tickets = Ticket.objects.filter(user__in=user.follows.all()) | user.tickets.all()
        reviews = Review.objects.filter(user__in=user.follows.all()) | user.reviews.all() | Review.objects.filter(ticket__in=tickets)
        reviews = reviews.distinct()
        tickets_and_reviews = sorted(
            chain(tickets, reviews),
            key=lambda instance: instance.time_created,
            reverse=True
        )
        return tickets_and_reviews
    
    def get_by_natural_key(self, username):
        return self.model.objects.get_by_natural_key(username)