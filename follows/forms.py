from django.contrib.auth import get_user_model
from django import forms
from django_select2.forms import ModelSelect2Widget
from follows.models import UserFollows
User = get_user_model()


class UsersWidget(ModelSelect2Widget):
    search_fields = [
        "username__icontains",
    ]


class FollowUserForm(forms.ModelForm):
    class Meta:
        model = UserFollows
        fields = ('followed_user',)
        widgets = {
            "followed_user": UsersWidget,
        }
        labels = {
            "followed_user": 'Nom d\'utilisateur',
        }

    def __init__(self, current_user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        q = User.objects.exclude(id=current_user.id).exclude(id__in=current_user.follows.all())
        self.fields['followed_user'].queryset = q
