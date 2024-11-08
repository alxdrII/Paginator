from django.db import models


# Create your models here.
class Product(models.Model):
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    items = models.IntegerField()

    def __str__(self):
        return self.code