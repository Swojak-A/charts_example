from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from modules.core.db import BaseModel
from .constants import EmployeeRoles


# helpers
def current_year():
    return timezone.now().year


# models
class Employee(BaseModel):
    first_name = models.CharField(
        verbose_name=_("First Name"),
        max_length=256,
        null=False,
        blank=False,
        default="",
    )
    last_name = models.CharField(
        verbose_name=_("Last Name"),
        max_length=256,
        null=False,
        blank=False,
        default="",
    )
    position = models.CharField(
        verbose_name=_("Position"), max_length=256, null=False, blank=False, default="",
    )
    role = models.CharField(
        verbose_name=_("Type"),
        max_length=256,
        choices=EmployeeRoles.name_choices(),
        default="",
    )

    def __str__(self):
        return f"{self.position} ({self.role}): {self.first_name} {self.last_name}"

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _("Employee")
        verbose_name_plural = _("Employees")
