from django.urls import path
from .views import (
    export_excel,
    import_excel
)

app_name = "excel"


urlpatterns = [
    path('export/', export_excel, name="export-excel"),
    path('import/', import_excel, name="import-excel"),
]
