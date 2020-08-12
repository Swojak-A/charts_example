from enum import unique

from django.utils.translation import ugettext_lazy as _

from modules.core.constants import ChoicesFactory


@unique
class EmployeeRoles(ChoicesFactory):
    board = _("Board")
    researcher = _("Researcher")
    maintenance = _("Maintenance")
    guide = _("Guide")
