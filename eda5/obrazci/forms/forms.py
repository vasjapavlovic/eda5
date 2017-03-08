from django import forms
from django.contrib.admin.sites import site

# relative imports
from ..models import ObrazecSplosno

from eda5.arhiv.widgets import ArhiviranjeManyToManyRawIdWidget
from eda5.partnerji.widgets import PartnerForeignKeyRawIdWidget, OsebaForeignKeyRawIdWidget




class ObrazecCreateForm(forms.ModelForm):
	
	class Meta:
		model = ObrazecSplosno
		fields=(
			'vrsta_dokumenta',
			'oznaka',
			'datum',
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
