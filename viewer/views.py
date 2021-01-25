from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.views.generic.detail import SingleObjectMixin
from accounts.models import UserProfile
from .forms import CreatePostForm, CreateLessonForm, CreateCourseForm, CreateGroupForm, CreateGradeForm, \
    CreateAttendanceForm, CreateAttachmentForm
from .models import Post, Group, Course, Lesson, Grade, Attachment, Attendance


class WelcomePageView(TemplateView):
    template_name = 'home.html'


class MainView(View):
    pass


class TeacherMainView:
    pass


class ParentMainView:
    pass


class StudentDetailView:
    pass


class UnauthorizedView:
    pass


class GroupList(ListView):
    template_name = 'group_list.html'
    model = Group


class GroupView(SingleObjectMixin, ListView):
    template_name = 'group.html'
    model = Group

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Group.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(GroupView, self).get_context_data(**kwargs)
        context['members'] = UserProfile.objects.filter(group_id=self.object)
        context['posts'] = Post.objects.filter(group_id=self.object)
        context['courses'] = Course.objects.filter(group_id=self.object)
        context['group'] = self.object
        return context


class CourseView(DetailView):
    template_name = 'course.html'
    model = Course

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Course.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CourseView, self).get_context_data(**kwargs)
        context['members'] = UserProfile.objects.filter(group_id=self.object.group_id)
        context['posts'] = Post.objects.filter(course_id=self.object)
        context['lessons'] = Lesson.objects.filter(course_id=self.object)
        return context


class LessonDetailView(DetailView):
    template_name = 'lesson.html'
    model = Lesson


class JournalView:
    pass


class UserDetailView(DetailView):
    template_name = 'user_detail_template.html'
    model = UserProfile


class CreateCourseView(CreateView):
    template_name = 'creation_form_course_etc.html'
    model = Course
    form_class = CreateCourseForm
    success_url = reverse_lazy('main_view')


class CreatePostView(CreateView):
    template_name = 'creation_form_course_etc.html'
    model = Post
    form_class = CreatePostForm
    success_url = reverse_lazy('main_view')


class CreateLessonView(CreateView):
    template_name = 'creation_form_course_etc.html'
    model = Lesson
    form_class = CreateLessonForm
    success_url = reverse_lazy('main_view')


class CreateGroupView(CreateView):
    template_name = 'creation_form_course_etc.html'
    model = Group
    form_class = CreateGroupForm
    success_url = reverse_lazy('main_view')


class CreateGradeView(CreateView):
    template_name = 'creation_form_course_etc.html'
    model = Grade
    form_class = CreateGradeForm
    success_url = reverse_lazy('main_view')


class CreateAttendanceView(CreateView):
    template_name = 'creation_form_course_etc.html'
    model = Attendance
    form_class = CreateAttendanceForm
    success_url = reverse_lazy('main_view')


class CreateAttachmentView(CreateView):
    template_name = 'creation_form_course_etc.html'
    model = Attachment
    form_class = CreateAttachmentForm
    success_url = reverse_lazy('main_view')