from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from accounts.models import UserProfile
from .models import Post, Group


# Create your views here.


class WelcomePageView(TemplateView):
    template_name = 'home.html'


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
