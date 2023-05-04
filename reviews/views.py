from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from tickets.models import Ticket
from reviews.models import Review
from reviews.forms import ReviewForm, DeleteReviewForm
from tickets.forms import TicketForm
from django.http import HttpResponseForbidden

@login_required
def create_review(request, ticket_id):
    # Restricting access to the view if the ticket has already been reviewed
    ticket = Ticket.objects.get(id=ticket_id)
    if ticket.has_been_reviewed():
        return HttpResponseForbidden()
    
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            review = form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('feed')
 
    return render(request,
                  'reviews/create_review.html',
                  {'form': form})


@login_required
def update_review(request, review_id):
    review = Review.objects.get(id=review_id)
    
    # Restricting access to the view to the owner of the review
    if request.user != review.user:
        return HttpResponseForbidden()
    
    edit_form = ReviewForm(instance=review)
    delete_form = DeleteReviewForm()
    if request.method == 'POST':
        if 'edit_review' in request.POST:
            edit_form = ReviewForm(request.POST, instance=review)
            if edit_form.is_valid():
                # mettre à jour le groupe existant dans la base de données
                edit_form.save()
                # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
                return redirect('feed')
        if 'delete_review' in request.POST:
            delete_form = DeleteReviewForm(request.POST)
            if delete_form.is_valid():
                # mettre à jour le groupe existant dans la base de données
                review.delete()
                # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
                return redirect('feed')
        
    context = {
        'edit_form': edit_form,
        'delete_form': delete_form
        }     

    return render(request,'reviews/update_review.html', context=context)


@login_required
def create_review_and_ticket(request):
    review_form = ReviewForm()
    ticket_form = TicketForm()
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        ticket_form = TicketForm(request.POST, request.FILES)
        if all([review_form.is_valid(), ticket_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('feed')
    context = {
        'review_form': review_form,
        'ticket_form': ticket_form,
    }
    return render(request, 'reviews/create_review_and_ticket.html', context=context)