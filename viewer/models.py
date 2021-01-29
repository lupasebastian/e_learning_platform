from django.utils.text import slugify
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models import CharField, BooleanField, DateTimeField, FileField, ImageField, \
    ForeignKey, IntegerField, TextField, Model, DO_NOTHING, CASCADE, SET_NULL, SlugField


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
    name = CharField(max_length=128, null=True, blank=True)
    teacher = ForeignKey(User, blank=True, on_delete=DO_NOTHING, null=True)
    group_id = ForeignKey(Group, on_delete=CASCADE, blank=True, null=True)
    slug = SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = f'{slugify(self.name)}_{self.group_id}'.lower()
        super(Course, self).save(*args, **kwargs)

    def __str__(self):
        if self.name:
            return self.name + ' ' + str(self.group_id)
        else:
            return str('missing name')


class Lesson(Model):
    name = CharField(max_length=128, default='lesson title')
    description = CharField(max_length=512, blank=True, null=True, default='sneak peek')
    course_id = ForeignKey(Course, on_delete=DO_NOTHING)
    content_type = TextField(blank=True)
    author = ForeignKey(User, on_delete=DO_NOTHING)
    published = DateTimeField(auto_created=True, default=datetime.now())
    datetime_start = DateTimeField(blank=True)
    datetime_end = DateTimeField(blank=True)
    slug = SlugField(null=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = f'{self.course_id}_{slugify(self.name)}'
        super(Lesson, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class AttachmentLesson(Model):
    file = FileField(upload_to='lessons/', null=True)
    # image = ImageField(upload_to='images/', null=True)
    lesson_id = ForeignKey(Lesson, on_delete=DO_NOTHING, default=None)


class Post(Model):
    user_id = ForeignKey(User, null=True, on_delete=SET_NULL)
    group_id = ForeignKey(Group, blank=True, null=True, on_delete=DO_NOTHING)
    content = TextField(blank=True)
    published = DateTimeField(default=datetime.now())
    course_id = ForeignKey(Course, blank=True, null=True, on_delete=DO_NOTHING)


class AttachmentPost(Model):
    file = FileField(upload_to='posts/', null=True)
    # image = ImageField(upload_to='images/', null=True)
    post_id = ForeignKey(Post, on_delete=DO_NOTHING, default=None)


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