from django.contrib.auth import get_user_model
<<<<<<< HEAD

from main.models import Users
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy


# User = get_user_model()

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomlete': 'email'})
    )

    class Meta(UserCreationForm.Meta):
        model = Users
        field = ("Username", "email")
=======
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")
>>>>>>> 683e5c7173bc422d7a3c8c25d46c42046ba8a083

