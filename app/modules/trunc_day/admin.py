from django.contrib import admin

from .models import PokeInstituteVisits


@admin.register(PokeInstituteVisits)
class PokeInstituteVisitsAdmin(admin.ModelAdmin):
    fields = ("uuid", "entrance")
    readonly_fields = ("uuid", "entrance")
