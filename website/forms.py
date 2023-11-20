from django import forms
from .models import *


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'slug', 'content', 'photo', 'contacts_vk', 'contacts_tg']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-name'}),
            'content': forms.Textarea(attrs={'rows': 8}),
        }
