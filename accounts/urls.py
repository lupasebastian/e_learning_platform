from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import MyLoginView, MyPasswordChangeView, SignUpView

urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login_view'),
    path('password_change/', MyPasswordChangeView.as_view(),
         name='password_change_view'),
    path('sign_up/', SignUpView.as_view(), name='sign_up_view'),
    path('logout/', LogoutView.as_view(), name='logout_view'),
]