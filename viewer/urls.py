from django.urls import path

from .views import UserDetailView, MainView

urlpatterns = [
    path('user_details/', UserDetailView.as_view(), name='user_detail_view'),
    path('main_view/', MainView.as_view(), name='main_view')
]