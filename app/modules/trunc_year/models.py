from django.db import models
from django.utils.translation import ugettext_lazy as _

from modules.core.db import BaseModel


class Donation(BaseModel):
    value = models.DecimalField(
        verbose_name=_("Value"),
        null=False,
        blank=False,
        max_digits=15,
        decimal_places=2,
    )

    def __str__(self):
        return f"Donation: {self.value} from {self.created_at.isoformat()}"

    class Meta:
        verbose_name = _("Donation")
        verbose_name_plural = _("Donations")
        ordering = ("-created_at",)
