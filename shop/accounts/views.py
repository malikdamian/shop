from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from .forms import LoginForm


class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form,
                                              'button': 'Zaloguj'})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                form = LoginForm()
        return render(request, 'login.html', {'form': form,
                                              'button': 'Zaloguj'})


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('/')


