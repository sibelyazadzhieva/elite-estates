from django.db import models
from django.contrib.auth import get_user_model
from properties.models import Property

UserModel = get_user_model()


class Service(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Contract(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='contracts')
    tenant = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='leases')
    start_date = models.DateField()
    end_date = models.DateField()
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    included_services = models.ManyToManyField(Service, related_name='contracts', blank=True)

    def __str__(self):
        return f"Contract: {self.property.title} - {self.tenant.username}"


class Ticket(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]

    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='tickets')
    title = models.CharField(max_length=150)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ticket: {self.title} ({self.get_status_display()})"