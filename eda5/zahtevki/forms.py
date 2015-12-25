from functools import partial

from django import forms
from django.utils import timezone

from .models import Zahtevek, ZahtevekSkodniDogodek, ZahtevekSestanek, ZahtevekIzvedbaDela
from eda5.narocila.models import Narocilo

DateInput = partial(forms.DateInput, {'class': 'datepicker'})
TimeInput = partial(forms.TimeInput, {'class': 'timepicker'})


class ZahtevekCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super(ZahtevekCreateForm, self).__init__(*args, **kwargs)
        # custom initial properties
        # OZNAKA - tuki je napisano z namen, ker je form uporabljen na dveh različnih mestih
        leto = timezone.now().date().year
        zap_st = Zahtevek.objects.all().count()
        zap_st = zap_st + 1
        nova_oznaka = "ZHT-%s-%s" % (leto, zap_st)
        self.initial['oznaka'] = nova_oznaka
        self.fields['oznaka'].widget.attrs['readonly'] = True

        # prikažemo samo veljavna naročila
        self.fields['narocilo'].queryset = Narocilo.objects.veljavna()

    def clean_oznaka(self):
        # poskrbimo: post ne more povoziti OZNAKO, ki je readonly
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.oznaka
        else:
            return self.cleaned_data['oznaka']

    class Meta:
        model = Zahtevek
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


class PodzahtevekCreateForm(ZahtevekCreateForm):

    class Meta(ZahtevekCreateForm.Meta):

        # brez "narocilo" --> ni potrebno saj je naročilo enako zahtevek_parent
        fields = (
            'oznaka',
            'naziv',
            'vrsta',
            'rok_izvedbe',
            'nosilec',
        )


class ZahtevekUpdateForm(ZahtevekCreateForm):

    class Meta(ZahtevekCreateForm.Meta):
        widgets = {
            'vrsta': forms.HiddenInput(),
            'narocilo': forms.HiddenInput(),
        }


class ZahtevekSkodniDogodekUpdateForm(forms.ModelForm):

    class Meta:
        model = ZahtevekSkodniDogodek
        fields = (
            'datum_nastanka_skode',
            'vzrok_skode',
            'is_prijava_policiji',
            'povzrocitelj',
            'predvidena_visina_skode',
            'poskodovane_stvari',
        )
        widgets = {"poskodovane_stvari": forms.CheckboxSelectMultiple}


class ZahtevekSestanekCreateForm(forms.ModelForm):

    class Meta:
        model = ZahtevekSestanek
        fields = (
            'datum',
            'sklicatelj',
            'udelezenci',
        )
        widgets = {
            "datum": DateInput(),
        }


class ZahtevekSestanekUpdateForm(forms.ModelForm):

    class Meta:
        model = ZahtevekSestanek
        fields = (
            'sklicatelj',
            'datum',
            'udelezenci',
        )
        widgets = {
            "datum": DateInput(),
        }


class ZahtevekIzvedbaDelCreateForm(forms.ModelForm):

    class Meta:
        model = ZahtevekIzvedbaDela
        fields = (
            'is_zakonska_obveza',
        )


class ZahtevekIzvedbaDelUpdateForm(forms.ModelForm):

    class Meta:
        model = ZahtevekIzvedbaDela
        fields = (
            'is_zakonska_obveza',
        )


class ZahtevekIzbiraForm(forms.Form):

    VRSTE = (
        (1, 'Sestanek'),
        (2, 'Izvedba Del')
    )

    vrsta_zahtevka = forms.ChoiceField(choices=VRSTE)
