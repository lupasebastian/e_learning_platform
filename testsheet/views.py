from django.http import request
from django.shortcuts import render
from django.contrib.auth.backends import Permission
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import View, CreateView, DetailView, ListView, TemplateView
from django.views.generic.detail import SingleObjectMixin

from .models import Test, QuestionType, QuestionType, TestQuestion,TestTeacherAnswer, TestStudentAnswer
from .forms import CreateTestForm
# Create your views here.


#Widok wszystkich testów

# django.contrib.auth.get_user_model()
# def post_save_receiver(sender, instance, created, **kwargs):
#    pass

# post_save.connect(post_save_receiver, sender=settings.AUTH_USER_MODEL)

class TestListView(ListView):

    model = Test
    template_name = 'test_list.html'


class TestDetailView(ListView):

    model = TestQuestion
    template_name = 'testsheet.html'
    queryset = TestQuestion.objects.filter(test_id=0)


class CreateTestView(CreateView):
    form_class = CreateTestForm
    model = Test
    template_name = 'test_add.html'

#widok pytanie + form na odpowiedź
class TestFillView(DetailView):
    form_class = CreateTestForm
    template_name = 'test_fill.html'
    model = Test






