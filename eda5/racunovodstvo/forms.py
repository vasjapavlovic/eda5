from django import forms
from functools import partial

from .models import Racun, Konto, PodKonto, SkupinaVrsteStroska, VrstaStroska
from eda5.core.models import ObdobjeLeto, ObdobjeMesec

DateInput = partial(forms.DateInput, {'class': 'datepicker'})
TimeInput = partial(forms.TimeInput, {'class': 'timepicker'})


class RacunCreateForm(forms.ModelForm):

    class Meta:
        model = Racun
        fields = (
            # "dokument",
            "davcna_klasifikacija",
            "datum_storitve_od",
            "datum_storitve_do",
            "obdobje_obracuna_leto",
            "obdobje_obracuna_mesec",
            "narocilo",
            "osnova_0",
            "osnova_1",
            "osnova_2",
            )
        widgets = {
            'datum_storitve_od': DateInput(),
            'datum_storitve_do': DateInput(),
        }


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


class SkupinaVrsteStroskaCreateForm(forms.ModelForm):

    class Meta:
        model = SkupinaVrsteStroska
        fields = (
            'oznaka',
            'naziv',
            'zap_st',
            'skupina',
        )


class VrstaStroskaCreateForm(forms.ModelForm):

    class Meta:
        model = VrstaStroska
        fields = (
            'oznaka',
            'naziv',
            'zap_st',
            'skupina',
        )
