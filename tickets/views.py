from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from tickets.models import Ticket
from tickets.forms import TicketForm, DeleteTicketForm

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
            return redirect('home')
 
    return render(request,
                  'tickets/create_ticket.html',
                  {'form': form})




@login_required
def update_ticket(request, id):
    ticket = Ticket.objects.get(id=id)
    edit_form = TicketForm(instance=ticket)
    delete_form = DeleteTicketForm()
    if request.method == 'POST':
        if 'edit_ticket' in request.POST:
            edit_form = TicketForm(request.POST, request.FILES, instance=ticket)
            if edit_form.is_valid():
                # mettre à jour le groupe existant dans la base de données
                edit_form.save()
                # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
                return redirect('home')
        if 'delete_ticket' in request.POST:
            delete_form = DeleteTicketForm(request.POST)
            if delete_form.is_valid():
                # mettre à jour le groupe existant dans la base de données
                ticket.delete()
                # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
                return redirect('home')
        
    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,
        }     

    return render(request,'tickets/update_ticket.html', context=context)