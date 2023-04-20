from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

class Ticket(models.Model):
    def __str__(self):
        return f'{self.title}'
    
    title = models.fields.CharField(max_length=128)
    description = models.fields.CharField(max_length=2048)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
