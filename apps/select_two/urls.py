from django.urls import path
from .views import (
    select_searching,
    select_multiple,
    array_country_name
)

app_name = "sel"


urlpatterns = [
    path('', select_searching, name='select-search'),
    path('multiple/', select_multiple, name='select-multiple'),
    path('country/', array_country_name, name='country-multiple'),
]
