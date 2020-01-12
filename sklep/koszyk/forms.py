from django import forms
from .models import *

class Zmiana_Statusu(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['status']
        labels = {
            "status": "status    :"
        }