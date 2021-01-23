from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView

# Create your views here.
from accounts.models import UserProfile
from django.views.generic.base import View

from viewer.models import Course

from viewer.forms import CreateCourseForm


class WelcomePageView(TemplateView):
    template_name = 'home.html'


class MainView(View):
    pass


class TeacherMainView:
    pass


class ParentMainView:
    pass


class StudentDetailView:
    pass


class UnauthorizedView:
    pass


class GroupView:
    pass


class CourseView:
    pass


class JournalView:
    pass


class UserDetailView(DetailView):
    template_name = 'user_detail_template.html'
    model = UserProfile


class CourseCreateView(CreateView):
    template_name = 'create_form.html'
    model = Course
    form_class = CreateCourseForm
    success_url = reverse_lazy('main_view')