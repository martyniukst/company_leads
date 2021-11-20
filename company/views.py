from rest_framework import viewsets
from .serializers import CompanySerializer
from .models import Company
from employee.models import Employee
from django.db.models import Count


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all().annotate()
    serializer_class = CompanySerializer


