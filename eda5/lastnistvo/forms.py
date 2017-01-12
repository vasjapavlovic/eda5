from functools import partial

from django import forms
from django.db.models import Q

from .models import PredajaLastnine, ProdajaLastnine, NajemLastnine

from eda5.arhiv.models import Arhiviranje

DateInput = partial(forms.DateInput, {'class': 'datepicker'})
TimeInput = partial(forms.TimeInput, {'class': 'timepicker'})


class PredajaLastnineCreateForm(forms.ModelForm):

    class Meta:
        model = PredajaLastnine
        fields = (
            'prodajalec',
            'kupec',
        )


class ProdajaLastnineCreateForm(forms.ModelForm):

    class Meta:
        model = ProdajaLastnine
        fields = (
            'lastniska_enota',
            'datum_predaje',
            'placnik',
        )
        widgets = {
            'datum_predaje': DateInput(),
        }


class NajemLastnineCreateForm(forms.ModelForm):



    class Meta:
        model = NajemLastnine
        fields = (
            'lastniska_enota',
            'predaja_datum',
            'veljavnost_datum',
            # 'najemna_pogodba',
            'veljavnost_trajanje_opisno',
            'placnik',
        )
        widgets = {
            'predaja_datum': DateInput(),
            'veljavnost_datum': DateInput(),
        }


class NajemLastnineVraciloForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(NajemLastnineVraciloForm, self).__init__(*args, **kwargs)

        # prikažemo samo dokumentacijo, ki je del zahtevka v katerem se predaja ključev izvaja
        self.fields['najemna_pogodba'].queryset = Arhiviranje.objects.filter(
            Q(zahtevek=self.instance.predaja_lastnine.zahtevek) &
            Q(dokument__vrsta_dokumenta__oznaka="PGD")
        )

        self.fields['vracilo_zapisnik'].queryset = Arhiviranje.objects.filter(
            Q(zahtevek=self.instance.predaja_lastnine.zahtevek) &
            Q(dokument__vrsta_dokumenta__oznaka="ZAP")
        )

    class Meta:
        model = NajemLastnine
        fields = (
            'najemna_pogodba',
            'vracilo_datum',
            'vracilo_zapisnik',
            'vracilo_posebnosti',
        )
        widgets = {
            'vracilo_datum': DateInput(),
        }