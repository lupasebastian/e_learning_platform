from django.urls import path

from .views import chat_main_view, chat_room_view

urlpatterns = [
    path('', chat_main_view, name='chat_main_view'),
    path('<str:room_name>/', chat_room_view, name='chat_room_view'),
]
