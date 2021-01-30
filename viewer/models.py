from django.utils.text import slugify
import datetime
from django.contrib.auth.models import User

from django.db.models import CharField, BooleanField, DateTimeField, DateField, FileField, FilePathField, \
    ForeignKey, IntegerField, TextField, Model, ManyToManyField, DO_NOTHING, CASCADE, SET_NULL, SlugField, TimeField


class Group(Model):
    symbol = CharField(max_length=16)
    date_created = DateTimeField(auto_now=True)
    year_start = CharField(max_length=32, default=datetime.datetime.now().year)
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
            return self.name
        else:
            return str('missing name')


class Lesson(Model):
    name = CharField(max_length=128, default='lesson title')
    description = CharField(max_length=512, blank=True, null=True, default='sneak peek')
    course_id = ForeignKey(Course, on_delete=DO_NOTHING)
    content_type = TextField(blank=True)
    author = ForeignKey(User, on_delete=DO_NOTHING)
    published = DateTimeField(auto_created=True, default=datetime.datetime.now())
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
    published = DateTimeField(default=datetime.datetime.now())
    course_id = ForeignKey(Course, blank=True, null=True, on_delete=DO_NOTHING)

    def __str__(self):
        return f'Post in {self.course_id}' if self.group_id is None else f'Post in {self.group_id}'


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


class Schedule(Model):
    WEEK = (
        ('monday', 'MONDAY'),
        ('tuesday', 'TUESDAY'),
        ('wednesday', 'WEDNESDAY'),
        ('thursday', 'THURSDAY'),
        ('friday', 'FRIDAY'),
    )
    TIMES = [
        (datetime.time(hour=8, minute=0), '08:00'),
        (datetime.time(hour=9, minute=0), '09:00'),
        (datetime.time(hour=10, minute=0), '10:00'),
        (datetime.time(hour=11, minute=0), '11:00'),
        (datetime.time(hour=12, minute=0), '12:00'),
        (datetime.time(hour=13, minute=0), '13:00'),
        (datetime.time(hour=14, minute=0), '14:00'),
        (datetime.time(hour=15, minute=0), '15:00'),
    ]
    course_id = ForeignKey(Course, on_delete=CASCADE)
    day_of_week = CharField(max_length=20, choices=WEEK, default='monday')
    start_time = TimeField(blank=False, choices=TIMES)
    end_time = TimeField(blank=True)

    def __str__(self):
        return f'{self.course_id.name} {self.course_id.teacher.first_name} {self.course_id.teacher.last_name} {self.course_id.group_id.symbol}'
