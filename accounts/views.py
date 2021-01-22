from django.contrib.auth.views import LoginView, PasswordChangeView
from django.views.generic import CreateView
from django.shortcuts import render

# Create your views here.


class MyLoginView(LoginView):
    pass


class MyPasswordChangeView(PasswordChangeView):
    pass


class SignUpView(CreateView):
    pass


class UserDetailView:
    pass


class MyProfileDetailView:
    pass
