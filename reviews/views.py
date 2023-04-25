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
