from datetime import date

import factory
from factory import fuzzy
from factory.faker import faker

from ..models import Donation
from ..constants import DonationTypes


# helpers
fake = faker.Faker()

this_year = date.today().year
date_start = date(this_year, 1, 1)
date_end = date.today()


def generate_donation_value() -> float:
    raw_val = fake.pydecimal(
        left_digits=6,
        right_digits=None,
        positive=True,
        min_value=1000,
        max_value=10000000,
    )
    return raw_val // 1000 * 1000


# factories
class DonationFactory(factory.DjangoModelFactory):
    class Meta:
        model = Donation

    value = factory.LazyFunction(generate_donation_value)
    type = fuzzy.FuzzyChoice(DonationTypes.names())
    donation_date = factory.Faker(
        "date_between_dates", date_start=date_start, date_end=date_end
    )
