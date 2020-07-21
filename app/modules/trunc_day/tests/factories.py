from typing import TYPE_CHECKING
from datetime import timedelta

import factory
from factory.faker import faker
import pytz

from django.utils import timezone
from django.conf import settings

from ..models import PokeInstituteVisits

if TYPE_CHECKING:
    from datetime import datetime  # NOQA


# helpers
fake = faker.Faker()


def generate_entrance() -> "datetime":
    today = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
    yesterday = today - timedelta(days=1)
    entrance = fake.date_time_between(
        start_date=yesterday, end_date=today, tzinfo=pytz.timezone(settings.TIME_ZONE)
    )
    return entrance


# factories
class PokeInstituteVisitsFactory(factory.DjangoModelFactory):
    class Meta:
        model = PokeInstituteVisits

    entrance = factory.LazyFunction(generate_entrance)
