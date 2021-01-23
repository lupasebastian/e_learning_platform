from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Test, TestTeacherAnswer, TestStudentAnswer, QuestionType, TestQuestion

admin.site.register(TestStudentAnswer)
admin.site.register(TestTeacherAnswer)
admin.site.register(Test)
admin.site.register(QuestionType)
admin.site.register(TestQuestion)
