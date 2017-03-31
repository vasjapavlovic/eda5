# Python
from functools import partial

# Django
from django import forms
from django.contrib.admin.sites import site
from django.utils import timezone

# Models
from ..models import Racun, Konto, PodKonto
from eda5.core.models import ObdobjeLeto

# Forms

# Widgets
from eda5.partnerji.widgets import OsebaForeignKeyRawIdWidget
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
            "povracilo_stroskov_zaposlenemu",
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
            'povracilo_stroskov_zaposlenemu': OsebaForeignKeyRawIdWidget(model._meta.get_field('povracilo_stroskov_zaposlenemu').rel, site),
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
