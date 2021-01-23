from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile

admin.site.unregister(User)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass

admin.site.register(UserProfile)
