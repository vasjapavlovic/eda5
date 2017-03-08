from django import forms
from django.contrib.admin.sites import site
from django.utils import timezone

# relative imports
from ..models import ObrazecSplosno

from eda5.arhiv.widgets import ArhiviranjeManyToManyRawIdWidget
from eda5.partnerji.widgets import PartnerForeignKeyRawIdWidget, OsebaForeignKeyRawIdWidget




class ObrazecCreateForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(ObrazecCreateForm, self).__init__(*args, **kwargs)

		self.initial['objava'] =  timezone.localtime(timezone.now())

	class Meta:
		model = ObrazecSplosno
		fields=(
			'objava',
			'vrsta_dokumenta',
			'zadeva',
			'vsebina',
			'posiljatelj',
			'naslovnik',
			'oseba_izdelal',
			'oseba_odgovorna',
			'priloge',
		)
		widgets={
            'priloge': ArhiviranjeManyToManyRawIdWidget(model._meta.get_field('priloge').rel, site),
            'posiljatelj': PartnerForeignKeyRawIdWidget(model._meta.get_field('posiljatelj').rel, site),
            'naslovnik': PartnerForeignKeyRawIdWidget(model._meta.get_field('naslovnik').rel, site),
            'oseba_izdelal': OsebaForeignKeyRawIdWidget(model._meta.get_field('oseba_izdelal').rel, site),
            'oseba_odgovorna': OsebaForeignKeyRawIdWidget(model._meta.get_field('oseba_odgovorna').rel, site),
		}
