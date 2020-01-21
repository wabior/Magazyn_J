from django.db import models
from django.shortcuts import render
#   moje
from produkty.models import Produkty

class Cart(models.Model):
    products = models.ManyToManyField(Produkty, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,default=0)
    Statusy = models.TextChoices('Statusy', 'NOWE ZAPISANE WYSŁANE GOTOWE BRAK_MOŻLIWOŚCI_REALIZACJI ZREALIZOWANE ARCHIWALNE')
    Statusy_m = models.TextChoices('Statusy_m','WYSŁANE GOTOWE BRAK_MOŻLIWOŚCI_REALIZACJI')
    status = models.CharField(default='NOWE', blank=0, choices=Statusy.choices, max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Zamówienie"
        verbose_name_plural = "Zamówienia"