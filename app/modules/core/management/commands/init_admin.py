import os

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        if "dev" not in os.environ.get("DJANGO_SETTINGS_MODULE"):
            raise CommandError("Only for development usage!")

        try:
            admin = User.objects.get(username="admin", is_superuser=True)
            admin.set_password("pass")
            admin.save()
            self.stdout.write(
                self.style.SUCCESS(f"Password reset for user {admin.username}")
            )
        except User.DoesNotExist:
            admin = User.objects.create_superuser(
                username="admin", email="admin@example.com", password="pass"
            )
            self.stdout.write(self.style.SUCCESS(f"User {admin.username} created."))
