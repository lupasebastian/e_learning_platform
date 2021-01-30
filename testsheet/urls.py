from django.urls import path
from django.views.generic import TemplateView

from .views import TestListView, QuestionView, CreateTestView, CreateAnswerView, CreateQuestionView, TestFillView

urlpatterns = [
    path('test/', TestListView.as_view(), name='test_list'),
    path('test/<slug:pk>/', QuestionView.as_view(), name='test_sheet'),
    path('test/<slug:pk>/fill/', TestFillView , name='test_fill'),
    path('add/', CreateTestView.as_view(), name='add_test'),
    path('add/question/', CreateQuestionView.as_view(), name='add_question'),
    path('add/answer/', CreateAnswerView.as_view(), name='add_answer')
]

