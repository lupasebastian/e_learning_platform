from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.admin import ModelAdmin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile



# class CustomUserAdmin(UserAdmin):
#     pass
#
# class UserProfileAdmin(ModelAdmin):
#     pass

# admin.site.unregister(User)
# admin.site.unregister(Group)
admin.site.register(UserProfile)
# admin.site.register(UserProfileAdmin)
admin.site.site_header = 'E-SCHOOL DASHBOARD'
