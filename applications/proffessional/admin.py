from django.contrib import admin
from .models import Experience, Education, Project


class ExperienceAdminManager(admin.ModelAdmin):
    list_display = ['id']

class EducationAdminManager(admin.ModelAdmin):
    list_display = ['id', 'stream', 'user']

class ProjectAdminManager(admin.ModelAdmin):
    list_display = ['id', 'user', 'project_name']

admin.site.register(Experience, ExperienceAdminManager)
admin.site.register(Education, EducationAdminManager)
admin.site.register(Project, ProjectAdminManager)