from functools import partial
from django.db.models import Q
from django import forms

from .models import PredajaKljuca

from eda5.arhiv.models import Arhiviranje

DateInput = partial(forms.DateInput, {'class': 'datepicker'})
TimeInput = partial(forms.TimeInput, {'class': 'timepicker'})


class PredajaKljucaCreateForm(forms.ModelForm):

	# def __init__(self, *args, **kwargs):
	# 	super(PredajaKljucaCreateForm, self).__init__(*args, **kwargs)

	# 	# prikažemo samo dokumentacijo, ki je del zahtevka v katerem se predaja ključev izvaja
	# 	self.fields['predaja_zapisnik'].queryset = Arhiviranje.objects.filter(zahtevek=self.instance.zahtevek)

	class Meta:
		model = PredajaKljuca
		fields = (
			'kljuc',
			'vrsta_predaje',
			'predaja_datum',
			# 'predaja_zapisnik', --> v vračilu se updata
		)
		widgets = {
            'datum_predaje': DateInput(),
        }


class PredajaKljucaVraciloForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(PredajaKljucaVraciloForm, self).__init__(*args, **kwargs)

		# Prikažemo samo dokumentacijo, ki je del zahtevka v katerem se predaja ključev izvaja.
		# Prikaže naj samo zapisnike
		self.fields['predaja_zapisnik'].queryset = Arhiviranje.objects.filter(
			Q(zahtevek=self.instance.zahtevek) & 
			Q(dokument__vrsta_dokumenta__oznaka="ZAP")
		)
		self.fields['vracilo_zapisnik'].queryset = Arhiviranje.objects.filter(
			Q(zahtevek=self.instance.zahtevek) & 
			Q(dokument__vrsta_dokumenta__oznaka="ZAP")
		)

	class Meta:
		model = PredajaKljuca

		# predaja_zapisnik spada v PredajaKljucaCreateForm vendar neznam še to sprogramirat
		fields = (
			'predaja_zapisnik',
			'vracilo_datum',
			'vracilo_zapisnik',
			'vracilo_posebnosti',
		)
		widgets = {
            'vracilo_datum': DateInput(),
        }