from django.contrib import admin

from .models import Profile, Project


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'title', 'email', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('full_name', 'title', 'email')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_featured', 'is_published', 'display_order', 'created_at')
    search_fields = ('title', 'short_description', 'tech_stack')
    list_filter = ('is_featured', 'is_published', 'created_at')
    ordering = ('-is_featured', 'display_order', '-created_at')
    prepopulated_fields = {'slug': ('title',)}

