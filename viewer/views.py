
import datetime
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.views.generic.detail import SingleObjectMixin

from accounts.models import UserProfile
from .forms import CreatePostForm, CreateLessonForm, CreateCourseForm, CreateGroupForm, \
    CreateAttachmentLessonForm, CreateAttachmentPostForm
from django.contrib.auth.models import User
from .models import Post, Group, Course, Lesson, Schedule, \
    AttachmentPost, AttachmentLesson


class MainView(TemplateView):
    template_name = 'home.html'


class TeacherMainView(ListView):
    template_name = 'teacher_main.html'
    model = Course

    def get_queryset(self):
        self.teacher = User.objects.filter(id=self.request.user.id).first()
        return Course.objects.filter(teacher=self.teacher)

    def get_context_data(self,  **kwargs):
        context = super(TeacherMainView, self).get_context_data(**kwargs)
        context['supervising_groups'] = Group.objects.filter(supervisor=self.request.user)
        context['teaching_groups'] = Course.objects.filter(teacher=self.request.user).values('group_id', 'group_id__symbol').distinct()
        return context


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
        # context['members'] = User.objects.filter(groups__name="student")
        context['posts'] = Post.objects.filter(group_id=self.object)
        context['courses'] = Course.objects.filter(group_id=self.object)
        context['group'] = self.object
        schedule = Schedule.objects.filter(course_id__group_id=self.object).order_by('day_of_week').order_by('start_time')
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
        times = [
            datetime.time(hour=8, minute=0),
            datetime.time(hour=9, minute=0),
            datetime.time(hour=10, minute=0),
            datetime.time(hour=11, minute=0),
            datetime.time(hour=12, minute=0),
            datetime.time(hour=13, minute=0),
            datetime.time(hour=14, minute=0),
            datetime.time(hour=15, minute=0)
        ]
        schedule_table = [
            ['time', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
        ]
        for time in times:
            schedule_table.append([time] + 5*[''])
        for el in schedule:
            col = days.index(el.day_of_week)+1
            row = times.index(el.start_time)+1
            if col and row:
                schedule_table[row][col] = el.course_id.name
        context['schedule'] = schedule_table
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

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Lesson.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(LessonDetailView, self).get_context_data(**kwargs)
        context['attachments'] = AttachmentLesson.objects.filter(lesson_id=self.object)
        return context


class JournalView:
    pass


class UserDetailView(DetailView):
    template_name = 'user_detail_template.html'
    model = UserProfile

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context['supervisor_group'] = Group.objects.filter(supervisor__profile_user=self.kwargs['pk']).first()
        context['courses'] = Course.objects.filter(teacher__profile_user=self.kwargs['pk'])
        return context


class CreateCourseView(CreateView):
    template_name = 'creation_form_course_etc.html'
    model = Course
    form_class = CreateCourseForm
    success_url = reverse_lazy('teacher_main')


class CreatePostView(CreateView):
    template_name = 'creation_form_course_etc.html'
    model = Post
    form_class = CreatePostForm
    success_url = reverse_lazy('attachment_post_upload')

    def get_form_kwargs(self):
        kwargs = super(CreatePostView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class CreateLessonView(CreateView):
    template_name = 'creation_form_course_etc.html'
    model = Lesson
    form_class = CreateLessonForm
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('attachment_lesson_upload')


class CreateGroupView(CreateView):
    template_name = 'creation_form_course_etc.html'
    model = Group
    form_class = CreateGroupForm
    success_url = reverse_lazy('main_view')


def attachment_lesson_upload(request):
    if request.method == 'POST':
        form = CreateAttachmentLessonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('teacher_main')
    else:
        form = CreateAttachmentLessonForm()
    return render(request, 'upload_form_attachment.html', {
        'form': form
    })


def attachment_post_upload(request):
    if request.method == 'POST':
        form = CreateAttachmentPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_view')
    else:
        form = CreateAttachmentPostForm()
    return render(request, 'upload_form_attachment.html', {
        'form': form
    })
