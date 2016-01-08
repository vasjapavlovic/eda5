from django import forms
from functools import partial
from django.forms import formset_factory

from ..models import Strosek


DateInput = partial(forms.DateInput, {'class': 'datepicker'})
TimeInput = partial(forms.TimeInput, {'class': 'timepicker'})


class StrosekOsnovaCreateForm(forms.ModelForm):

    class Meta:
        model = Strosek
        fields = (
            'naziv',
            'datum_storitve_od',
            'datum_storitve_do',
            'obdobje_obracuna_leto',
            'obdobje_obracuna_mesec',
            'delovni_nalog',
            'osnova',
            'stopnja_ddv',
            # 'vrsta_stroska', --> vrsta stroska se izbere pod StrosekVrstaIzbiraForm
        )

        widgets = {
            'datum_storitve_od': DateInput(),
            'datum_storitve_do': DateInput(),
        }


class StrosekRazdelilnikCreateForm(forms.ModelForm):

    class Meta:
        model = Strosek
        fields = (
            'lastniska_skupina',
            'delilnik_vrsta',
            'delilnik_kljuc',
            'is_strosek_posameznidel',
        )


class StrosekUpdateForm(forms.ModelForm):

    class Meta:
        model = Strosek
        fields = (
            'oznaka',
            'naziv',
            'datum_storitve_od',
            'datum_storitve_do',
            'obdobje_obracuna_leto',
            'obdobje_obracuna_mesec',
            'delovni_nalog',
            'osnova',
            'stopnja_ddv',
            'vrsta_stroska',
            'lastniska_skupina',
            'delilnik_vrsta',
            'delilnik_kljuc',
            'is_strosek_posameznidel',
        )

        widgets = {
            'datum_storitve_od': DateInput(),
            'datum_storitve_do': DateInput(),
        }

