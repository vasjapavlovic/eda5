from django import forms
from functools import partial
from django.utils import timezone

from eda5.core.models import ObdobjeLeto

from ..models import Racun, Konto, PodKonto

DateInput = partial(forms.DateInput, {'class': 'datepicker'})
TimeInput = partial(forms.TimeInput, {'class': 'timepicker'})


class RacunCreateForm(forms.ModelForm):

    class Meta:
        model = Racun
        fields = (
            "davcna_klasifikacija",
            "datum_storitve_od",
            "datum_storitve_do",
            "valuta",
            "je_reprezentanca",
            "reprezentanca_opis",
            "zavrnjen",
            "zavrnjen_datum",
            "zavrnjen_obrazlozitev_text",
            )
        widgets = {
            'datum_storitve_od': DateInput(),
            'datum_storitve_do': DateInput(),
            'valuta': DateInput(),
        }


class RacunUpdateForm(RacunCreateForm):
    pass


class KontoCreateForm(forms.ModelForm):

    class Meta:
        model = Konto
        fields = (
            'oznaka',
            'naziv',
            'zap_st',
        )


class PodkontoCreateForm(forms.ModelForm):

    class Meta:
        model = PodKonto
        fields = (
            'oznaka',
            'naziv',
            'zap_st',
            'skupina',
        )
