from functools import partial

from django import forms

from .models import PredajaKljuca

DateInput = partial(forms.DateInput, {'class': 'datepicker'})
TimeInput = partial(forms.TimeInput, {'class': 'timepicker'})


class PredajaKljucaCreateForm(forms.ModelForm):

	class Meta:
		model = PredajaKljuca
		fields = (
			'kljuc',
			'datum_predaje',
			'vrsta_predaje'
		)
		widgets = {
            'datum_predaje': DateInput(),
        }