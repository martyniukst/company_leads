from rest_framework import serializers
from employee.serializers import EmployeeSerializer
from .models import Company
from employee.models import Employee

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    employees = serializers.PrimaryKeyRelatedField(many=True, queryset=Employee.objects.all())
    print (employees.__dict__)
    class Meta:
        model = Company
        fields = '__all__'

