from django.contrib import admin
from .models import Experience, Education


class ExperienceAdminManager(admin.ModelAdmin):
    list_display = ['id']


class EducationAdminManager(admin.ModelAdmin):
    list_display = ['id', 'stream', 'user']

admin.site.register(Experience, ExperienceAdminManager)
admin.site.register(Education, EducationAdminManager)