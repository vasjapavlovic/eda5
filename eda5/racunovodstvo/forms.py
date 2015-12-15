from django import forms

from .models import Racun, Konto, PodKonto, SkupinaVrsteStroska, VrstaStroska
from eda5.core.models import ObdobjeLeto, ObdobjeMesec


class RacunCreateForm(forms.ModelForm):

    class Meta:
        model = Racun
        fields = (
            # "dokument",
            "davcna_klasifikacija",
            "datum_storitve_od",
            "datum_storitve_do",
            "obdobje_obracuna_leto",
            "obdobje_obracuna_mesec",
            "narocilo",
            "osnova_0",
            "osnova_1",
            "osnova_2",
            )


class RacunAddWidget(forms.Form):

    OBDOBJE_LETO = ObdobjeLeto.objects.all()
    OBDOBJE_MESEC = ObdobjeMesec.objects.all()

    davcna_klasifikacija = forms.CharField()
    datum_storitve_od = forms.DateField(widget=forms.TextInput(attrs=
                                {
                                    'class':'datepicker'
                                }))
    datum_storitve_do = forms.DateField(widget=forms.TextInput(attrs=
                                {
                                    'class':'datepicker'
                                }))
    obdobje_obracuna_leto = forms.ModelChoiceField(queryset=OBDOBJE_LETO)
    obdobje_obracuna_mesec = forms.ModelChoiceField(queryset=OBDOBJE_MESEC)


class KontoCreateForm(forms.ModelForm):

    class Meta:
        model = Konto
        fields = (
            'oznaka',
            'naziv',
            'zap_st',
        )


class PodkontoCreateForm(forms.ModelForm):

    class Meta:
        model = PodKonto
        fields = (
            'oznaka',
            'naziv',
            'zap_st',
            'skupina',
        )


class SkupinaVrsteStroskaCreateForm(forms.ModelForm):

    class Meta:
        model = SkupinaVrsteStroska
        fields = (
            'oznaka',
            'naziv',
            'zap_st',
            'skupina',
        )


class VrstaStroskaCreateForm(forms.ModelForm):

    class Meta:
        model = VrstaStroska
        fields = (
            'oznaka',
            'naziv',
            'zap_st',
            'skupina',
        )
