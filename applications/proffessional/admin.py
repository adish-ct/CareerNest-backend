from django.contrib import admin
from .models import Experience


class ExperienceAdminManager(admin.ModelAdmin):
    list_display = ['id']


admin.site.register(Experience, ExperienceAdminManager)