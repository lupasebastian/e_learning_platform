from django.contrib.auth.models import User
from django.db.models import CharField, BooleanField, DateField, DateTimeField,\
    ForeignKey, TextField, Model, DO_NOTHING, CASCADE
import viewer.models


class Test(Model):
    course_id = ForeignKey('viewer.Course', on_delete=DO_NOTHING, related_name='course_test')
    teacher = ForeignKey(User, on_delete=DO_NOTHING)
    created = DateTimeField()
    title = CharField(max_length=128)
    description = CharField(max_length=512)


class QuestionType(Model):
    name = CharField(max_length=128)

    def __str__(self):
        return self.name


class TestQuestion(Model):
    test_id = ForeignKey(Test, on_delete=CASCADE, related_name='question_test')
    type_id = ForeignKey(QuestionType, on_delete=DO_NOTHING, related_name='question_type')
    text_content = TextField()
    attachment = ForeignKey('viewer.Attachment', on_delete=DO_NOTHING)


class TestTeacherAnswer(Model):
    question_id = ForeignKey(TestQuestion, on_delete=CASCADE,)
    answer_text = CharField(max_length=128)
    correct = BooleanField()


class TestStudentAnswer(Model):
    question_id = ForeignKey(TestQuestion, on_delete=DO_NOTHING)
    answer_text = TextField()
