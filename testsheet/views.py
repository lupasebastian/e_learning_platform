from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.detail import SingleObjectMixin
from .models import Test, TestQuestion, TestTeacherAnswer
from .forms import CreateTestForm, QuestionCreateForm, AnswerCreateForm, FillTestForm

class TestListView(ListView):

    model = Test
    template_name = 'test_list.html'

class QuestionView(SingleObjectMixin, ListView):

    model = TestQuestion
    paginate_by = 1
    paginate_orphans = True
    template_name = 'testsheet.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=TestQuestion.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(QuestionView, self).get_context_data(**kwargs)
        context['questions'] = TestQuestion.objects.filter(test_id=self.object.id)
        context['answers'] = TestTeacherAnswer.objects.filter(question_id__test_id=self.object.id)
        return context


# AnswerView był testowy, można go usunąć.
class AnswerView(ListView):

    model = TestTeacherAnswer
    template_name = 'answers.html'
    context_object_name = 'answers'
    #
    # def get(self, request, *args, **kwargs):
    #     self.object = self.get_object(queryset=TestTeacherAnswer.objects.all())
    #     return super().get(request, *args, **kwargs)
    #
    # def get_context_data(self, **kwargs):
    #     context = super(AnswerView, self).get_context_data(**kwargs)
    #     context['answers'] = TestTeacherAnswer.objects.filter(question_id=self.object.question_id)
    #     return context


class CreateTestView(CreateView):
    form_class = CreateTestForm
    model = Test
    template_name = 'test_add.html'


class CreateQuestionView(CreateView):
    form_class = QuestionCreateForm
    model = TestQuestion
    template_name = 'test_add.html'


class CreateAnswerView(CreateView):
    form_class = AnswerCreateForm
    model = TestTeacherAnswer
    template_name = 'test_add.html'


class TestFillView(DetailView):
    form_class = FillTestForm
    template_name = 'test_fill.html'
    model = Test






