from django.contrib import admin
from .models import UserInformation, ExcelFile


@admin.register(UserInformation)
class UserInformationAdmin(admin.ModelAdmin):
    list_display = ['a_party', 'b_party', 'imei']
    search_fields = ['a_party', 'b_party', 'imei']
    list_filter = ['a_party', 'b_party', 'imei']


@admin.register(ExcelFile)
class ExcelFileAdmin(admin.ModelAdmin):
    list_display = ['id', 'file']
