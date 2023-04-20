from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tickets.models import Ticket



@login_required
def home(request):
    tickets = Ticket.objects.all()
    return render(request, 'feed/home.html',
    {'tickets': tickets})
