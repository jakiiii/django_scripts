from django.contrib import admin
from apps.generatedocuments.models import GenerateDocuments


@admin.register(GenerateDocuments)
class GenerateDocumentsAdmin(admin.ModelAdmin):
    list_display = ['product', 'customer', 'price', 'quantity']
