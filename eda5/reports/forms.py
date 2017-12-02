# Python
from functools import partial
# Django
from django import forms
from django.utils.html import conditional_escape, mark_safe
from django.utils.encoding import smart_text

# Models
from eda5.core.models import ObdobjeLeto, ObdobjeMesec
from eda5.etaznalastnina.models import Program
from eda5.narocila.models import Narocilo
from eda5.racunovodstvo.models import SkupinaVrsteStroska, VrstaStroska

DateInput = partial(forms.DateInput, {'class': 'datepicker'})
TimeInput = partial(forms.TimeInput, {'class': 'timepicker'})


# Forms




class ReportForm(forms.Form):

    q = forms.ModelMultipleChoiceField(
        queryset=SkupinaVrsteStroska.objects.filter(skupina__skupina__oznaka="O"),
        widget=forms.CheckboxSelectMultiple,
    )


class FormatForm(forms.Form):
    FORMAT_CHOICES = (
        ('pdf', 'PDF'),
        ('docx', 'MS Word'),
        ('html', 'HTML'),
        ('xlsx', 'MS Excel'),
    )

    format_field = forms.ChoiceField(choices=FORMAT_CHOICES)


class DeliSeznamFilterForm(forms.Form):

    program = forms.ModelMultipleChoiceField(
        queryset=Program.objects.all())


class ObracunFilterForm(forms.Form):

    obdobje_leto = forms.ModelChoiceField(
        queryset=ObdobjeLeto.objects.all())

    obdobje_mesec = forms.ModelChoiceField(
        queryset=ObdobjeMesec.objects.all())


class ObracunIzrednaDelaForm(forms.Form):

    # začetne nastavitve prikazanega "form"
    def __init__(self, *args, **kwargs):
        super(ObracunIzrednaDelaForm, self).__init__(*args, **kwargs)
        # na začetku so okenca za vnos filtrov prazna
        self.initial['datum_od'] = ""
        self.initial['datum_do'] = ""
        self.initial['vrsta_stroska'] = ""
        self.initial['prikazi_izpis_del'] = False
        self.initial['prikazi_izpis_dn'] = False

    datum_od = forms.DateField(label='datum od', required=False)
    datum_do = forms.DateField(label='datum do', required=False)

    narocilo = forms.ModelChoiceField(
        queryset=Narocilo.objects.veljavna())

    vrsta_stroska = forms.ModelChoiceField(
        queryset=VrstaStroska.objects.filter(skupina__skupina__skupina__oznaka="O"))


    prikazi_izpis_del = forms.BooleanField(label='Prikaži izpis del', required=False)
    prikazi_izpis_dn = forms.BooleanField(label='Prikaži izpis delovnih nalogov', required=False)



class ObracunIzpisVrstaForm(forms.Form):
    VRSTA_IZPISA_CHOICES = (
        ('neplanirano', 'Neplanirano - Izpis'),
        ('planirano', 'Planirano - Izpis'),
        ('neplanirano_delitev', 'Neplanirano - Delitev'),
        ('planirano_delitev', 'Planirano - Delitev'),
    )

    vrsta_izpisa_field = forms.ChoiceField(choices=VRSTA_IZPISA_CHOICES)
