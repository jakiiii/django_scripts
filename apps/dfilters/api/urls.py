from django.urls import path
from apps.dfilters.api.views import ApiFilterView


app_name = "api_dfilter"


urlpatterns = [
    path('', ApiFilterView.as_view(), name='api-filter')
]
