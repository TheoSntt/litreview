from django.db import models
from django.conf import settings
from PIL import Image


class Ticket(models.Model):
    def __str__(self):
        return f'{self.title}'

    title = models.fields.CharField(max_length=128)
    description = models.fields.CharField(max_length=2048)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tickets')
    image = models.ImageField(null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

    IMAGE_MAX_SIZE = (200, 200)

    def resize_image(self):
        if self.image:
            image = Image.open(self.image)
            image.thumbnail(self.IMAGE_MAX_SIZE)
            image.save(self.image.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()

    def has_been_reviewed(self):
        return self.review.exists()
