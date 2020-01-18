from django import forms
from .models import *

class Zmiana_Statusu(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['status']
        labels = {
            "status": "status    :"
        }

class Status_f(forms.Form):
    my_choices = [('','filr'),('all','all'),('NOWE', 'NOWE'),
                  ('ZAPISANE', 'ZAPISANE'),('WYSŁANE', 'WYSŁANE'),
                  ('GOTOWE', 'GOTOWE'),('BRAK_MOŻLIWOŚCI_REALIZACJI','BRAK_MOŻLIWOŚCI_REALIZACJI'),
                  ('ARCHIWALNE','ARCHIWALNE')]
    status = forms.ChoiceField(choices=my_choices, widget = forms.Select(attrs={'onchange': 'submit()'}))