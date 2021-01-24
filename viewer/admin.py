from django.contrib import admin
from django.contrib.auth.models import User
from .models import Group, Course, Lesson, Post, Attendance, Grade


admin.site.register(Group)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Post)
admin.site.register(Attendance)
admin.site.register(Grade)

# Próbuje tu zrobić coś co sprawi, że przy tworzeniu studentgrupy w polu supervisor nie będą pojawiali się
# studenci do wyboru, czyli ograniczyć wybór do teachera i supervisora.
# Na razie skopiowalem z neta coś co wygląda obiecująco :D

class GroupAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "supervisor":
            kwargs["queryset"] = User.objects.filter(myparent=request.object_id)
        return super(GroupAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)