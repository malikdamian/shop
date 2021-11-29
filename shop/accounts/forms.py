from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Row, Column
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(label='Użytkownik')
    password = forms.CharField(widget=forms.PasswordInput(), label='Hasło')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                'Logowanie',
            ),
            Row(
                Column('username'),
                Column('password')
            ),
            ButtonHolder(
                Submit('submit', 'Zaloguj', css_class='btn btn-success'),

            ),
        )


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput())
    password_2 = forms.CharField(label='Powtórz hasło', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        labels = {
            'username': 'Login',
            'first_name': 'Imię',
            'last_name': 'Nażwisko',
            'email': 'Email',
        }
        help_texts = {
            'username': '',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                'Rejestracja',
            ),
            Row(
                Column('username'),
                Column('email'),
            ),
            Row(
                Column('first_name'),
                Column('last_name'),
            ),
            Row(
                Column('password'),
                Column('password_2'),
            ),
            ButtonHolder(
                Submit('submit', 'Rejestracja', css_class='btn btn-success'),

            ),
        )

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
        return username

