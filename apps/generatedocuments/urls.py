from django.urls import path
from apps.generatedocuments.views import GenerateDocListViews, GenerateDocDetailViews

app_name = "documents"


urlpatterns = [
    path('list/', GenerateDocListViews.as_view(), name='doc-list'),
    path('detail/<int:pk>/', GenerateDocDetailViews.as_view(), name='doc-detail'),
]
