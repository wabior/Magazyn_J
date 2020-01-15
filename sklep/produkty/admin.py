from django.contrib import admin

# Register your models here.
from .models import Produkty
from .models import Producent
from .models import Kategoria

admin.site.register(Produkty)
admin.site.register(Producent)
admin.site.register(Kategoria)


