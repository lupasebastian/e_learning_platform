"""e_learning_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from viewer.views import WelcomePageView, GroupList, GroupView, CourseView, LessonDetailView

# from viewer.models import Role, Group, Course, Lesson, Post, Attachment, PostAttachment, LessonAttachment, Grade, Attendance
# from testsheet.models import Test, QuestionType, TestQuestion, TestTeacherAnswer, TestStudentAnswer
# from accounts.models import UserProfile

# admin.site.register(Role)
# admin.site.register(Group)
# admin.site.register(Course)
# admin.site.register(Lesson)
# admin.site.register(Post)
# admin.site.register(Attachment)
# admin.site.register(PostAttachment)
# admin.site.register(LessonAttachment)
# admin.site.register(Grade)
# admin.site.register(Attendance)
# admin.site.register(Test)
# admin.site.register(QuestionType)
# admin.site.register(TestQuestion)
# admin.site.register(TestTeacherAnswer)
# admin.site.register(TestStudentAnswer)
# admin.site.register(UserProfile)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', WelcomePageView.as_view(), name='home'),
    path('groups/', GroupList.as_view(), name='group_list'),
    path('groups/<slug:slug>/', GroupView.as_view(), name='group'),
    path('courses/<slug:slug>/', CourseView.as_view(), name='course'),
    path('lesson/<slug:slug>/', LessonDetailView.as_view(), name='lesson'),
    path('accounts/', include('accounts.urls')),
    path('testsheet/', include('testsheet.urls')),
    path('viewer/', include('viewer.urls')),
    path('chat/', include('chat.urls')),
]
