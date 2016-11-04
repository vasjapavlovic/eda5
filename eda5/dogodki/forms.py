from django import forms
from functools import partial

from .models import Dogodek

DateInput = partial(forms.DateInput, {'class': 'datepicker'})
TimeInput = partial(forms.TimeInput, {'class': 'timepicker'})


class DogodekCreateForm(forms.ModelForm):

	class Meta:
		model = Dogodek
		fields = (
			'datum_dogodka',
			'opis_dogodka',
			'cas_dogodka',
			'is_potrebna_prijava_policiji',
			'povzrocitelj',
			'predvidena_visina_skode',
			'is_nastala_skoda',
		)
		widgets = {
            'datum_dogodka': DateInput(),
            'cas_dogodka':TimeInput(),
        }

class DogodekUpdateForm(forms.ModelForm):

	class Meta:
		model = Dogodek
		fields = (
			'datum_dogodka',
			'opis_dogodka',
			'cas_dogodka',
			'is_potrebna_prijava_policiji',
			'povzrocitelj',
			'predvidena_visina_skode',
			'is_nastala_skoda',
		)
		widgets = {
            'datum_dogodka': DateInput(),
            'cas_dogodka':TimeInput(),
        }
