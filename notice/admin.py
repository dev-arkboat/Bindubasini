from django.contrib import admin
from .models import Notice, NoticeCategory


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'is_important', 'is_published', 'publish_date']
    list_filter = ['category', 'is_important', 'is_published']
    search_fields = ['title', 'content']
    list_editable = ['is_important', 'is_published']
    date_hierarchy = 'publish_date'
    list_per_page = 20


@admin.register(NoticeCategory)
class NoticeCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'order']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['order']
