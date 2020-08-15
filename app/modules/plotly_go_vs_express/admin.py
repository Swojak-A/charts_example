from django.contrib import admin

from .models import Employee, YearRoundEmployerExpenses


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
