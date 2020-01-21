from django import forms
from .models import *

class Zmiana_Statusu(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['status']
        labels = {"status": "status    :"}

class Zmiana_Statusu_M(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['status']
        labels = {"status": "status    :"}

    def __init__(self, *args, **kwargs):
        super(Zmiana_Statusu_M, self).__init__(*args, **kwargs)
        self.fields['status'].choices = Status_m.my_choices

class Status_f(forms.Form):
    my_choices = [('filtrowanie',''),('all','all'),('NOWE', 'NOWE'),
                  ('ZAPISANE', 'ZAPISANE'),('WYSŁANE', 'WYSŁANE'),
                  ('GOTOWE', 'GOTOWE'),('BRAK_MOŻLIWOŚCI_REALIZACJI','BRAK_MOŻLIWOŚCI_REALIZACJI'),
                  ('ARCHIWALNE','ARCHIWALNE')]
    status = forms.ChoiceField(choices=my_choices, widget = forms.Select(attrs={'onchange': 'submit()'}))

class Status_m(forms.Form):
    my_choices = [('WYSŁANE', 'WYSŁANE'), ('GOTOWE', 'GOTOWE'),('BRAK_MOŻLIWOŚCI_REALIZACJI','BRAK_MOŻLIWOŚCI_REALIZACJI'),
             ]
    status = forms.ChoiceField(choices=my_choices, widget = forms.Select(attrs={'onchange': 'submit()'}))