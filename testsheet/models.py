from django.contrib.auth.models import User
from django.db.models import CharField, BooleanField, DateTimeField, IntegerField, ManyToManyField, \
    ForeignKey, TextField, Model, DO_NOTHING, CASCADE


class Test(Model):
    course_id = ForeignKey('viewer.Course', on_delete=DO_NOTHING, related_name='course_test')
    teacher = ForeignKey(User, on_delete=DO_NOTHING)
    created = DateTimeField(auto_created=True)
    title = CharField(max_length=128)
    description = CharField(max_length=512)

    class Meta:
        ordering = ['course_id']

    def __str__(self):
        return f'{self.course_id} {self.title} {self.description}'


class QuestionType(Model):
    name = CharField(max_length=128)

    def __str__(self):
        return self.name


class TestQuestion(Model):
    test_id = ForeignKey(Test, on_delete=CASCADE, related_name='question_test')
    type_id = ForeignKey(QuestionType, on_delete=DO_NOTHING, related_name='question_type')
    question_number = IntegerField(blank=True, null=True)
    text_content = TextField()

    class Meta:
        ordering = ['test_id', 'question_number']

    def __str__(self):
        return f'{self.test_id} {self.question_number}. {self.text_content}'


class TestTeacherAnswer(Model):
    question_id = ForeignKey(TestQuestion, default=None, blank=True, on_delete=CASCADE)
    answer_num = CharField(max_length=1, default='A')
    answer_text = CharField(max_length=128)
    correct = BooleanField()

    def __str__(self):
        return f'{self.answer_num}. {self.answer_text}'


class TestStudentAnswer(Model):
    question_id = ForeignKey(TestQuestion, on_delete=DO_NOTHING)
    answer_text = TextField()
