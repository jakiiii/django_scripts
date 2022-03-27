from django.contrib import admin

from apps.authotp.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_verified', 'is_staff']
