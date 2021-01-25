from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Course, Post, Lesson, Group, Grade, Attendance, Attachment


class CreateCourseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        users = ((user.id, f'{user.first_name} {user.last_name}') for user in User.objects.filter(groups__name="teacher"))
        self.fields['teacher'].choices = users

    class Meta:
        model = Course
        fields = '__all__'


class CreatePostForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Post
        fields = '__all__'


class CreateLessonForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Lesson
        fields = '__all__'


class CreateGroupForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Group
        fields = '__all__'


class CreateGradeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Grade
        fields = '__all__'


class CreateAttendanceForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Attendance
        fields = '__all__'


class CreateAttachmentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

    class Meta:
        model = Attachment
        fields = '__all__'
