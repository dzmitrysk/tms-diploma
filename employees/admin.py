from django.contrib import admin
from employees.models import Employee, EmployeeAdmin
from employees.models import Equipment, EquipmentAdmin


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Equipment, EquipmentAdmin)

