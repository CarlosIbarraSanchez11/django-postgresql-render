from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Vet(models.Model):
    SEXO_CHOICES = [
        ('M', 'Macho'),
        ('F', 'Hembra'),
    ]

    name = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    discharge_date = models.DateField(null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Add phone_number field
    edad = models.TextField(blank=True, null=True)  # Add edad field
    peso = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)  # Add peso field
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=True, null=True)  # Add sexo field with choices
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name