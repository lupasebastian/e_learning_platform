from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class WelcomePageView(TemplateView):
    template_name = 'home.html'


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
