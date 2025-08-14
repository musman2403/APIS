from django.db import models
from django.views.generic import ListView
import uuid

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

    def __str__(self):
        return self.name

class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=250)
    discount = models.FloatField()



