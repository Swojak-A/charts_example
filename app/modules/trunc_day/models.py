from django.db import models
from django.utils.translation import ugettext_lazy as _

from modules.core.db import BaseModel


class PokeInstituteVisits(BaseModel):
    entrance = models.DateTimeField(verbose_name=_("Entrance"), blank=True, null=False)

    class Meta:
        ordering = ("-entrance",)
        verbose_name = _("PokeInstitute Visit")
        verbose_name_plural = _("PokeInstitute Visits")

    def __str__(self):
        return f"Visit at {self.entrance}"
