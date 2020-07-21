from datetime import timedelta

from factory.faker import faker

from django.utils import timezone

from modules.trunc_day.models import PokeInstituteVisits
from modules.trunc_day.tests.factories import PokeInstituteVisitsFactory


fake = faker.Faker()


def create_poke_institute_visits(days_backwards: int) -> None:
    PokeInstituteVisits.objects.all().delete()

    today = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
    t = today - timedelta(days=days_backwards)

    while t < today:
        if t.weekday() in list(range(4)):
            for i in range(fake.pyint(min_value=5, max_value=50)):
                PokeInstituteVisitsFactory(
                    entrance=t
                    + timedelta(minutes=fake.pyint(min_value=480, max_value=1200))
                )
        else:
            for i in range(fake.pyint(min_value=5, max_value=100)):
                PokeInstituteVisitsFactory(
                    entrance=t
                    + timedelta(minutes=fake.pyint(min_value=480, max_value=1200))
                )

        print(f"Created PokeInstituteVisits for day: {t}")
        t = t + timedelta(days=1)
