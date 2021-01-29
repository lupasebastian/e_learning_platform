from django.urls import path

from .views import UserDetailView, MainView, CreateCourseView, CreatePostView, \
    CreateLessonView, CreateGroupView, CreateGradeView, CreateAttendanceView, \
    CreateAttachmentPostView, CreateAttachmentLessonView, attachment_lesson_upload, \
    attachment_post_upload

urlpatterns = [
    path('user_details/', UserDetailView.as_view(), name='user_detail_view'),
    path('main_view/', MainView.as_view(), name='main_view'),
    path('create_course/', CreateCourseView.as_view(), name='create_course_view'),
    path('create_post/', CreatePostView.as_view(), name='create_post_view'),
    path('create_lesson/', CreateLessonView.as_view(), name='create_lesson_view'),
    path('create_group/', CreateGroupView.as_view(), name='create_group_view'),
    path('create_grade/', CreateGradeView.as_view(), name='create_grade_view'),
    path('create_attendance/', CreateAttendanceView.as_view(), name='create_attendance_view'),
    path('create_attachment_post/', CreateAttachmentPostView.as_view(), name='create_attachment_post'),
    path('create_attachment_lesson/', CreateAttachmentLessonView.as_view(), name='create_attachment_lesson'),
    path('upload_attachment_lesson_succesful', attachment_lesson_upload, name='attachment_lesson_upload'),
    path('upload_attachment_post_succesful', attachment_post_upload, name='attachment_post_upload'),
]