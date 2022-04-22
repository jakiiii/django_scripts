from fpdf import FPDF
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

from apps.converter.forms import ImagesToPDF


class ImageToPDF(TemplateView):
    template_name = 'converter/image-to-pdf.html'


def img_to_pdf(request):
    template_name = 'converter/image-to-pdf.html'
    image_list = []
    _datetime = datetime.now()
    datetime_str = _datetime.strftime("%Y-%m-%d-%H-%M-%S")
    pdf = FPDF('P', 'mm', 'A4')

    for img in request.FILES.getlist('images'):
        print(img)
        # pdf.add_page()
        # pdf.image(img, x=None, y=None, w=190.0, h=0)

    # pdf_path = f"/home/jaki/Dev/django_scripts/apps/converter/scripts/{datetime_str}.pdf"
    # pdf.output(pdf_path, "F")
    return render(request, template_name, {})
