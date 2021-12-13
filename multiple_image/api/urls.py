from django.urls import path
from .views import TaskImageUpload

app_name = "images"


urlpatterns = [
    path('', TaskImageUpload.as_view(), name="task-images")
]
