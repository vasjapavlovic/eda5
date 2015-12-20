from functools import partial

from django import forms

from .models import Aktivnost, Dokument

DateInput = partial(forms.DateInput, {'class': 'datepicker'})
TimeInput = partial(forms.TimeInput, {'class': 'timepicker'})


class AktivnostCreateForm(forms.ModelForm):

    class Meta:
        model = Aktivnost
        fields = (
            'vrsta_aktivnosti',
            'izvajalec',
            'likvidiral',
            'datum',
        )
        widgets = {
            'datum': DateInput(),
        }


class DokumentCreateForm(forms.ModelForm):

    class Meta:
        model = Dokument
        fields = (
            # 'aktivnost',
            'vrsta_dokumenta',
            'avtor',
            'naslovnik',
            'oznaka',
            'naziv',
            'datum',
            'priponka',
        )
        widgets = {
            'datum': DateInput(),
        }
