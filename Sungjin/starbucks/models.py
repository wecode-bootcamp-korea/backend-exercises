from django.db import models

class Drinks(models.Model):
    name    = models.CharField(max_length = 200)
    img_url = models.URLField()

    class Meta:
        db_table = 'starbucks_drinks'



