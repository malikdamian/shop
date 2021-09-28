from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                       'placeholder': 'Użytkownik'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                           'placeholder': 'Hasło'}))


