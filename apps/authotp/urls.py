from django.urls import path
from apps.authotp.views import RegisterAPI, VerifyOTP

app_name = "auth"


urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('verify/', VerifyOTP.as_view(), name='verify-otp'),
]
