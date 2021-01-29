from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Course, Post, Lesson, Group, Grade, Attendance, \
    AttachmentPost, AttachmentLesson


class CreateCourseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['teacher'].choices = [
            (user.id, f'{user.first_name} {user.last_name}') for
            user in User.objects.filter(groups__name="teacher")
        ]
        self.fields['group_id'].choices = [
            (group.id, group.symbol) for group in Group.objects.all()
        ]

    class Meta:
        model = Course
        fields = '__all__'


class CreatePostForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_id = user.id

    class Meta:
        model = Post
        fields = '__all__'
        exclude = ('user_id', 'published',)


class CreateLessonForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].choices = [
            (user.id, f'{user.first_name} {user.last_name}') for
            user in User.objects.filter(groups__name="teacher")
        ]
        self.fields['datetime_start'].widget.attrs['placeholder'] = \
            'YYYY-MM-DD HH-MM'
        self.fields['datetime_end'].widget.attrs['placeholder'] = \
            'YYYY-MM-DD HH-MM'

    class Meta:
        model = Lesson
        fields = '__all__'


class CreateGroupForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['supervisor'].choices = [
            (user.id, f'{user.first_name} {user.last_name}') for
            user in User.objects.filter(groups__name='supervisor')
        ]

    class Meta:
        model = Group
        fields = '__all__'


class CreateGradeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['student_id'].choices = [
            (user.id, f'{user.first_name} {user.last_name}') for
            user in User.objects.filter(groups__name='student')
        ]
        self.fields['teacher_id'].choices = [
            (user.id, f'{user.first_name} {user.last_name}') for
            user in User.objects.filter(groups__name='teacher')
        ]
        self.fields['date'].widget.attrs['placeholder'] = 'YYYY-MM-DD HH-MM'

    class Meta:
        model = Grade
        fields = '__all__'


class CreateAttendanceForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['student_id'].choices = [
            (user.id, f'{user.first_name} {user.last_name}') for
            user in User.objects.filter(groups__name='student')
        ]
        self.fields['teacher_id'].choices = [
            (user.id, f'{user.first_name} {user.last_name}') for
            user in User.objects.filter(groups__name='teacher')
        ]
        self.fields['lesson_id'].choices = [
            (lesson.id, f'{lesson.name}') for
            lesson in Lesson.objects.all()
        ]
        self.fields['date'].widget.attrs['placeholder'] = 'YYYY-MM-DD HH-MM'

    class Meta:
        model = Attendance
        fields = '__all__'


class CreateAttachmentPostForm(ModelForm):

    class Meta:
        model = AttachmentPost
        fields = '__all__'


class CreateAttachmentLessonForm(ModelForm):

    class Meta:
        model = AttachmentLesson
        fields = '__all__'
