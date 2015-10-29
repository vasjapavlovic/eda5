from django import forms

from .models import Racun, DavcnaKlasifikacija
from eda5.core.models import ObdobjeLeto, ObdobjeMesec


class RacunCreateForm(forms.ModelForm):

    class Meta:
        model = Racun
        fields = (
            "dokument",
            "davcna_klasifikacija",
            "datum_storitve_od",
            "datum_storitve_do",
            "obdobje_obracuna_leto",
            "obdobje_obracuna_mesec",
            )


class RacunAddWidget(forms.Form):

    OBDOBJE_LETO = ObdobjeLeto.objects.all()
    OBDOBJE_MESEC = ObdobjeMesec.objects.all()
    DAVCNA_KLASIFIKACIJA = DavcnaKlasifikacija.objects.all()

    davcna_klasifikacija = forms.ModelChoiceField(queryset=DAVCNA_KLASIFIKACIJA)
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