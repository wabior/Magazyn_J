from django.db import models

class Producent(models.Model):
    def __str__(self):
        return self.nazwa
    nazwa   = models.CharField(max_length=60)
    opis    = models.TextField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name        = "Producent"
        verbose_name_plural = "Producenci"

class Kategoria(models.Model):
    nazwa = models.CharField(max_length=30)
    def __str__(self):
        return self.nazwa
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name        = "Kategoria"
        verbose_name_plural = "Kategorie"

class Tagi(models.Model):
    def __str__(self):
        return self.name
    name    = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name        = "Tag"
        verbose_name_plural = "Tagi"

class Produkty(models.Model):
    def __str__(self):
        return self.nazwa
    n_cz    = 235110
    nazwa   = models.CharField(max_length=60)
    opis    = models.TextField(blank=True)
    cena    = models.DecimalField(max_digits=99999 ,decimal_places=2)
    producent = models.ForeignKey(Producent,on_delete=models.CASCADE,blank=True,null=True)
    kategoria = models.ForeignKey(Kategoria,on_delete=models.CASCADE,blank=True,null=True)
    tagi      = models.ManyToManyField(Tagi,blank=True,null=True)
    obraz   = models.FileField(upload_to='', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    stan    = models.IntegerField(default=0)
    numer   = models.IntegerField(max_length=6,default=n_cz + 10)
    slug    = models.SlugField()
    regał_wygory = models.TextChoices('regały', 'Regał_1 Regał_2 Regał_3 Regał_4')
    lokacja_x_wybory = models.TextChoices('lokacje', 'slot_1 slot_2 slot_3 slot_4 slot_5 slot_6 slot_7 slot_8')
    półka_wybory = models.TextChoices('półki', 'Półka_1 Półka_2 Półka_3 Półka_4')
    regał = models.CharField(default='Regał_1', blank=True, choices=regał_wygory.choices, max_length=30)
    półka = models.CharField(default='Półka_1', blank=True, choices=półka_wybory.choices, max_length=30)
    lokacja_x = models.CharField(default='slot_1', blank=True, choices=lokacja_x_wybory.choices, max_length=30)


    class Meta:
        verbose_name        = "Produkt"
        verbose_name_plural = "Produkty"

