from django.shortcuts import render
from django.contrib.auth.backends import Permission
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.detail import SingleObjectMixin

from .models import Test, TestQuestion, TestTeacherAnswer
from .forms import CreateTestForm


class TestListView(ListView):

    model = Test
    template_name = 'test_list.html'


class QuestionView(SingleObjectMixin, ListView):


    model = TestQuestion
    template_name = 'testsheet.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=TestQuestion.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(QuestionView, self).get_context_data(**kwargs)
        context['questions'] = TestQuestion.objects.filter(test_id=self.object.id)
        context['answers'] = TestTeacherAnswer.objects.filter(question_id__test_id=self.object.id)
        return context



class AnswerView(SingleObjectMixin, ListView):
    pass
#
#     model = TestTeacherAnswer
#     template_name = 'answers.html'
#     context_object_name = 'answers'
#
#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object(queryset=TestTeacherAnswer.objects.all())
#         return super().get(request, *args, **kwargs)
#
#     def get_context_data(self, **kwargs):
#         context = super(AnswerView, self).get_context_data(**kwargs)
#         context['answers'] = TestTeacherAnswer.objects.filter(question_id=self.object.question_id)
#         return context


class CreateTestView(CreateView):
    form_class = CreateTestForm
    model = Test
    template_name = 'test_add.html'


class TestFillView(DetailView):
    form_class = CreateTestForm
    template_name = 'test_fill.html'
    model = Test






