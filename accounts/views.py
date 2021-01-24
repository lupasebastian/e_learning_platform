from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy

# Create your views here.
from .forms import SignUpForm


class MyLoginView(LoginView):
    template_name = 'accounts_form.html'


class MyPasswordChangeView(PasswordChangeView):
    template_name = 'accounts_form.html'
    success_url = reverse_lazy('main_view')


class SignUpView(CreateView):
    template_name = 'accounts_form.html'
    form_class = SignUpForm
    success_url = reverse_lazy('main_view')


def login_success(request):
    if request.user.groups.filter(name='student').exists():
        return redirect('group_list')
    elif request.user.groups.filter(name='teacher').extists() or request.user.groups.filter(name='supervisor').extists():
        return redirect('home')
    else:
        return redirect('sign_up_view')
