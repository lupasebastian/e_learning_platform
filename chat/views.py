from django.shortcuts import render


def chat_main_view(request):
    return render(request, 'chat/chat_main_view_template.html')


def chat_room_view(request, room_name):
    return render(request, 'chat/room_template.html', {
        'room_name': room_name
    })