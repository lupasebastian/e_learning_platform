from django.urls import path

from .views import UserDetailView, GroupList, GroupView, CourseView, LessonDetailView, TeacherMainView

urlpatterns = [
    path('user_details/', UserDetailView.as_view(), name='user_detail_view'),
    path('teacher/', TeacherMainView.as_view(), name='teacher_main'),
    path('groups/', GroupList.as_view(), name='group_list'),
    path('groups/<slug:slug>/', GroupView.as_view(), name='group'),
    path('courses/<slug:slug>/', CourseView.as_view(), name='course'),
    path('lesson/<slug:slug>/', LessonDetailView.as_view(), name='lesson'),
]
