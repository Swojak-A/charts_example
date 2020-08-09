from datetime import date

from factory.faker import faker

from django.utils import timezone

from modules.trunc_year.models import Donation
from modules.trunc_year.tests.factories import DonationFactory


# helpers
fake = faker.Faker()

# create functions
def create_donations(no_of_years) -> None:
    Donation.objects.all().delete()

    this_year = timezone.now().year
    y = this_year - no_of_years

    while y <= this_year:
        no_of_donations = fake.pyint(min_value=3, max_value=20)
        for i in range(no_of_donations):
            date_start = date(y, 1, 1)
            if y == this_year:
                date_end = date.today()
            else:
                date_end = date(y, 12, 31)
            DonationFactory(
                donation_date=fake.date_between_dates(
                    date_start=date_start, date_end=date_end
                )
            )

        print(f"Created {no_of_donations} Donation for year: {y}")
        y = y + 1
