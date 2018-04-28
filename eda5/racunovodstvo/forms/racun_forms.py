# Python
from functools import partial

# Django
from django import forms
from django.contrib.admin.sites import site
from django.utils import timezone
from django.db.models import Q

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
            "stavba",
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



class RacunSearchForm(forms.Form):
    oznaka = forms.CharField(label='oznaka', required=False)
    naziv = forms.CharField(label='naziv', required=False)

    # začetne nastavitve prikazanega "form"
    def __init__(self, *args, **kwargs):
        super(RacunSearchForm, self).__init__(*args, **kwargs)
        # na začetku so okenca za vnos filtrov prazna
        self.initial['oznaka'] = ""
        self.initial['naziv'] = ""

    def filter_queryset(self, request, queryset):

        oznaka_filter = self.cleaned_data['oznaka']
        naziv_filter = self.cleaned_data['naziv']

        # filtriranje samo po oznaki
        if oznaka_filter and not naziv_filter:
            return queryset.filter(
                Q(oznaka__icontains=oznaka_filter)
            )

        # filtriranje ostalo
        if naziv_filter and not oznaka_filter:
            return queryset.filter(
                Q(arhiviranje__dokument__oznaka__icontains=naziv_filter)
            )


        # uporabnik filtrira po kratkem imenu in naslovu partnerja
        if oznaka_filter and naziv_filter:
            return queryset.filter(
                (
                    Q(oznaka__icontains=oznaka_filter)
                ) &
                (
                    Q(arhiviranje__dokument__oznaka__icontains=naziv_filter)
                )
            )

        return queryset
