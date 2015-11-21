from django import forms
from django.utils import timezone
from django.core.exceptions import ValidationError

from .models import Opravilo, DelovniNalog, Delo, DeloVrsta

from eda5.deli.models import Element
from eda5.narocila.models import Narocilo
from eda5.partnerji.models import Oseba
from eda5.posta.models import Dokument


class OpraviloForm(forms.Form):

    # querysets
    NAROCILA = Narocilo.objects.all()
    ELEMENTI = Element.objects.all()
    OSEBE = Oseba.objects.all()

    # FORM
    # **onovno
    oznaka = forms.CharField()
    naziv = forms.CharField()
    rok_izvedbe = forms.DateField()
    # **relacije
    narocilo = forms.ModelChoiceField(queryset=NAROCILA)
    nadzornik = forms.ModelChoiceField(queryset=OSEBE)
    # element = forms.ModelMultipleChoiceField(queryset=ELEMENTI)

class OpraviloCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(OpraviloCreateForm, self).__init__(*args, **kwargs)
        # custom initial properties

        leto = timezone.now().date().year
        zap_st = Opravilo.objects.all().count()
        zap_st = zap_st + 1

        nova_oznaka = "OPR-%s-%s" % (leto, zap_st)  #

        self.initial['oznaka'] = nova_oznaka

        #querysets
        self.fields["narocilo"].queryset = Narocilo.objects.all()
        self.fields["nadzornik"].queryset = Oseba.objects.all()

    class Meta:
        model = Opravilo
        fields = (
            'naziv',
            'rok_izvedbe',
            'narocilo',
            'nadzornik',
            'oznaka',
        )
        widgets = {'oznaka': forms.HiddenInput(),}



class OpraviloModelForm(forms.ModelForm):

    class Meta:
        model = Opravilo
        fields = (
            'narocilo',
            'element',
            'oznaka',
            'naziv',
            'rok_izvedbe',
            )


class DelovniNalogVcakanjuModelForm(forms.ModelForm):

    class Meta:
        model = DelovniNalog
        fields = (
            'status',
            'datum_plan',
            'nosilec',
            )
        widgets = {
            'status': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        super(DelovniNalogVcakanjuModelForm, self).__init__(*args, **kwargs)
        # custom initial properties
        self.initial['status'] = 2


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

    class Meta:
        model = DelovniNalog
        fields = (
            'status',
            'datum_stop',
            )
        widgets = {
            'status': forms.HiddenInput(),
            'datum_stop': forms.TextInput(attrs={'readonly':'True'})
            }

    def __init__(self, *args, **kwargs):
        super(DelovniNalogVresevanjuModelForm, self).__init__(*args, **kwargs)
        # custom initial properties
        self.initial['status'] = 4
        self.initial['datum_stop'] = timezone.now().date()


        ''' validiraj Dokler so odprta dela, delovnega naloga ne moreš končati'''



class DeloForm(forms.Form):

    DELAVCI = Oseba.objects.all()
    VRSTE_DEL = DeloVrsta.objects.all()

    delavec = forms.ModelChoiceField(queryset=DELAVCI)
    vrsta_dela = forms.ModelChoiceField(queryset=VRSTE_DEL)



class DeloZacetoUpdateModelForm(forms.ModelForm):

    class Meta:
        model = Delo
        fields = ('time_stop',)
        widgets = {'time_stop': forms.HiddenInput(),}

    def __init__(self, *args, **kwargs):
        super(DeloZacetoUpdateModelForm, self).__init__(*args, **kwargs)
        # custom initial properties
        self.initial['time_stop'] = timezone.now().time().strftime("%H:%M:%S")




# class DelovniNalogAddDokumentForm(forms.ModelForm):

#     class Meta:
#         model = DelovniNalog
#         fields = ("dokument",)
#         widgets = {"dokument": forms.CheckboxSelectMultiple}

#     def __init__(self, *args, **kwargs):
#         super(DelovniNalogAddDokumentForm, self).__init__(*args, **kwargs)

#         # vidni samo računi
#         vrsta_dokumenta = 1
#         self.fields["dokument"].queryset = Dokument.objects.filter(vrsta_dokumenta=vrsta_dokumenta)