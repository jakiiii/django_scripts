from django.urls import path
from apifilter.views import CustomUserFilterAV

app_name = "apifilter"


urlpatterns = [
    path('users/', CustomUserFilterAV.as_view(), name='users-filter-api'),
]
