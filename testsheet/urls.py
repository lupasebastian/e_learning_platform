from django.urls import path
from django.views.generic import TemplateView

from .views import TestListView, QuestionView, AnswerView, CreateTestView, CreateAnswerView, CreateQuestionView

urlpatterns = [
    path('test/', TestListView.as_view(), name='test_list'),
    path('test/<slug:pk>/', QuestionView.as_view(), name='test_sheet'),
    path('answers/', AnswerView.as_view(), name='answers'),
    path('test/fill/', AnswerView, name='test_fill'),
    path('test/add/', CreateTestView.as_view(), name='add_test'),
    path('test/add/question/', CreateQuestionView.as_view(), name='add_q'),
    path('test/add/answer/', CreateAnswerView.as_view(), name='add_q')
]

