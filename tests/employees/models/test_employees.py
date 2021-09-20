import pytest

from employees.models import Employee


@pytest.mark.django_db
def test_it_creates_employee():
    Employee.objects.create(first_name='John',
                            last_name='Smith')
    assert Employee.objects.count() == 1

