from django import forms

from .models import PredpisSklop, PredpisPodsklop, PredpisOpravilo, Predpis


class PredpisSklopCreateForm(forms.ModelForm):

    class Meta:
        model = PredpisSklop
        fields = (
            'oznaka',
            'naziv',
            'zap_st',
        )


class PredpisPodsklopCreateForm(forms.ModelForm):

    class Meta:
        model = PredpisPodsklop
        fields = (
            'oznaka',
            'naziv',
            'predpis_sklop',
        )


class PredpisOpraviloCreateForm(forms.ModelForm):

    class Meta:
        model = PredpisOpravilo
        fields = (
            'oznaka',
            'naziv',
            'predpis_podsklop',
            'predpis',
        )


class PredpisCreateForm(forms.ModelForm):

    class Meta:
        model = Predpis
        fields = (
            'oznaka',
            'naziv',
        )
