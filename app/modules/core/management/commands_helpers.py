from datetime import date

from factory.faker import faker

from django.utils import timezone

from modules.plotly_go_vs_express.models import Employee, YearRoundEmployerExpenses
from modules.plotly_go_vs_express.tests.factories import (
    EmployeeFactory,
    YearRoundEmployerExpensesFactory,
)
from modules.trunc_year.models import Donation
from modules.trunc_year.tests.factories import DonationFactory


# helpers
fake = faker.Faker()


def draw_probability(chance: int):
    r = fake.pyint(max_value=99)
    return r < chance


# create functions
def create_employer_expenses(no_of_years: int) -> None:
    Employee.objects.all().delete()
    YearRoundEmployerExpenses.objects.all().delete()

    this_year = timezone.now().year
    y = this_year - no_of_years

    initial_no_of_employees = fake.pyint(min_value=1, max_value=3)
    for n in range(initial_no_of_employees):
        EmployeeFactory()

    while y <= this_year:
        no_of_new_employees = fake.pyint(min_value=1, max_value=3)
        for n in range(no_of_new_employees):
            EmployeeFactory()
        employees = Employee.objects.filter(active=True)
        for employee in employees:
            if (
                previous_expenses := YearRoundEmployerExpenses.objects.filter(
                    employee=employee
                ).first()
            ) :
                YearRoundEmployerExpensesFactory(
                    employee=employee, year=y, value=previous_expenses.value
                )
            else:
                YearRoundEmployerExpensesFactory(employee=employee, year=y)
            if draw_probability(chance=15):
                employee.active = False
                employee.save()

        print(f"Created {employees.count()} YearRoundEmployerExpenses for year: {y}")
        y = y + 1


def create_donations(no_of_years: int) -> None:
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
