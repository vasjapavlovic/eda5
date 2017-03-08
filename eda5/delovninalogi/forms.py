from functools import partial

from django.template.loader import render_to_string
from django.contrib.admin.sites import site

from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.utils import timezone
from django.core.exceptions import ValidationError

from .models import Opravilo, DelovniNalog, Delo, DeloVrsta, DeloVrstaSklop, VzorecOpravila

from eda5.deli.models import Element, ProjektnoMesto
from eda5.narocila.models import Narocilo
from eda5.partnerji.models import Oseba
from eda5.posta.models import Dokument


from eda5.planiranje.models import SkupinaPlanov, Plan, PlaniranoOpravilo


from eda5.deli.widgets import ProjektnoMestoSelectWithPop, ProjektnoMestoMultipleSelectWithPop, ProjektnoMestoForeignKeyRawIdWidget, ProjektnoMestoManyToManyRawIdWidget

DateInput = partial(forms.DateInput, {'class': 'datepicker'})
TimeInput = partial(forms.TimeInput, {'class': 'timepicker'})





class OpraviloCreateForm(forms.ModelForm):

    ''' *** Opravila se izdelajo samo pod zahtevkih *** '''

    def __init__(self, *args, **kwargs):
        super(OpraviloCreateForm, self).__init__(*args, **kwargs)
        # custom initial properties

        try:
            leto = timezone.now().date().year
            zap_st = Opravilo.objects.all().count()
            zap_st = zap_st + 1
        except:
            zap_st = 1


        nova_oznaka = "OPR-%s-%s" % (leto, zap_st)  #

        self.initial['oznaka'] = nova_oznaka

        # avtomatsko dodeljena oznaka = ReadOnly
        self.fields['oznaka'].widget.attrs['readonly'] = True

        # querysets
        self.fields["narocilo"].queryset = Narocilo.objects.all().order_by('-id')

        # filtriranje dropdown
        self.fields['oseba_hidden'].required = False

    # post ne more povozit okence ki je readonly
    def clean_oznaka(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.oznaka
        else:
            return self.cleaned_data['oznaka']

    # zaradi filtriranja "oseba"
    oseba_hidden = forms.ModelChoiceField(queryset=Oseba.objects.all())


    class Meta:
        model = Opravilo
        fields = (
            'oznaka',
            'naziv',
            'rok_izvedbe',
            'narocilo',
            'nosilec',
            'planirano_opravilo',
        )
        widgets = {
            'rok_izvedbe': DateInput(),
        }



class VzorecOpravilaIzbiraForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(VzorecOpravilaIzbiraForm, self).__init__(*args, **kwargs)

        # filtriranje dropdown
        self.fields['plan_hidden'].required = False
        self.fields['planirano_opravilo_hidden'].required = False
        self.fields['vzorec_opravila_hidden'].required = False

        self.fields['skupina_planov'].required = False
        self.fields['plan'].required = False
        self.fields['planirano_opravilo'].required = False

    skupina_planov = forms.ModelChoiceField(queryset=SkupinaPlanov.objects.all())
    plan = forms.ModelChoiceField(queryset=Plan.objects.all())
    planirano_opravilo = forms.ModelChoiceField(queryset=PlaniranoOpravilo.objects.all())
    vzorec_opravila = forms.ModelChoiceField(queryset=VzorecOpravila.objects.all())

    # za filtriranje
    plan_hidden = forms.ModelChoiceField(queryset=Plan.objects.all())
    planirano_opravilo_hidden = forms.ModelChoiceField(queryset=PlaniranoOpravilo.objects.all())
    vzorec_opravila_hidden = forms.ModelChoiceField(queryset=VzorecOpravila.objects.all())


class VzorecOpravilaCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(VzorecOpravilaCreateForm, self).__init__(*args, **kwargs)
        # custom initial properties

        try:
            zap_st = VzorecOpravila.objects.all().count()
            zap_st = zap_st + 1
        except:
            zap_st = 1

        nova_oznaka = "OPR-VZOREC-%s" % (zap_st)  #

        self.initial['oznaka'] = nova_oznaka

        # avtomatsko dodeljena oznaka = ReadOnly
        self.fields['oznaka'].widget.attrs['readonly'] = True

        # querysets
        self.fields["narocilo"].queryset = Narocilo.objects.all()
        self.fields["nosilec"].queryset = Oseba.objects.all()

        # filtriranje dropdown
        self.fields['oseba_hidden'].required = False

    # post ne more povozit okence ki je readonly
    def clean_oznaka(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.oznaka
        else:
            return self.cleaned_data['oznaka']

    # zaradi filtriranja "oseba"
    oseba_hidden = forms.ModelChoiceField(queryset=Oseba.objects.all())

    class Meta:
        model = Opravilo
        fields = (
            'oznaka',
            'naziv',
            'rok_izvedbe',
            'narocilo',
            'nosilec',
        )
        widgets = {
            'rok_izvedbe': DateInput(),
        }




class OpraviloUpdateForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
        # super(OpraviloUpdateForm, self).__init__(*args, **kwargs)
        # self.fields['element'].queryset = ProjektnoMesto.objects.filter(is_active=True)

    class Meta:
        model = Opravilo
        fields = (
            'narocilo',
            'element',
            'oznaka',
            'naziv',
            'rok_izvedbe',
            )
        widgets = {
            'rok_izvedbe': DateInput(),
        }

''' Ko je opravilo izdelano ga posodobimo tako, da mu
dodelimo še na katerih elementih se izvaja'''

class OpraviloElementUpdateForm(OpraviloUpdateForm):

    class Meta:
        model = Opravilo
        fields = (
            'element',
        )
        widgets = {
            'element': ProjektnoMestoManyToManyRawIdWidget(model._meta.get_field('element').rel, site),
        }


                    



''' Ko je opravilo izdelano ga posodobimo tako, da mu
dodelimo še katere pomanjkljivosti se v opravilu 
odpravljajo '''

class OpraviloPomanjkljivostUpdateForm(OpraviloUpdateForm):

    class Meta:
        model = Opravilo
        fields = (
            'pomanjkljivost',
        )





class DelovniNalogVcakanjuModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(DelovniNalogVcakanjuModelForm, self).__init__(*args, **kwargs)
        # custom initial properties
        self.initial['status'] = 2
        self.fields['datum_plan'].required = True
        self.fields['nosilec'].required = True

        # filtriranje dropdown
        self.fields['oseba_hidden'].required = False

    # zaradi filtriranja "oseba"
    oseba_hidden = forms.ModelChoiceField(queryset=Oseba.objects.all())

    class Meta:
        model = DelovniNalog
        fields = (
            'status',
            'datum_plan',
            'nosilec',
            )
        widgets = {
            'status': forms.HiddenInput(),
            'datum_plan': DateInput(),
        }


class DelovniNalogVplanuModelForm(forms.ModelForm):

    class Meta:
        model = DelovniNalog
        fields = (
            'status',
            )
        widgets = {
            'status': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        super(DelovniNalogVplanuModelForm, self).__init__(*args, **kwargs)
        # custom initial properties
        self.initial['status'] = 3


class DelovniNalogVresevanjuModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(DelovniNalogVresevanjuModelForm, self).__init__(*args, **kwargs)
        # custom initial properties
        self.initial['status'] = 4
        self.initial['datum_stop'] = timezone.now().date()

        ''' validiraj Dokler so odprta dela, delovnega naloga ne moreš končati'''

    class Meta:
        model = DelovniNalog
        fields = (
            'status',
            'datum_stop',
            )
        widgets = {
            'status': forms.HiddenInput(),
            'datum_stop': forms.TextInput(attrs={'readonly': 'True'},),
            'datum_stop': DateInput(),
            }


class DeloCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(DeloCreateForm, self).__init__(*args, **kwargs)

        ''' Avtomatska oznaka dela. Oznaka = Zaporedna številka '''

        try:
            zap_st = Delo.objects.all().count()
            zap_st = zap_st + 1
        except:
            zap_st = 1

        oznaka = zap_st
        self.initial['oznaka'] = oznaka
        self.fields['oznaka'].widget.attrs['readonly'] = True


        ''' Avtomatska dodelitev trenutnega datuma in časa začetka
        izvajanja dela. '''

        datum = timezone.now().date()
        time_start = timezone.localtime(timezone.now()).time().strftime("%H:%M:%S")

        self.initial['datum'] = datum
        self.fields['datum'].widget.attrs['readonly'] = True

        self.initial['time_start'] = time_start
        self.fields['time_start'].widget.attrs['readonly'] = True


    def clean_oznaka(self):
        """ poskrbimo: post ne more povoziti OZNAKO, ki je readonly """
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.oznaka
        else:
            return self.cleaned_data['oznaka']        

    def clean_datum(self):
        """ poskrbimo: post ne more povoziti datuma, ki je readonly """
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.datum
        else:
            return self.cleaned_data['datum']

    def clean_time_start(self):
        """ poskrbimo: post ne more povoziti datuma, ki je readonly """
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.time_start
        else:
            return self.cleaned_data['time_start']


    class Meta:
        model = Delo
        fields = (
            'oznaka',
            'naziv',
            'delavec',
            'vrsta_dela',
            'datum',
            'time_start',
        )


class DeloKoncajUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(DeloKoncajUpdateForm, self).__init__(*args, **kwargs)
        # custom initial properties
        self.initial['time_stop'] = timezone.localtime(timezone.now()).time().strftime("%H:%M:%S")
        # uredimo, da je time_stop readonly
        self.fields['time_stop'].widget.attrs['readonly'] = True

    class Meta:
        model = Delo
        fields = ('time_stop',)
        widgets = {
            'time_stop': TimeInput()
        }

class DeloUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(DeloUpdateForm, self).__init__(*args, **kwargs)

        # oznake dela ni mogoče spreminjati
        self.fields['oznaka'].widget.attrs['readonly'] = True

    class Meta:
        model = Delo
        fields = (
            'oznaka',
            'datum',
            'vrsta_dela',
            'delavec',
            'time_start',
            'time_stop',
        )
        widgets = {
            'datum': DateInput(),
            'time_start': TimeInput(),
            'time_stop': TimeInput()
        }


class DeloVrstaSklopCreateForm(forms.ModelForm):

    class Meta:
        model = DeloVrstaSklop
        fields = (
            'oznaka',
            'naziv',
            'zap_st',
        )


class DeloVrstaCreateForm(forms.ModelForm):

    class Meta:
        model = DeloVrsta
        fields = (
            'oznaka',
            'naziv',
            'zap_st',
            'cena',
            'stopnja_ddv',
            'skupina',
        )

