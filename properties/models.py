from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator

UserModel = get_user_model()

class Feature(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Feature Name")

    def __str__(self):
        return self.name

class Property(models.Model):
    PROPERTY_TYPES = [
        ('apartment', 'Apartment'),
        ('house', 'House'),
        ('commercial', 'Commercial'),

    ]

    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='property_images/', blank=True, null=True)
    agent = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='properties')
    features = models.ManyToManyField(Feature, related_name='properties', blank=True)
    likes = models.ManyToManyField(UserModel, related_name='favorite_properties', blank=True)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )

    def __str__(self):
        return f"{self.title} - {self.location}"


