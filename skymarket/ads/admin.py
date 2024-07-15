from django.contrib import admin

from ads.models import Ad, Comment


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "price", "created_at", "author"]
    search_fields = ["title"]
    list_filter = ["title", "author"]
    ordering = ["title", "price"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["id", "text", "author", "ad", "created_at"]
    list_filter = ["author"]
    ordering = ["text", "ad"]
