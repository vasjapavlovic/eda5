from functools import partial

from django import forms

from .models import Zaznamek

DateInput = partial(forms.DateInput, {'class': 'datepicker'})
TimeInput = partial(forms.TimeInput, {'class': 'timepicker'})


class ZaznamekForm(forms.ModelForm):

    class Meta:
        model = Zaznamek
        fields = (
            'tekst',
            'datum',
            'ura',
        )
        widgets = {
            'datum': DateInput(),
            'ura': TimeInput(),
        }


class ZaznamekUpdateForm(ZaznamekForm):
    pass

