from django.shortcuts import render
from django.conf import settings
from django.views.generic import TemplateView, ListView

from apps.home.models import MenuCategory, Menu


class HomeView(ListView):
    model = MenuCategory
    template_name = 'home/home.html'
    context_object_name = 'menu_context'
