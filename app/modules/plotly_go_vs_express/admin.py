from django.contrib import admin

from .charts import EmployerExpensesGoChart, EmployerExpensesExpressChart
from .models import Employee, YearRoundEmployerExpenses, YearRoundEmployerExpensesReport


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    fields = (
        "id",
        "created_at",
        "updated_at",
        "first_name",
        "last_name",
        "position",
        "role",
        "active",
    )
    readonly_fields = ("id", "created_at", "updated_at")
    list_display = ("id", "first_name", "last_name", "position", "role", "active")
    list_display_links = ("id", "first_name", "last_name")


@admin.register(YearRoundEmployerExpenses)
class YearRoundEmployerExpensesAdmin(admin.ModelAdmin):
    fields = ("id", "created_at", "updated_at", "employee", "year", "value")
    readonly_fields = ("id", "created_at", "updated_at")
    list_display = ("id", "employee", "year", "value")
    list_display_links = ("id",)


@admin.register(YearRoundEmployerExpensesReport)
class YearRoundEmployerExpensesReportAdmin(admin.ModelAdmin):

    change_list_template = (
        "admin/plotly_go_vs_express/employer_expenses_report_change_list.html"
    )

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)

        try:
            qs = response.context_data["cl"].queryset
        except (AttributeError, KeyError):
            return response

        employer_expenses_go_chart = EmployerExpensesGoChart(queryset=qs)
        response.context_data[
            "employer_expenses_go_chart"
        ] = employer_expenses_go_chart.to_html()
        employer_expenses_express_chart = EmployerExpensesExpressChart(queryset=qs)
        response.context_data[
            "employer_expenses_express_chart"
        ] = employer_expenses_express_chart.to_html()
        return response
