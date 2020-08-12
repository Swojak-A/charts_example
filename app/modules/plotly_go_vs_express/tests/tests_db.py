from django.test import TestCase

from ..models import YearRoundEmployerExpenses


class YearRoundEmployerExpensesDBTests(TestCase):
    def test_year_round_employer_expenses_created_successfully(self):
        YearRoundEmployerExpenses.objects.create()

        qs = YearRoundEmployerExpenses.objects.exists()
        self.assertTrue(qs)
