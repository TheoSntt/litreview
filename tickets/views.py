from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from tickets.models import Ticket
from tickets.forms import TicketForm

@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            ticket = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('home')

    else:
        form = TicketForm()
    
    return render(request,
                  'tickets/create_ticket.html',
                  {'form': form})


@login_required
def update_ticket(request, id):
    ticket = Ticket.objects.get(id=id)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('home')
    else:
        form = TicketForm(instance=ticket)

    return render(request,
                'tickets/update_ticket.html',
                {'form': form})