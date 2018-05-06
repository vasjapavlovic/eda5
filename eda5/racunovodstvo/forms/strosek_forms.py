from django import forms
from functools import partial
from django.forms import formset_factory

from ..models import Strosek

# potrebno za RawIdWidget
from django.contrib.admin.sites import site
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.core.exceptions import ValidationError
from django.template.loader import render_to_string
from django.utils import timezone

from eda5.delovninalogi.models import DelovniNalog

from eda5.delovninalogi.widgets import DelovniNalogSelectWithPop, DelovniNalogMultipleSelectWithPop, DelovniNalogForeignKeyRawIdWidget


DateInput = partial(forms.DateInput, {'class': 'datepicker'})
TimeInput = partial(forms.TimeInput, {'class': 'timepicker'})


class StrosekOsnovaCreateForm(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        super(StrosekOsnovaCreateForm, self).__init__(*args, **kwargs)

        self.fields['delovni_nalog'].queryset = DelovniNalog.objects.filter(strosek__isnull=True)


    class Meta:
        model = Strosek
        fields = (
            'naziv',
            'datum_storitve_od',
            'datum_storitve_do',
            'delovni_nalog',
            'narocilo',
            'osnova',
            'stopnja_ddv',
            # 'vrsta_stroska', --> vrsta stroska se izbere pod StrosekVrstaIzbiraForm
        )

        widgets = {
            'datum_storitve_od': DateInput(),
            'datum_storitve_do': DateInput(),
            'delovni_nalog': DelovniNalogForeignKeyRawIdWidget(model._meta.get_field('delovni_nalog').rel, site),
        }



class StrosekRazdelilnikCreateForm(forms.ModelForm):
    pass
    # class Meta:
    #     model = Strosek
    #     fields = (
    #         'lastniska_skupina',
    #         'delilnik_vrsta',
    #         'delilnik_kljuc',
    #         'is_strosek_posameznidel',
    #     )


class StrosekUpdateForm(forms.ModelForm):

    class Meta:
        model = Strosek
        fields = (
            'oznaka',
            'naziv',
            'datum_storitve_od',
            'datum_storitve_do',
            'delovni_nalog',
            'narocilo',
            'osnova',
            'stopnja_ddv',
            'vrsta_stroska',
        )

        widgets = {
            'datum_storitve_od': DateInput(),
            'datum_storitve_do': DateInput(),
        }
