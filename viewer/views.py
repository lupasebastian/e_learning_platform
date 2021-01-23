from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from accounts.models import UserProfile
from .models import Post, Group

<<<<<<< HEAD
=======
# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView
>>>>>>> dev

# Create your views here.
from accounts.models import UserProfile
from django.views.generic.base import View

from viewer.models import Course

from viewer.forms import CreateCourseForm


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


class GroupView(ListView):
    template_name = 'group.html'
    model = Group

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Group.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(GroupView, self).get_context_data(**kwargs)
        context['members'] = UserProfile.objects.filter(group_id=self.object)
        context['posts'] = Post.objects.filter(group_id=self.object)
        context['group'] = self.object
        return context

    # def get_queryset(self):
    #     return Post.objects.filter(group_id=self.object)


class CourseView:
    pass


class JournalView:
    pass


class CreateLessonForm:
    pass


class UserDetailView(DetailView):
    template_name = 'user_detail_template.html'
    model = UserProfile


class CourseCreateView(CreateView):
    template_name = 'create_form.html'
    model = Course
    form_class = CreateCourseForm
    success_url = reverse_lazy('main_view')

