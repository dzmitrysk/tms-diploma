from rest_framework.serializers import ModelSerializer
from employees.models import Employee, Equipment


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields =('id',
                 'avatar',
                 'last_name',
                 'first_name',
                 'position',
                 'department'
                 )


class EquipmentSerializer(ModelSerializer):
    class Meta:
        model = Equipment
        fields = ('id',
                  'photo',
                  'item_number',
                  'name',
                  'in_use_by',
                  'paid_by',
                  'price',
                  'comment',
                  'employee_start_date',
                  'configuration'
                  )