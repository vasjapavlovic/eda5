from functools import partial

from django import forms

from .models import PredajaLastnine, ProdajaLastnine, NajemLastnine

DateInput = partial(forms.DateInput, {'class': 'datepicker'})
TimeInput = partial(forms.TimeInput, {'class': 'timepicker'})


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
        widgets = {
            'datum_predaje': DateInput(),
        }


class NajemLastnineCreateForm(forms.ModelForm):

    class Meta:
        model = NajemLastnine
        fields = (
            'lastniska_enota',
            'datum_predaje',
            'placnik',
            'datum_veljavnosti',
        )
        widgets = {
            'datum_predaje': DateInput(),
            'datum_veljavnosti': DateInput(),
        }
