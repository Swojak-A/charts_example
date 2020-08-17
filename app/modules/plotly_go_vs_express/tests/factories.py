import factory
from factory import fuzzy
from factory.faker import faker

from ..constants import EmployeeRoles
from ..models import Employee, YearRoundEmployerExpenses, current_year


# helpers
fake = faker.Faker()


def generate_employer_expenses_value() -> float:
    raw_val = fake.pydecimal(
        left_digits=6,
        right_digits=None,
        positive=True,
        min_value=20000,
        max_value=100000,
    )
    return raw_val // 10 * 10


# factories
class EmployeeFactory(factory.DjangoModelFactory):
    class Meta:
        model = Employee

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    position = factory.Faker("job")
    role = fuzzy.FuzzyChoice(EmployeeRoles.names())


class YearRoundEmployerExpensesFactory(factory.DjangoModelFactory):
    class Meta:
        model = YearRoundEmployerExpenses

    employee = factory.SubFactory(EmployeeFactory)
    year = factory.Faker("pyint", min_value=2000, max_value=current_year())
    value = factory.LazyFunction(generate_employer_expenses_value)
