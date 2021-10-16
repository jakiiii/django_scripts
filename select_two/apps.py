from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SelectTwoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'select_two'
    verbose_name = _("Select2 Module")
