from django.urls import path
from django.views.generic import TemplateView

from .views import TestListView, TestDetailView

urlpatterns = [
    path('', TestListView.as_view(), name='test_list'),
    path('test/', TestDetailView.as_view(), name='test_sheet'),
    path('test/fill/', TestDetailView, name='test_fill')
]