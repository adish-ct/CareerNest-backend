from django.contrib import admin
from .models import Jobs

# Register your models here.

class JobAdmin(admin.ModelAdmin):
    list_display = ['id', 'job_role']

admin.site.register(Jobs, JobAdmin)