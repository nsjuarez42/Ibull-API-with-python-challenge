from django.db import models

# Create your models here.
class Trade(models.Model):
    id = models.AutoField(primary_key=True)
    type =models.CharField(max_length=4)
    user_id = models.IntegerField()
    symbol = models.CharField(max_length=3)
    shares = models.IntegerField()
    price = models.FloatField()
    timestamp = models.BigIntegerField()


