from django.utils.text import slugify
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models import CharField, BooleanField, DateTimeField, DateField, FileField, FilePathField, \
    ForeignKey, IntegerField, TextField, Model, ManyToManyField, DO_NOTHING, CASCADE, SET_NULL, SlugField

from accounts.models import UserProfile


# class Role(Model):
#     name = CharField(max_length=128)
#
#     def __str__(self):
#         return self.name


class Group(Model):
    symbol = CharField(max_length=16)
    date_created = DateTimeField(auto_now=True)
    year_start = CharField(max_length=32, default=datetime.now().year)
    year_end = CharField(null=True, blank=True, default=None, max_length=32)
    supervisor = ForeignKey(User, null=True, blank=True, on_delete=DO_NOTHING)
    slug = SlugField(null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.symbol)
        super(Group, self).save(*args, **kwargs)

    def __str__(self):
        return self.symbol


class Course(Model):
    name = CharField(max_length=128)
    teacher = ForeignKey(User, blank=True, on_delete=DO_NOTHING)
    group_id = ForeignKey(Group, on_delete=CASCADE)
    slug = SlugField(null=True, unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Attachment(Model):
    file = FileField()
    file_path = FilePathField()


class Lesson(Model):
    name = CharField(max_length=128)
    description = CharField(max_length=512, blank=True, null=True)
    course_id = ForeignKey(Course, on_delete=DO_NOTHING)
    content_type = TextField(blank=True)
    author = ForeignKey(User, on_delete=DO_NOTHING)
    published = DateTimeField(auto_created=True)
    datetime_start = DateTimeField(blank=True)
    datetime_end = DateTimeField(blank=True)
    attachment = ManyToManyField(Attachment, blank=True, default=None)
    slug = SlugField(null=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Lesson, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Post(Model):
    user_id = ForeignKey(User, null=True, on_delete=SET_NULL)
    group_id = ForeignKey(Group, blank=True, null=True, on_delete=DO_NOTHING)
    content = TextField(blank=True)
    published = DateTimeField(default=datetime.now())
    attachment = ManyToManyField(Attachment, blank=True, default=None)
    course_id = ForeignKey(Course, blank=True, null=True, on_delete=DO_NOTHING)


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