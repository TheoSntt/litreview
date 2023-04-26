from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from tickets.models import Ticket
from reviews.models import Review
from reviews.forms import ReviewForm, DeleteReviewForm

@login_required
def create_review(request, ticket_id):
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            review = form.save(commit=False)
            review.user = request.user
            review.ticket = Ticket.objects.get(id=ticket_id)
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
        'delete_form': delete_form,
        }     

    return render(request,'reviews/update_review.html', context=context)