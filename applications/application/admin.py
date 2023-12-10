from django.contrib import admin
from .models import Application

class ApplicationAdminManager(admin.ModelAdmin):
    list_display = ['id', 'user', 'job']

admin.site.register(Application, ApplicationAdminManager) 