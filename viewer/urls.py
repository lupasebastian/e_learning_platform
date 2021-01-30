from django.conf.urls.static import static
from django.urls import path


from .views import UserDetailView, MainView, CreateCourseView, CreatePostView, \
    CreateLessonView, CreateGroupView, TeacherMainView, GroupList, GroupView, \
    CourseView, LessonDetailView, attachment_lesson_upload


urlpatterns = [
    path('user_details/', UserDetailView.as_view(), name='user_detail_view'),
    path('main_view/', MainView.as_view(), name='main_view'),
    path('profile/<int:pk>/', UserDetailView.as_view(), name='profile'),
    path('teacher/', TeacherMainView.as_view(), name='teacher_main'),
    path('groups/', GroupList.as_view(), name='group_list'),
    path('groups/<slug:slug>/', GroupView.as_view(), name='group'),
    path('courses/<slug:slug>/', CourseView.as_view(), name='course'),
    path('lesson/<slug:slug>/', LessonDetailView.as_view(), name='lesson'),
    path('create_course/', CreateCourseView.as_view(), name='create_course_view'),
    path('groups/<slug:slug>/create_post/', CreatePostView.as_view(), name='create_post_view'),
    path('create_lesson/', CreateLessonView.as_view(), name='create_lesson_view'),
    path('create_group/', CreateGroupView.as_view(), name='create_group_view'),
    path('upload_attachment_lesson', attachment_lesson_upload, name='attachment_lesson_upload'),
]
