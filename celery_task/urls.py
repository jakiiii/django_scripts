from django.urls import path
from .views import ReviewEmailView

app_name = "task"


urlpatterns = [
    path('send-review/', ReviewEmailView.as_view(), name='send-review-email'),
]
