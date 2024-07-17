from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Отображение информации о пользователях в админ панели"""

    list_display = ["id", "email", "first_name", "last_name", "phone", "role", "is_active", "last_login"]
    search_fields = ["email", "first_name", "last_name", "last_login"]
    list_filter = ["role", "is_active"]
    ordering = ["email"]
