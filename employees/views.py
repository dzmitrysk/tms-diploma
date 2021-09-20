from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from employees.models import Employee, Equipment
from employees.serializers import EmployeeSerializer, EquipmentSerializer


class APIEmployees(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class APIEmployeeDetail(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class APIEquipments(ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


class APIEquipmentDetail(RetrieveUpdateDestroyAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


@api_view(['POST'])
def api_give_equipment(request, equipment_id):
    employee_id = request.POST.get('employee')

    try:
        employee = Employee.objects.get(id=employee_id)
    except Employee.DoesNotExist:
        return Response('Unknown employee',
                        content_type='text/html',
                        status=status.HTTP_400_BAD_REQUEST)

    try:
        equipment = Equipment.objects.get(id=equipment_id)
    except Equipment.DoesNotExist:
        return Response('Unknown equipment',
                        content_type='text/html',
                        status=status.HTTP_400_BAD_REQUEST)

    equipment.in_use_by = employee
    equipment.save()

    serializer = EquipmentSerializer(equipment)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def api_not_found(request):
    return Response('Unknown API request',
                    content_type='text/html',
                    status=status.HTTP_400_BAD_REQUEST)
