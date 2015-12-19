from django import forms

from .models import Podskupina, Skupina, DelStavbe, ProjektnoMesto, Element, Nastavitev


class DelCreateForm(forms.ModelForm):

    class Meta:
        model = DelStavbe
        fields = (
            'podskupina',
            'oznaka',
            'naziv',
            'shema',
            'lastniska_skupina',
        )


class SkupinaCreateForm(forms.ModelForm):

    class Meta:
        model = Skupina
        fields = (
            'oznaka',
            'naziv',
        )


class PodskupinaCreateForm(forms.ModelForm):

    class Meta:
        model = Podskupina
        fields = (
            'oznaka',
            'naziv',
            'skupina'
        )


class ProjektnoMestoCreateForm(forms.ModelForm):

    class Meta:
        model = ProjektnoMesto
        fields = (
            'oznaka',
            'naziv',
            'funkcija',
            'del_stavbe',
            'tip_elementa',
        )


class ElementCreateForm(forms.ModelForm):

    class Meta:
        model = Element
        fields = (
            'tovarniska_st',
            'serijska_st',
            'artikel',
            'projektno_mesto',
        )


class NastavitevCreateForm(forms.ModelForm):

    class Meta:
        model = Nastavitev
        fields = (
            'obratovalni_parameter',
            'vrednost',
            'datum_nastavitve',
            'element',
        )
