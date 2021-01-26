from django.shortcuts import render
from django.contrib.auth.backends import Permission
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import View, CreateView, DetailView, ListView, TemplateView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.list import MultipleObjectMixin

from .models import Test, QuestionType, QuestionType, TestQuestion,TestTeacherAnswer, TestStudentAnswer
from .forms import CreateTestForm



class TestListView(ListView):

    model = Test
    template_name = 'test_list.html'


class QuestionView(SingleObjectMixin, ListView):

    model = TestQuestion
    template_name = 'testsheet.html'
    context_object_name = 'questions'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=TestQuestion.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(QuestionView, self).get_context_data(**kwargs)
        context['questions'] = TestQuestion.objects.filter(test_id=self.object.test_id)
        return context


class AnswerView(SingleObjectMixin, ListView):

    model = TestTeacherAnswer
    template_name = 'testsheet.html'
    context_object_name = 'answers'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=TestTeacherAnswer.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AnswerView, self).get_context_data(**kwargs)
        context['answers'] = TestTeacherAnswer.objects.filter(test_id=self.object.test_id)
        return context


class CreateTestView(CreateView):
    form_class = CreateTestForm
    model = Test
    template_name = 'test_add.html'


class TestFillView(DetailView):
    form_class = CreateTestForm
    template_name = 'test_fill.html'
    model = Test






