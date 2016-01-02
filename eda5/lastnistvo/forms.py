from django import forms

from .models import PredajaLastnine, ProdajaLastnine, NajemLastnine


class PredajaLastnineCreateForm(forms.ModelForm):

    class Meta:
        model = PredajaLastnine
        fields = (
            'prodajalec',
            'kupec',
        )


class ProdajaLastnineCreateForm(forms.ModelForm):

    class Meta:
        model = ProdajaLastnine
        fields = (
            'lastniska_enota',
            'datum_predaje',
            'placnik',
        )


class NajemLastnineCreateForm(forms.ModelForm):

    class Meta:
        model = NajemLastnine
        fields = (
            'lastniska_enota',
            'datum_predaje',
            'placnik',
            'datum_veljavnosti',
        )
