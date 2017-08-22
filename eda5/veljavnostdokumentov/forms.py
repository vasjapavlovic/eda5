from functools import partial
from django import forms
from django.utils import timezone

from .models import VeljavnostDokumenta
from eda5.narocila.models import Narocilo
from eda5.planiranje.models import PlaniranoOpravilo

DateInput = partial(forms.DateInput, {'class': 'datepicker'})
TimeInput = partial(forms.TimeInput, {'class': 'timepicker'})


class VeljavnostDokumentaCreateForm(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        super(VeljavnostDokumentaCreateForm, self).__init__(*args, **kwargs)

        self.fields['planirano_opravilo'].queryset = PlaniranoOpravilo.objects.filter(is_active=True)
        self.fields['narocilo'].queryset = Narocilo.objects.filter(datum_veljavnosti__gte=timezone.now()).order_by('-id')

    class Meta:
        model = VeljavnostDokumenta
        fields = (
            'stavba',
            'narocilo',
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
        self.fields['narocilo'].queryset = Narocilo.objects.filter(datum_veljavnosti__gte=timezone.now()).order_by('-id')
    
    class Meta:
        model = VeljavnostDokumenta
        fields = (
            'is_active',
            'stavba',
            'narocilo',
            'vrsta_stroska',
            'planirano_opravilo',
            'velja_od',
            'velja_do',
        )
        widgets = {
            'velja_od': DateInput(),
            'velja_do': DateInput(),
        }