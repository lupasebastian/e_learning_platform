from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView, DetailView
from .models import Test, QuestionType, QuestionType, TestQuestion,TestTeacherAnswer, TestStudentAnswer
# Create your views here.


@login_required
class TestDetailView(PermissionRequiredMixin, DetailView):
    pass


@login_required
class CreateTestForm(PermissionRequiredMixin, CreateView):
    model = Test
    template_name = 'test.html'
