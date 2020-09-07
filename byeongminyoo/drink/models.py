from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'drinks'
