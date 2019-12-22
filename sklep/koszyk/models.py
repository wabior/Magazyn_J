from django.db import models
#   moje
from produkty.models import Produkty

class Cart(models.Model):
    products = models.ManyToManyField(Produkty, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)