from django import forms

from ..models import Stavba, Etaza, Lokacija, DelStavbe

class StavbaCreateForm(forms.ModelForm):

    class Meta:
        model = Stavba
        fields = (
            'oznaka',
            'naziv', 
            'opis', 
        )


class EtazaCreateForm(forms.ModelForm):

    class Meta:
        model = Etaza
        fields = (
            'oznaka',
            'naziv', 
            'elevation',
            'stavba',
        )


class DelStavbeProstorCreateForm(forms.ModelForm):

    class Meta:
        model = DelStavbe
        fields = (
            'oznaka',
            'naziv', 
            'funkcija',
            'bim_id',
            'podskupina',
        )


class LokacijaCreateForm(forms.ModelForm):

    class Meta:
        model = Lokacija
        fields = (
            'prostor',
            'etaza',
        )