from django.db import models
#   moje
from produkty.models import Produkty

class Cart(models.Model):
    products = models.ManyToManyField(Produkty, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,default=0)
    Statusy = models.TextChoices('Statusy', 'NOWE ZAPISEAE WYSŁANE GOTOWE ZREALIZOWANE ARCHIWALNE')
    status = models.CharField(default='NOWE', blank=True, choices=Statusy.choices, max_length=15)