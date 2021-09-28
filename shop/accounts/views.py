from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View

from .forms import LoginForm, UserRegistrationForm


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


class UserRegistrationView(View):

    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'base_form.html', {'form': form,
                                                  'button': 'Zarejestuj'})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'register_done.html', {'new_user': user})

        return render(request, 'base_form.html', {'form': form,
                                                  'button': 'Zarejestuj'})
