from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                       'placeholder': 'Użytkownik'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                           'placeholder': 'Hasło'}))


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                           'placeholder': 'Hasło'}))
    password_2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                             'placeholder': 'Powtórz hasło'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': 'Nazwa użytkownika',
                                               'help_text': ''}),
            'first_name': forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Imię'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Nazwisko'}),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'placeholder': 'Email'})
        }
        labels = {
            'username': '',
            'first_name': '',
            'last_name': '',
            'email': '',
        }
        help_texts = {
            'username': '',
        }

    def clean_password_2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password_2']:
            raise forms.ValidationError('Hasła nie sa identyczne')
        return cd['password_2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('Użytkownik o takim emailu już istnieje.')

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError('Użytkownik o tej nazwie już istnieje.')
