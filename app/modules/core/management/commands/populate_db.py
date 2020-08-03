from typing import Optional

from django.core.management.base import BaseCommand

from modules.core.management.commands_helpers import create_donations


class Command(BaseCommand):
    help = "populate database for testing purposes using mock data"

    def add_arguments(self, parser):
        parser.add_argument("--days-backwards", type=int, help="No of Days Backwards")

    def handle(self, *args, **options):
        self.stdout.write("Starting to populate database using mock data...")
        populate(self, days_backwards=options.get("days_backwards"))
        self.stdout.write("Database populated.")


def populate(self, days_backwards: Optional[int] = None):
    if not days_backwards:
        days_backwards = 30

    print(f"Populating database {days_backwards} days backwards")

    create_donations()
