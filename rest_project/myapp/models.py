from django.db import models

# Create your models here.
class Ticks(models.Model):

    ticker = models.CharField(max_length = 200)
    order_type = models.CharField(max_length = 200)
    quantity = models.CharField(max_length = 200)
    currency = models.CharField(max_length = 200)
    exchange = models.CharField(max_length = 200)


