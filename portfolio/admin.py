from django.contrib import admin
from .models import Project, Skill, Certification, Achievement, Contact


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'github_link')
    search_fields = ('title',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')
    list_editable = ('level',)
    search_fields = ('name',)


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'issuing_organization')
    search_fields = ('name', 'issuing_organization')


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    readonly_fields = ('created_at',)
    search_fields = ('name', 'email')
