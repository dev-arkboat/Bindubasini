from django.contrib import admin
from .models import Teacher, Headmaster, Alumni, AboutInfo, SchoolInfo, ContactMessage, Subject, Facility, SchoolBuilding, Achievement


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'designation', 'subject', 'is_active', 'order']
    list_filter = ['is_active', 'subject']
    search_fields = ['name', 'designation', 'subject']
    list_editable = ['order', 'is_active']
    list_per_page = 20


@admin.register(Headmaster)
class HeadmasterAdmin(admin.ModelAdmin):
    list_display = ['name', 'qualification', 'took_office', 'left_office', 'is_current']
    list_filter = ['is_current']
    search_fields = ['name']
    list_editable = ['is_current']


@admin.register(Alumni)
class AlumniAdmin(admin.ModelAdmin):
    list_display = ['name', 'class_year', 'notability']
    search_fields = ['name']
    list_per_page = 20


@admin.register(AboutInfo)
class AboutInfoAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_published']
    list_editable = ['order', 'is_published']
    search_fields = ['title']


@admin.register(SchoolInfo)
class SchoolInfoAdmin(admin.ModelAdmin):
    list_display = ['name_en', 'established_year', 'phone', 'email']
    list_per_page = 20


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'email', 'is_read', 'created_at']
    list_filter = ['is_read']
    search_fields = ['name', 'subject', 'email', 'message']
    readonly_fields = ['name', 'email', 'phone', 'subject', 'message', 'created_at']
    list_editable = ['is_read']
    actions = ['mark_as_read', 'mark_as_unread']

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Mark selected as read"

    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)
    mark_as_unread.short_description = "Mark selected as unread"


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'order']
    list_editable = ['order']
    search_fields = ['name']


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    list_editable = ['order']


@admin.register(SchoolBuilding)
class SchoolBuildingAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    list_editable = ['order']


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'order']
    list_editable = ['order']
    search_fields = ['title']
