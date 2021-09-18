"""tms_diploma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from employees.views import APIEmployees, APIEquipments, APIEmployeeDetail, APIEquipmentDetail
from employees.views import api_give_equipment, api_not_found
from tms_diploma.views import index

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('api/give/<int:equipment_id>', api_give_equipment),
    path('api/employees', APIEmployees.as_view()),
    path('api/employees/<int:pk>', APIEmployeeDetail.as_view()),
    path('api/equipments', APIEquipments.as_view()),
    path('api/equipments/<int:pk>', APIEquipmentDetail.as_view()),
    re_path(r'^api', api_not_found),
]
