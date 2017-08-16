from functools import partial
from django import forms

from .models import VeljavnostDokumenta

DateInput = partial(forms.DateInput, {'class': 'datepicker'})
TimeInput = partial(forms.TimeInput, {'class': 'timepicker'})


class VeljavnostDokumentaCreateForm(forms.ModelForm):

    class Meta:
        model = VeljavnostDokumenta
        fields = (
            'stavba',
            'velja_od',
            'velja_do',
        )
        widgets = {
            'velja_od': DateInput(),
            'velja_do': DateInput(),
        }


class VeljavnostDokumentaUpdateForm(VeljavnostDokumentaCreateForm):
    
    class Meta:
        model = VeljavnostDokumenta
        fields = (
            'is_active',
            'stavba',
            'vrsta_stroska',
            'velja_od',
            'velja_do',
        )
        widgets = {
            'velja_od': DateInput(),
            'velja_do': DateInput(),
        }