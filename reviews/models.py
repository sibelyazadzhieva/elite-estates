from django.db import models
from django.contrib.auth import get_user_model
from properties.models import Property
from django.core.validators import MinValueValidator, MaxValueValidator

UserModel = get_user_model()

class Review(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Rate between 1 and 5"
    )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.author.username} for {self.property.title}"