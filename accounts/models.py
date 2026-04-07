from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=15,
        blank=True,
        null=True,
        verbose_name="Phone Number"
    )
    profile_picture = models.ImageField(
        upload_to='profiles/',
        blank=True,
        null=True,
        verbose_name="Profile Picture"
    )
    is_agent = models.BooleanField(
        default=False,
        verbose_name="Is Real Estate Agent"
    )

    def __str__(self):
        return f"{self.username} ({'Agent' if self.is_agent else 'User'})"