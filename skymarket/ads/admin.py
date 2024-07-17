from django.contrib import admin

from ads.models import Ad, Comment


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    """Отображение информации об объявлениях в админ панели"""

    list_display = ["id", "title", "description", "price", "created_at", "author"]
    search_fields = ["title"]
    list_filter = ["title", "author"]
    ordering = ["title", "price", "created_at"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Отображение информации об отзывах в админ панели"""

    list_display = ["id", "text", "ad", "created_at", "author"]
    list_filter = ["author", "ad"]
    ordering = ["text", "ad", "created_at"]
