from django.contrib import admin
from generatedocuments.models import GenerateDocuments


@admin.register(GenerateDocuments)
class GenerateDocumentsAdmin(admin.ModelAdmin):
    list_display = ['product', 'customer', 'price', 'quantity']
