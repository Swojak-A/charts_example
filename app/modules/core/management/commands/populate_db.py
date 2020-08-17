from typing import Optional

from django.core.management.base import BaseCommand

from modules.core.management.commands_helpers import (
    create_employer_expenses,
    create_donations,
)


class Command(BaseCommand):
    help = "populate database for testing purposes using mock data"

    def add_arguments(self, parser):
        parser.add_argument("--days-backwards", type=int, help="No of Days Backwards")
        parser.add_argument(
            "--years-backwards", type=int, help="No of Years Backwards for specific"
        )

    def handle(self, *args, **options):
        self.stdout.write("Starting to populate database using mock data...")
        populate(
            self,
            days_backwards=options.get("days_backwards"),
            years_backwards=options.get("years_backwards"),
        )
        self.stdout.write("Database populated.")


def populate(
    self, days_backwards: Optional[int] = None, years_backwards: Optional[int] = None
):
    if not days_backwards:
        days_backwards = 30
    if not years_backwards:
        years_backwards = 10

    print(
        f"Populating database {days_backwards} days / {years_backwards} years backwards"
    )

    create_employer_expenses(no_of_years=years_backwards)
    create_donations(no_of_years=years_backwards)
