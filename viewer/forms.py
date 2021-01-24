from django.forms import ModelForm

from viewer.models import Course


class CreateCourseForm(ModelForm):
    pass
    # class Meta:
    #     model = Course
    #     fields = '__all__'
    #
    # teacher =