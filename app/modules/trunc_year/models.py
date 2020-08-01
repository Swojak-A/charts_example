from django.db import models
from django.utils.translation import ugettext_lazy as _

from modules.core.db import BaseModel
from .constants import DonationType


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
        choices=DonationType.name_choices(),
        default=DonationType.donation.name,
    )

    def __str__(self):
        return f"Donation: {self.value} from {self.created_at.isoformat()}"

    class Meta:
        verbose_name = _("Donation")
        verbose_name_plural = _("Donations")
        ordering = ("-created_at",)
