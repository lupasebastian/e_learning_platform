from django.forms import ModelForm
from .models import Test, TestQuestion, TestStudentAnswer, TestTeacherAnswer
# from viewer.models import Attachment


class CreateTestForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Test
        fields = '__all__'

class QuestionCreateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = TestQuestion
        fields = '__all__'

class AnswerCreateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = TestTeacherAnswer
        fields = '__all__'

# class CreateAttachmentForm(ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(self, *args, **kwargs)
#
#     class Meta:
#         model = Attachment
#         fields = '__all__'

class FillTestForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

    class Meta:
        model = TestStudentAnswer
        fields = '__all__'
