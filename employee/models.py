from django.db import models
from django.core.validators import validate_email
from company.models import Company


class Employee(models.Model):
    full_name = models.CharField(max_length=10)
    job_title = models.CharField(max_length=60)
    profile_url = models.URLField(max_length=60)
    location = models.CharField(max_length=60)
    email = models.EmailField(max_length=100, unique=True, validators=[validate_email])
    phone_number = models.CharField(max_length=20)
    company = models.ForeignKey(Company, default=0, on_delete=models.SET_DEFAULT, related_name='employees')

    def __str__(self):
        return self.full_name