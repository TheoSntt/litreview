from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from tickets.models import Ticket
from tickets.forms import TicketForm, DeleteTicketForm
from django.http import HttpResponseForbidden


@login_required
def create_ticket(request):
    form = TicketForm()
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('feed')

    return render(request,
                  'tickets/create_ticket.html',
                  {'form': form})


@login_required
def update_ticket(request, id):
    ticket = Ticket.objects.get(id=id)
    # Restricting access to the view to the owner of the ticket
    if request.user != ticket.user:
        return HttpResponseForbidden()
    edit_form = TicketForm(instance=ticket)
    delete_form = DeleteTicketForm()
    if request.method == 'POST':
        if 'edit_ticket' in request.POST:
            edit_form = TicketForm(request.POST, request.FILES, instance=ticket)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('feed')
        if 'delete_ticket' in request.POST:
            delete_form = DeleteTicketForm(request.POST)
            if delete_form.is_valid():
                ticket.delete()
                return redirect('feed')

    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,
        }

    return render(request, 'tickets/update_ticket.html', context=context)
