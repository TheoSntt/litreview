from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

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