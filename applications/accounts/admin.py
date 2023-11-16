from django.contrib import admin
from applications.accounts.models import User, Role

class UserAdminManager(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'is_active']


class RoleAdminManger(admin.ModelAdmin):
    list_display = ['id', 'role']

admin.site.register(User, UserAdminManager)
admin.site.register(Role, RoleAdminManger)
