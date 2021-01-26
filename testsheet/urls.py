from django.urls import path
from django.views.generic import TemplateView

from .views import TestListView, QuestionView, AnswerView

urlpatterns = [
    path('', TestListView.as_view(), name='test_list'),
    path('test/<slug:pk>/', QuestionView.as_view(), name='test_sheet'),
    path('test/<slug:pk>/', AnswerView.as_view(), name='test_sheet'),
    path('test/fill/', AnswerView, name='test_fill')
]

