from django import forms


from reviews.models import Review

class ReviewForm(forms.ModelForm):
  edit_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)
  class Meta:
    model = Review
    fields = ['headline', 'rating', 'body']
    widgets = {
      'rating': forms.RadioSelect(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')],
                                  # attrs={"class":"inLineRadioContainer"}),
                                  attrs={"style":"display:flex;flex-direction:row;gap:30px;justify-content:space-around;"}),
      'body': forms.Textarea(attrs={'rows': 6}),
      }
    labels={
      'headline': 'Titre',
      'rating': 'Note',
      'body': 'Commentaire',

        }

class DeleteReviewForm(forms.Form):
  delete_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)