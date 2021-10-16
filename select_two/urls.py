from django.urls import path
from .views import (
    select_searching,
    select_multiple
)

app_name = "sel"


urlpatterns = [
    path('', select_searching, name='select-search'),
    path('multiple/', select_multiple, name='select-multiple')
]
