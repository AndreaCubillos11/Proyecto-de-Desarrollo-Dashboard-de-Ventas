from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class Venta(models.Model):
    Cliente = models.CharField(max_length=120)
    Barrio = models.CharField(max_length=120)
    Mes = models.IntegerField(
        default=timezone.now().month,
        validators=[MinValueValidator(1), MaxValueValidator(12)],
        error_messages={
            'min_value': 'El mes debe estar entre 1 a 12.',
            'max_value': 'El mes debe estar entre 1 a 12.',
        })