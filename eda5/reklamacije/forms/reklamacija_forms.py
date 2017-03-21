from functools import partial

from django import forms
from django.utils import timezone

from ..models import Reklamacija


DateInput = partial(forms.DateInput, {'class': 'datepicker'})
TimeInput = partial(forms.TimeInput, {'class': 'timepicker'})

class ReklamacijaCreateFromZahtevekForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(ReklamacijaCreateFromZahtevekForm, self).__init__(*args, **kwargs)

		#=========================================================
		# oznaka
		#---------------------------------------------------------
		# 2017-1, 2017-2, ...
		leto = timezone.now().date().year

		try:
			st_vnosov = Reklamacija.objects.count()
			zap_st = st_vnosov + 1
		except:
			# pri prvi reklamaciji dodelimo št. 1 : count =0
			zap_st = 1

		nova_oznaka = "%s-%s" % (leto, zap_st)
		self.initial['oznaka'] = nova_oznaka
		self.fields['oznaka'].widget.attrs['readonly'] = True

		#======================================================
		# datum
		#-----------------------------------------------------
		self.initial['datum'] = timezone.now().date()


	class Meta:
		model = Reklamacija
		fields = (
			'oznaka',
			'naziv',
			'opis',
			'datum',
			'narocnik',
			'izvajalec',
			'okvirni_strosek',
		)
		widgets = {
            'datum': DateInput(),
        }
