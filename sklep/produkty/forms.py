from django import forms


from .models import *

class Zamowienie(forms.Form):
    ilosc   = forms.IntegerField(label="",min_value=0,initial=0)


