from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from modules.core.db import BaseModel
from .constants import DonationTypes


class Donation(BaseModel):
    value = models.DecimalField(
        verbose_name=_("Value"),
        null=False,
        blank=False,
        max_digits=15,
        decimal_places=2,
    )
    type = models.CharField(
        verbose_name=_("Type"),
        max_length=256,
        choices=DonationTypes.name_choices(),
        default=DonationTypes.donation.name,
    )
    donation_date = models.DateField(
        verbose_name=_("Donation Date"), null=False, blank=False, default=timezone.now
    )

    def __str__(self):
        return f"{self.get_type_display()}: {self.value} from {self.donation_date}"

    class Meta:
        verbose_name = _("Donation")
        verbose_name_plural = _("Donations")
        ordering = ("-created_at",)
