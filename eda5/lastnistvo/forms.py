from functools import partial

from django import forms
from django.contrib.admin.sites import site
from django.db.models import Q


from .models import PredajaLastnine, ProdajaLastnine, NajemLastnine

from eda5.arhiv.models import Arhiviranje
from eda5.etaznalastnina.models import LastniskaEnotaInterna

# Partnerji
from eda5.partnerji.widgets import PartnerForeignKeyRawIdWidget, OsebaForeignKeyRawIdWidget

DateInput = partial(forms.DateInput, {'class': 'datepicker'})
TimeInput = partial(forms.TimeInput, {'class': 'timepicker'})


class PredajaLastnineCreateForm(forms.ModelForm):

    class Meta:
        model = PredajaLastnine
        fields = (
            'prodajalec',
            'kupec',
        )
        widgets = {
            'prodajalec': PartnerForeignKeyRawIdWidget(model._meta.get_field('prodajalec').rel, site),
            'kupec': PartnerForeignKeyRawIdWidget(model._meta.get_field('kupec').rel, site),
        }


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
            'placnik': PartnerForeignKeyRawIdWidget(model._meta.get_field('placnik').rel, site),
        }

class ProdajaLastnineUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProdajaLastnineUpdateForm, self).__init__(*args, **kwargs)

        self.fields['zapisnik_izrocitev'].queryset = Arhiviranje.objects.filter(
            Q(zahtevek=self.instance.predaja_lastnine.zahtevek) &
            Q(dokument__vrsta_dokumenta__oznaka="ZAP")
        )

    class Meta:
        model = ProdajaLastnine
        fields = (
            'lastniska_enota',
            'datum_predaje',
            'placnik',
            'zapisnik_izrocitev',
        )
        widgets = {
            'datum_predaje': DateInput(),
            'placnik': PartnerForeignKeyRawIdWidget(model._meta.get_field('placnik').rel, site),
        }

class NajemLastnineCreateForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super(NajemLastnineCreateForm, self).__init__(*args, **kwargs)

    #     # pri izbiri lastniške enote prikažemo samo neoddane
    #     self.fields['lastniska_enota'].queryset = LastniskaEnotaInterna.objects.exclude(
    #         Q(najemlastnine__vracilo_datum__isnull=True)
    #     )


    class Meta:
        model = NajemLastnine
        fields = (
            'lastniska_enota',
            'predaja_datum',
            'veljavnost_datum',
            'veljavnost_trajanje_opisno',
            'placnik',
        )
        widgets = {
            'predaja_datum': DateInput(),
            'veljavnost_datum': DateInput(),
            'placnik': PartnerForeignKeyRawIdWidget(model._meta.get_field('placnik').rel, site),
        }


class NajemLastnineVraciloForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(NajemLastnineVraciloForm, self).__init__(*args, **kwargs)

        # prikažemo samo dokumentacijo, ki je del zahtevka v katerem se predaja ključev izvaja
        self.fields['najemna_pogodba'].queryset = Arhiviranje.objects.filter(
            Q(zahtevek=self.instance.predaja_lastnine.zahtevek) &
            Q(dokument__vrsta_dokumenta__oznaka="PGD")
        )

        self.fields['zapisnik_izrocitev'].queryset = Arhiviranje.objects.filter(
            Q(zahtevek=self.instance.predaja_lastnine.zahtevek) &
            Q(dokument__vrsta_dokumenta__oznaka="ZAP")
        )
        
        self.fields['vracilo_zapisnik'].queryset = Arhiviranje.objects.filter(
            Q(zahtevek=self.instance.predaja_lastnine.zahtevek) &
            Q(dokument__vrsta_dokumenta__oznaka="ZAP")
        )


    class Meta:
        model = NajemLastnine
        fields = (
            'lastniska_enota',
            'placnik',
            'predaja_datum',
            'veljavnost_datum',
            'veljavnost_trajanje_opisno',
            'najemna_pogodba',
            'zapisnik_izrocitev',
            'vracilo_datum',
            'vracilo_zapisnik',
            'vracilo_posebnosti',
            'opombe',
        )
        widgets = {
            'predaja_datum': DateInput(),
            'veljavnost_datum': DateInput(),
            'vracilo_datum': DateInput(),
            'placnik': PartnerForeignKeyRawIdWidget(model._meta.get_field('placnik').rel, site),
        }