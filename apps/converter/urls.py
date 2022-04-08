from django.urls import path
from apps.converter.views import ImageToPDF

app_name = "converter"


urlpatterns = [
    path('img-to-pdf/', ImageToPDF.as_view(), name='img-to-pdf'),
]
