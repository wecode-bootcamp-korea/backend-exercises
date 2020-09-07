from django.db import models

class Product(models.Model):
    name        = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    price       = models.IntegerField(default=0)
    image_url   = models.URLField()

