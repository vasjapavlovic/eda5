from functools import partial

from django import forms
from .models import Zaznamek

DateInput = partial(forms.DateInput, {'class': 'datepicker'})
TimeInput = partial(forms.TimeInput, {'class': 'timepicker'})


# class ZaznamekForm(forms.Form):

#     tekst = forms.CharField(widget=forms.Textarea)
#     datum = forms.DateField()
#     ura = forms.TimeField()


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
