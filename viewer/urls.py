from django.urls import path

from .views import UserDetailView, MainView, CreateCourseView, CreatePostView, CreateLessonView, CreateGroupView

urlpatterns = [
    path('user_details/', UserDetailView.as_view(), name='user_detail_view'),
    path('main_view/', MainView.as_view(), name='main_view'),
    path('create_course/', CreateCourseView.as_view(), name='create_course_view'),
    path('create_post/', CreatePostView.as_view(), name='create_post_view'),
    path('create_lesson/', CreateLessonView.as_view(), name='create_lesson_view'),
    path('create_group/', CreateGroupView.as_view(), name='create_group_view')
]