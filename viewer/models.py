from django.db import models
from django.contrib.auth.models import User
from django.db.models import CharField, BooleanField, DateTimeField, FileField, FilePathField, \
    ForeignKey, IntegerField, TextField, Model, ManyToManyField, DO_NOTHING, CASCADE, SET_NULL


class Role(Model):
    name = CharField(max_length=128)

    def __str__(self):
        return self.name


class Group(Model):
    symbol = CharField(max_length=16)
    date_start = DateTimeField()
    date_end = DateTimeField()
    supervisor = ForeignKey(User, on_delete=DO_NOTHING)


class Course(Model):
    name = CharField(max_length=128)
    teacher = ForeignKey(User, on_delete=DO_NOTHING)
    group_id = ForeignKey(Group, on_delete=CASCADE)

    def __str__(self):
        return self.name


class Attachment(Model):
    file = FileField()
    file_path = FilePathField()


class Lesson(Model):
    name = CharField(max_length=128)
    description = CharField(max_length=512)
    course_id = ForeignKey(Course, on_delete=DO_NOTHING)
    content_type = TextField()
    author = ForeignKey(User, on_delete=DO_NOTHING)
    published = DateTimeField()
    datetime_start = DateTimeField()
    datetime_end = DateTimeField()
    attachment = ManyToManyField(Attachment, default=None)

    def __str__(self):
        return self.name


class Post(Model):
    user_id = ForeignKey(User, null=True, on_delete=SET_NULL)
    group_id = ForeignKey(Group, on_delete=DO_NOTHING)
    content = TextField()
    published = DateTimeField
    attachment = ManyToManyField(Attachment, default=None)



# class PostAttachment(Model):
#     attachment_id = ForeignKey(Attachment, on_delete=CASCADE)
#     post_id = ForeignKey(Post, default=None, on_delete=CASCADE)


# class LessonAttachment(Model):
#     attachment_id = ForeignKey(Attachment, on_delete=CASCADE)
#     lesson_id = ForeignKey(Lesson, default=None, on_delete=CASCADE)


class Grade(Model):
    value_int = IntegerField()
    grade_type = CharField(max_length=128)
    course_id = ForeignKey(Course, on_delete=DO_NOTHING)
    student_id = ForeignKey(User, on_delete=CASCADE, related_name='grade_student')
    teacher_id = ForeignKey(User, on_delete=DO_NOTHING, related_name='grade_teacher')
    date = DateTimeField()
    semester = BooleanField()


class Attendance(Model):
    present = BooleanField()
    date = DateTimeField()
    student_id = ForeignKey(User, on_delete=CASCADE, related_name='attendance_student')
    teacher_id = ForeignKey(User, null=True, on_delete=DO_NOTHING, related_name='attendance_teacher')
    lesson_id = ForeignKey(Lesson, null=True, on_delete=SET_NULL)