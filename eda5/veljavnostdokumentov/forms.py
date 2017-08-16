from functools import partial
from django import forms

from .models import VeljavnostDokumenta
from eda5.planiranje.models import PlaniranoOpravilo

DateInput = partial(forms.DateInput, {'class': 'datepicker'})
TimeInput = partial(forms.TimeInput, {'class': 'timepicker'})


class VeljavnostDokumentaCreateForm(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        super(VeljavnostDokumentaUpdateForm, self).__init__(*args, **kwargs)

        self.fields['planirano_opravilo'].queryset = PlaniranoOpravilo.objects.filter(is_active=True)

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


class VeljavnostDokumentaUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(VeljavnostDokumentaUpdateForm, self).__init__(*args, **kwargs)

        self.fields['planirano_opravilo'].queryset = PlaniranoOpravilo.objects.filter(is_active=True)
    
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