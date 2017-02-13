from django import forms
from django.utils.html import conditional_escape, mark_safe
from django.utils.encoding import smart_text

from .models import Podskupina, Skupina, DelStavbe, ProjektnoMesto, Element, Nastavitev
from eda5.zahtevki.models import Zahtevek


class SkupinaIzbiraForm(forms.Form):

    skupina = forms.ModelChoiceField(queryset=Skupina.objects.all())
    podskupina_hidden = forms.ModelChoiceField(queryset=Podskupina.objects.all())


class ElementIzbiraForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(ElementIzbiraForm, self).__init__(*args, **kwargs)

        self.fields['skupina'].required = False
        self.fields['podskupina'].required = False
        self.fields['del_stavbe'].required = False

        self.fields['podskupina_hidden'].required = False
        self.fields['del_stavbe_hidden'].required = False
        self.fields['element_hidden'].required = False

    skupina = forms.ModelChoiceField(queryset=Skupina.objects.all())
    podskupina = forms.ModelChoiceField(queryset=Podskupina.objects.all())
    del_stavbe = forms.ModelChoiceField(queryset=DelStavbe.objects.all())

    # za filtriranje
    podskupina_hidden = forms.ModelChoiceField(queryset=Podskupina.objects.all())
    del_stavbe_hidden = forms.ModelChoiceField(queryset=DelStavbe.objects.all())
    element_hidden = forms.ModelChoiceField(queryset=ProjektnoMesto.objects.all())


class DelCreateForm(forms.ModelForm):

    class Meta:
        model = DelStavbe
        fields = (
            'podskupina',
            'oznaka',
            'naziv',
            'funkcija',
            'shema',
            'lastniska_skupina',
        )


class DelUpdateForm(DelCreateForm):
    pass


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
