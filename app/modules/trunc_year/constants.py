from enum import unique

from django.utils.translation import ugettext_lazy as _

from modules.core.constants import ChoicesFactory


@unique
class DonationTypes(ChoicesFactory):
    donation = _("Donation")
    grant = _("Grant")
