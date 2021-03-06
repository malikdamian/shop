from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from .forms import LoginForm, UserRegistrationForm


class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('name_app:index')
            else:
                form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('name_app:index')


class UserRegistrationView(View):

    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'accounts/register_done.html', {'new_user': user})

        return render(request, 'accounts/register.html', {'form': form})


class UserInfoView(View):

    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        return render(request, 'accounts/user_info.html', {'user': user})
