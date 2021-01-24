from django.contrib.auth.models import User
from django.forms import ModelForm, Select, ChoiceField

from viewer.models import Course


class CreateCourseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(User.objects.filter(groups__name="teacher"))
        teachers_choices = ((user, f'{user.first_name}' + ' ' + f'{user.last_name}') for user in
                            User.objects.filter(groups__name="teacher"))
        self.fields['teacher'].choices = teachers_choices

    class Meta:
        model = Course
        fields = '__all__'
        teacher = ChoiceField()
