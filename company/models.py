from django.db import models
# from employee.models import Employee

class Company(models.Model):
    name = models.CharField(max_length=20)
    company_url = models.URLField(max_length=60)
    location = models.CharField(max_length=60)
    revenue = models.CharField(max_length=20)
    # employees = models.ForeignKey(Employee, default=0, on_delete=models.SET_DEFAULT, related_name='company')

    def __str__(self):
        return self.name

