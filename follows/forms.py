from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()


class FollowUsersForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['follows']