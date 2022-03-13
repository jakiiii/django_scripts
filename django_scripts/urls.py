"""django_scripts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('sel/', include('select_two.urls', namespace='sel')),
    path('task/', include('celery_task.urls', namespace='task')),
    path('excel/', include('excelhandling.urls', namespace='excel')),
    path('filter/', include('dfilters.urls', namespace='dfilter')),
    path('geodj/', include('geodj.urls', namespace='geodj')),
    path('apifilter/', include('apifilter.urls', namespace='apifilter')),

    path('api/filter/', include('dfilters.api.urls', namespace='api_dfilter')),
    path('api/images/', include('multiple_image.api.urls', namespace='images')),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
