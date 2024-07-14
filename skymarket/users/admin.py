from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "email", "first_name", "last_name", "phone", "role", "is_active", "last_login"]
    ordering = ["email"]
