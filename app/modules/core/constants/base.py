from enum import Enum
from typing import List, Tuple

from django.utils.translation import ugettext_lazy as _

ECOMMERCE_SERVICE_MODE = "PICKING_DRIVE"

NO_INFO: str = _("Lack of information")
BLANK: Tuple[str, str] = ("", NO_INFO)


class ChoicesFactory(Enum):
    @classmethod
    def name_choices(cls) -> List[Tuple[str, str]]:
        choices = [(str(item.name).lower(), str(item.value)) for item in cls]
        choices.append(BLANK)
        return sorted(choices, key=lambda x: x[0])

    @classmethod
    def values(cls) -> List[str]:
        return [str(item.value).lower() for item in cls]

    @classmethod
    def names(cls) -> List[str]:
        return [str(item.name).lower() for item in cls]
