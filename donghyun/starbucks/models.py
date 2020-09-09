from django.db import models

# Create your models here.

class Users(models.Model):
    name            = models.CharField(max_length =50)
    img_link        = models.URLField(max_length=200, default='')
    
    class Meta:
        db_table = 'drink' 


