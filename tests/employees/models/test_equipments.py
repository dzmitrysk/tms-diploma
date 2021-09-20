import pytest

from employees.models import Equipment, Employee


@pytest.mark.django_db
def test_it_creates_equipment():
    Employee.objects.create(first_name='John',
                            last_name='Smith')

    Equipment.objects.create(name='Equipment1',
                             item_number='0100',
                             in_use_by_id=Employee.objects.first().id,
                             paid_by_id=Employee.objects.first().id)
    assert Equipment.objects.count() == 1
