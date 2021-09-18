from django.db import models
from django.contrib import admin


class Employee(models.Model):
    avatar = models.ImageField(blank=True)
    first_name = models.CharField(max_length=20, verbose_name='First name')
    last_name = models.CharField(max_length=20, verbose_name='Last name')
    department = models.CharField(max_length=30, verbose_name='Department', blank=True)
    position = models.CharField(max_length=50, verbose_name='Position', blank=True)

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'avatar', 'last_name', 'first_name', 'position', 'department']
    list_display_links = ['id', 'avatar', 'last_name', 'first_name']
    search_fields = ['id', 'last_name', 'first_name']


class Equipment(models.Model):
    photo = models.ImageField(blank=True)
    name = models.CharField(max_length=30)
    item_number = models.CharField(max_length=5, unique=True)
    price = models.FloatField(default=0.0)
    configuration = models.URLField(blank=True)
    in_use_by = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, related_name='equipped', default=0)
    paid_by = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, related_name='paid', default=1)
    comment = models.TextField(blank=True)
    employee_start_date = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['item_number']

    def __str__(self):
        return f'{self.item_number} - {self.name}'


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo', 'item_number', 'name', 'in_use_by', 'paid_by',
                    'price', 'comment', 'employee_start_date', 'configuration']
    list_display_links = ['id', 'photo', 'item_number', 'name', 'in_use_by', 'paid_by',
                          'price', 'comment', 'employee_start_date']
    search_fields = ['id', 'item_number', 'name']

