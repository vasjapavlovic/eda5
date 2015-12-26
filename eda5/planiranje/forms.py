from django import forms

from .models import Plan, PlaniranoOpravilo


class PlanCreateform(forms.ModelForm):

    class Meta:
        model = Plan
        fields = (
            'oznaka',
            'naziv',
            'zap_st',
            'opis',
            'sklop',
        )


class PlaniranoOpraviloCreateform(forms.ModelForm):

    class Meta:
        model = PlaniranoOpravilo
        fields = (
            'oznaka',
            'naziv',
            'namen',
            'obseg',
            'perioda_predpisana_enota',
            'perioda_predpisana_enota_kolicina',
            'perioda_predpisana_kolicina_na_enoto',
            'datum_prve_izvedbe',
            'opomba',

        )
