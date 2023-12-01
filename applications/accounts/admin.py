from django.contrib import admin
from applications.accounts.models import User, Role, Profile

class UserAdminManager(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'is_active']


class RoleAdminManger(admin.ModelAdmin):
    list_display = ['id', 'role']

class ProfileAdminManger(admin.ModelAdmin):
    list_display = ['id', 'user', 'candidate_designation', '']

admin.site.register(User, UserAdminManager)
admin.site.register(Role, RoleAdminManger)
