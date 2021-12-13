from django.urls import path
from dfilters.views import (
    filter_view
)

app_name = "dfilter"


urlpatterns = [
    path('', filter_view, name='filter')
]

