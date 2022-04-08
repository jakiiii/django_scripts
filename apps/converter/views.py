from django.shortcuts import render
from django.views.generic import TemplateView


class ImageToPDF(TemplateView):
    template_name = 'converter/image-to-pdf.html'
