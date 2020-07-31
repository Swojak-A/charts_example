from django.contrib import admin

from .models import Donation


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    fields = (
        "id",
        "value",
    )
    readonly_fields = ("id",)
    list_display = ("id", "value")
