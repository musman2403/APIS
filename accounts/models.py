from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone = models.CharField(max_length=15, blank=True, null=True)
    registered_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.PositiveIntegerField()
    image_url = models.URLField(max_length=2083)  # or use ImageField if uploading

    def __str__(self):
        return self.name
