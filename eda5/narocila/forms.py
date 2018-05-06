from functools import partial

from django import forms
from django.contrib.admin.sites import site
from django.db.models import Q
from django.utils import timezone


# Naročila
from .models import Narocilo, NarociloTelefon, NarociloDokument



# Arhiv
from eda5.arhiv.models import Arhiviranje

# Partnerji
from eda5.partnerji.models import Oseba
from eda5.partnerji.widgets import PartnerForeignKeyRawIdWidget, OsebaForeignKeyRawIdWidget

# Pošta
from eda5.posta.models import VrstaDokumenta

# Zahtevki
from eda5.zahtevki.models import Zahtevek


DateInput = partial(forms.DateInput, {'class': 'datepicker'})
TimeInput = partial(forms.TimeInput, {'class': 'timepicker'})



class NarociloCreateIzbiraForm(forms.Form):
    CHOICES = (
        (1, 'naročilo telefon'),
        (2, 'naročilo dokument'),
    )

    vrsta_narocila = forms.ChoiceField(choices=CHOICES)


class NarociloSplosnoCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(NarociloSplosnoCreateForm, self).__init__(*args, **kwargs)

        # Dodelitev številke naročila
        predoznaka = "NRC"
        leto = timezone.now().date().year
        zap_st = Narocilo.objects.all().count() + 1

        nova_oznaka = "%s-%s-%s" % (predoznaka, leto, zap_st)
        self.initial['oznaka'] = nova_oznaka
        # avtomatsko dodeljena oznaka = ReadOnly
        self.fields['oznaka'].widget.attrs['readonly'] = True

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
        model = Narocilo
        fields = [
            'oznaka',
            'predmet',
            'narocnik',
            'izvajalec',
            'datum_narocila',
            'datum_veljavnosti',
            'vrednost',
        ]
        widgets = {
            'datum_narocila': DateInput(),
            'datum_veljavnosti': DateInput(),
            'narocnik': PartnerForeignKeyRawIdWidget(model._meta.get_field('narocnik').rel, site),
            'izvajalec': PartnerForeignKeyRawIdWidget(model._meta.get_field('izvajalec').rel, site),
        }


class NarociloTelefonCreateForm(forms.ModelForm):

    class Meta:
        model = NarociloTelefon
        fields = [
            'dogovor_text',
            'dogovor_date',
            'dogovor_time',
            'dogovor_person',
            'dogovor_phonenumber',
        ]
        widgets = {
            'dogovor_date': DateInput(),
            'dogovor_time': TimeInput(),
        }


class NarociloDokumentCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(NarociloDokumentCreateForm, self).__init__(*args, **kwargs)

        self.fields['vrsta_dokumenta'].queryset = VrstaDokumenta.objects.filter(
            # pogodba ali
            Q(oznaka="PGD") |
            # naročilnica
            Q(oznaka="NRC")
        )

    class Meta:
        model = NarociloDokument
        fields = [
            'vrsta_dokumenta',
        ]


class NarociloDokumentUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super(NarociloDokumentUpdateForm, self).__init__(*args, **kwargs)

        ''' Pri izbiri dokumenta prikažemo samo pogodbe in naročilnice '''
        self.fields['dokument'].queryset = Arhiviranje.objects.filter(

        Q(zahtevek=self.instance.narocilo.zahtevek) &
            (
                Q(dokument__vrsta_dokumenta__oznaka="PGD") |
                Q(dokument__vrsta_dokumenta__oznaka="NRC")
            )
        )

    class Meta:
        model = NarociloDokument
        fields = [
            'dokument',
        ]


class NarociloSelectForm(forms.Form):

    narocilo = forms.ModelChoiceField(
        queryset=Narocilo.objects.filter(), required=False)
