from employees.models import Employee
from employees.models import Equipment
from faker import Faker
from random import randint, choice


DEPARTMENTS = ['01 - Python dep.',
               '02 - Java dep.',
               '03 - QA dep.']

POSITIONS = [['Junior Python developer', 'Middle Python developer', 'Senior Python developer'],
             ['Junior Java developer', 'Middle Java developer', 'Senior Java developer'],
             ['Junior QA engineer', 'Middle QA engineer', 'Senior QA engineer']]

EQUIPMENTS = ['HP Envy',
              'Acer Aspire',
              'MacBook PRO',
              'KOSS BT540i headphones',
              'iPhone 13',
              'Dell Inspiron',
              'MacBook Air',
              'Asus VivoBook 15',
              'Lenovo IdeaPad',
              'HONOR MagicBook X15',
              'Dell XPS 15',
              'Logitech G Pro mouse',
              'Keychron K2 wireless',
              'JBL T660 headphones']

void_employee = Employee.objects.create(first_name='-',
                                        last_name='-',
                                        position='-',
                                        department='-')
if void_employee:
    print(f"Employee '{void_employee}' created")
else:
    print("NOT CREATED 'void employee'")


firm_owner = Employee.objects.create(first_name=' ',
                                     last_name='Firm',
                                     position='-',
                                     department='-')
if firm_owner:
    print(f"Employee '{firm_owner}' created")
else:
    print("NOT CREATED 'firm owner'")


fake = Faker()
for i in range(10):
    first_name, last_name = fake.first_name(), fake.last_name()
    department = randint(0, 2)
    position = choice(POSITIONS[department])

    new_employee = Employee.objects.create(first_name=first_name,
                                           last_name=last_name,
                                           position=position,
                                           department=DEPARTMENTS[department])
    if new_employee.last_name:
        print(f"Employee '{new_employee}' created")
    else:
        print("NOT CREATED random employee")


for number, equipment in enumerate(EQUIPMENTS):
    new_equipment = Equipment.objects.create(name=equipment,
                                             item_number=f'{number + 1: 05d}',
                                             in_use_by_id=1,
                                             paid_by_id=2)
    if new_equipment:
        print(f"Equipment '{new_equipment}' created")
    else:
        print(f"NOT CREATED {new_equipment}")
