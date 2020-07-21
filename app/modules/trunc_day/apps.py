from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class TruncDayConfig(AppConfig):
    name = "modules.trunc_day"
    verbose_name: str = _("TruncDay")
