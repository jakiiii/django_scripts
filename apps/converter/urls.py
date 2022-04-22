from django.urls import path
from apps.converter.views import ImageToPDF, img_to_pdf

app_name = "converter"


urlpatterns = [
    # path('img-to-pdf/', ImageToPDF.as_view(), name='img-to-pdf'),
    path('img-to-pdf/', img_to_pdf, name='img-to-pdf'),
]
