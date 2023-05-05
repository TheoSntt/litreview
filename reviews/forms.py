from django import forms


from reviews.models import Review

class ReviewForm(forms.ModelForm):
  edit_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)
  class Meta:
    model = Review
    fields = ['headline', 'rating', 'body']
    widgets = {
      'rating': forms.RadioSelect(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')],
                                  attrs={"class":"tropclassecetteclass"})
                                  }

class DeleteReviewForm(forms.Form):
  delete_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)