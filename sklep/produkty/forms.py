from django import forms

from koszyk.models import Cart
from .models import Produkty

class Zamowienie(forms.Form):
    ilosc   = forms.IntegerField(label="",min_value=0,initial=0)

class Przyjmij(forms.ModelForm):
    class Meta:
        model = Produkty
        fields = (
            "kategoria",
            "nazwa",
            "opis",
            "producent",
            "obraz",
            "cena",
            "stan",
            "numer",
            "regał",
            "półka",
            "lokacja_x"
        )
        labels = {
            "lokacja_x": "lokacja na półce"
        }
        widgets = {
            'opis': forms.Textarea(attrs={'cols': 110, 'rows': 2}),
            'nazwa' :forms.Textarea(attrs={'cols' : 110, 'rows': 1}),
        }

