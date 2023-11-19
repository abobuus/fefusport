from django import forms
from django.contrib.auth.forms import UserCreationForm
from.models import User


class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=255, required=True)
    about_me = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = User
        fields = ('username', 'name', 'about_me', 'password1', 'password2')
