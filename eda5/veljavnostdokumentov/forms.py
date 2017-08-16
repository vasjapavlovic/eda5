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
            'planirano_opravilo',
            # vrsta_stroska --> eda5:racunovodstvo:vrsta_stroska --> izbiraForm
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
            'planirano_opravilo',
            'velja_od',
            'velja_do',
        )
        widgets = {
            'velja_od': DateInput(),
            'velja_do': DateInput(),
        }