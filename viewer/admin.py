from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Role, Group, Course, Lesson, Post, Attendance, Grade


admin.site.register(Role)
admin.site.register(Group)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Post)
admin.site.register(Attendance)
admin.site.register(Grade)


