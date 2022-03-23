from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from generatedocuments.models import GenerateDocuments


class GenerateDocListViews(ListView):
    template_name = 'generatedocuments/list.html'
    model = GenerateDocuments
    context_object_name = 'generate_documents'


class GenerateDocDetailViews(DetailView):
    template_name = 'generatedocuments/detail.html'
    model = GenerateDocuments
    context_object_name = 'documents'
