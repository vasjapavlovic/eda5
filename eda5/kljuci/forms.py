from django import forms

from .models import PredajaKljuca


class PredajaKljucaCreateForm(forms.ModelForm):

	class Meta:
		model = PredajaKljuca
		fields = (
			'kljuc',
			'datum_predaje'
		)