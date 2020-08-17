from django.contrib import admin

from .models import Donation, DonationReport
from .charts import DonationCountChart, DonationTypeComparisonChart


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    fields = (
        "id",
        "value",
    )
    readonly_fields = ("id",)
    list_display = ("id", "value")


@admin.register(DonationReport)
class DonationReportAdmin(admin.ModelAdmin):

    change_list_template = "admin/trunc_year/donation_report_change_list.html"

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)

        try:
            qs = response.context_data["cl"].queryset
        except (AttributeError, KeyError):
            return response

        donation_count_chart = DonationCountChart(queryset=qs)
        response.context_data["donation_count_chart"] = donation_count_chart.to_html()
        donation_type_chart = DonationTypeComparisonChart(queryset=qs)
        response.context_data["donation_type_hart"] = donation_type_chart.to_html()
        return response
