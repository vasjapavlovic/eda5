from django import forms
from functools import partial

from .models import Dogodek
from eda5.posta.models import Dokument

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
			'is_nastala_skoda',
			'povzrocitelj',


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
			'prijava_skode',
			'prijava_policiji',
			'poravnava_skode',
		)
		widgets = {
            'datum_dogodka': DateInput(),
            'cas_dogodka':TimeInput(),
        }
