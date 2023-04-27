from itertools import chain

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tickets.models import Ticket
from reviews.models import Review
from django.core.paginator import Paginator



@login_required
def feed(request):
    # tickets = Ticket.objects.all()
    # reviews= Review.objects.all()
    # tickets_and_reviews = sorted(
    #     chain(tickets, reviews),
    #     key=lambda instance: instance.time_created,
    #     reverse=True
    # )

    tickets_and_reviews = request.user.get_feed()
    logged_user = request.user

    paginator = Paginator(tickets_and_reviews, 2)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context={
        'page_obj':page_obj,
        'logged_user':logged_user
    }

    return render(request, 'feed/feed.html', context=context)

@login_required
def users_posts_feed(request):
    # tickets = Ticket.objects.all()
    # reviews= Review.objects.all()
    # tickets_and_reviews = sorted(
    #     chain(tickets, reviews),
    #     key=lambda instance: instance.time_created,
    #     reverse=True
    # )

    tickets_and_reviews = request.user.get_own_posts_feed()
    logged_user = request.user

    paginator = Paginator(tickets_and_reviews, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context={
        'page_obj':page_obj,
        'logged_user':logged_user
    }

    return render(request, 'feed/users_posts_feed.html', context=context)
