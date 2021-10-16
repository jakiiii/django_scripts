from django.contrib import admin
from .models import Language, Entry, EntryName


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ['name', 'language']


@admin.register(EntryName)
class EntryNameAdmin(admin.ModelAdmin):
    list_display = ['name']
