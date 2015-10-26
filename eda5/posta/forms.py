from django import forms

from .models import Dokument


class PrejetaPostaCreateForm(forms.ModelForm):

    class Meta:
        model = Dokument
        fields = (
            "vrsta_dokumenta",
            "posiljatelj",
            "datum_prejema",
            "oznaka",
            "opis",
            "priponka",
            )
