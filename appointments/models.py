from django.db import models
from django.contrib.auth import get_user_model
from properties.models import Property

UserModel = get_user_model()

class Appointment(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='appointments')
    client = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='appointments')
    date_and_time = models.DateTimeField()
    notes = models.TextField(blank=True, null=True, verbose_name="Additional Notes")
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Viewing: {self.property.title} by {self.client.username}"