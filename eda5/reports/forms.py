# Python
from functools import partial
# Django
from django import forms
from django.utils.html import conditional_escape, mark_safe
from django.utils.encoding import smart_text

# Models
from eda5.core.models import ObdobjeLeto, ObdobjeMesec
from eda5.delovninalogi.models import Delo
from eda5.etaznalastnina.models import Program
from eda5.narocila.models import Narocilo
from eda5.partnerji.models import Oseba
from eda5.planiranje.models import Plan
from eda5.racunovodstvo.models import SkupinaVrsteStroska, VrstaStroska

# Forms
from eda5.racunovodstvo.forms.vrsta_stroska_forms import VrstaStroskaIzbiraForm



# widgets
from django.contrib.admin.sites import site
from eda5.partnerji.widgets import OsebaForeignKeyRawIdWidget

DateInput = partial(forms.DateInput, {'class': 'datepicker'})
TimeInput = partial(forms.TimeInput, {'class': 'timepicker'})


# Forms


class ReportForm(forms.Form):

    q = forms.ModelMultipleChoiceField(
        queryset=SkupinaVrsteStroska.objects.filter(skupina__skupina__oznaka="O"),
        widget=forms.CheckboxSelectMultiple,
    )


class UporabimFilterForm(forms.Form):
    uporabim_filter = forms.BooleanField(label='Uporabi filter')


class FormatForm(forms.Form):
    FORMAT_CHOICES = (
        ('pdf', 'PDF'),
        ('docx', 'MS Word'),
        ('html', 'HTML'),
        ('xlsx', 'MS Excel'),
    )

    format_field = forms.ChoiceField(choices=FORMAT_CHOICES)


class LetoIzbiraForm(forms.Form):

    obdobje_leto = forms.ModelChoiceField(
        queryset=ObdobjeLeto.objects.all(), required=False)


class MesecIzbiraForm(forms.Form):

    obdobje_mesec = forms.ModelChoiceField(
        queryset=ObdobjeMesec.objects.all(), required=False)



class ObdobjeDatumForm(forms.Form):
    datum_od = forms.DateField(required=False)
    datum_do = forms.DateField(required=False)


class DeliSeznamFilterForm(forms.Form):

    program = forms.ModelMultipleChoiceField(
        queryset=Program.objects.all())


# DELOVNI NALOG FORMS
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


# LETNO POROČILO UPRAVNIKA
class LetnoPorociloUpravnikaStroskiIzpisIzbiraForm(forms.Form):
    IZBIRE = (
        (1, "Seznam stroškov"),
        (2, "Skupine stroškov"),
        (3, "Vrste stroškov"),
    )
    izpis_izbira = forms.ChoiceField(choices=IZBIRE)


class PlanIzbiraForm(forms.Form):


    plan_list = Plan.objects.filter()

    izbrani_plan = forms.ModelChoiceField(
        queryset=plan_list)


class IzvedenaDelaIzpisIzbiraForm(forms.Form):
    IZBIRE = (
        (0, "----"),
        (1, "Izvedena opravila po planih obratovanja in vzdrževanja"),
        (2, "Izredna opravila"),
        (3, "Izredna opravila zunanji"),
    )

    izpis_izbira = forms.ChoiceField(choices=IZBIRE, required=False)


class DogodekFilterForm(forms.Form):

    zavarovani_dogodki = forms.BooleanField(label='Prikaži samo zavarovane dogodke', required=False)
    nezavarovani_dogodki = forms.BooleanField(label='Prikaži nezavarovane dogodke', required=False)


class DogodkiIzpisIzbiraForm(forms.Form):
    IZBIRE = (
        (0, "----"),
        (1, "Zavarovani dogodki"),
        (2, "Pomembni dogodki"),

    )

    izpis_izbira = forms.ChoiceField(choices=IZBIRE, required=False)


class DelavecIzbiraForm(forms.Form):

    delavec = forms.ModelChoiceField(
        queryset=Oseba.objects.filter(),
        required=False,
        widget=OsebaForeignKeyRawIdWidget(Delo._meta.get_field('delavec').rel, site),
        )


class NarociloSelectForm(forms.Form):

    narocilo = forms.ModelChoiceField(
        queryset=Narocilo.objects.filter(), required=False)


class VrstaStroskaIzbiraForm(VrstaStroskaIzbiraForm):

    def __init__(self, *args, **kwargs):
        super(VrstaStroskaIzbiraForm, self).__init__(*args, **kwargs)

        # filter
        #self.fields['konto_hidden'].required = False
        self.fields['konto'].required = False
        self.fields['podkonto'].required = False
        self.fields['skupina_vrste_stroska'].required = False
        self.fields['vrsta_stroska'].required = False
