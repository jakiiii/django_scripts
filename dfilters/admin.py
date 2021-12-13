from django.contrib import admin
from dfilters.models import (
    Author, Category, Journal
)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publish_date', 'views', 'reviewed']
