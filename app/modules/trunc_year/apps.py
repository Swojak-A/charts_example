from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class TruncYearConfig(AppConfig):
    name = "modules.trunc_year"
    verbose_name: str = _("TruncYear")
