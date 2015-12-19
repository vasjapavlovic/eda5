from functools import partial

from django import forms
from django.utils import timezone

from .models import Zahtevek, ZahtevekSkodniDogodek, ZahtevekSestanek, ZahtevekIzvedbaDela
from eda5.narocila.models import Narocilo

DateInput = partial(forms.DateInput, {'class': 'datepicker'})
TimeInput = partial(forms.TimeInput, {'class': 'timepicker'})


class ZahtevekCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        zahtevek_parent = kwargs.pop('zahtevek', None)
        print(zahtevek_parent)

        super(ZahtevekCreateForm, self).__init__(*args, **kwargs)
        # custom initial properties
        # OZNAKA - tuki je napisano z namen, ker je form uporabljen na dveh različnih mestih
        leto = timezone.now().date().year
        zap_st = Zahtevek.objects.all().count()
        zap_st = zap_st + 1
        nova_oznaka = "ZHT-%s-%s" % (leto, zap_st)
        self.initial['oznaka'] = nova_oznaka
        self.fields['oznaka'].widget.attrs['readonly'] = True

        if zahtevek_parent:
            self.initial['zahtevek_parent'] = zahtevek_parent.pk
            print("PARENT ID: ", zahtevek_parent.pk, zahtevek_parent)

        else:
            print("NI PARENT ID-ja")
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
            'vrsta',
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
            "udelezenci": forms.CheckboxSelectMultiple,
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
            "udelezenci": forms.CheckboxSelectMultiple,
            "datum": DateInput(),
        }


class ZahtevekIzvedbaDelaCreateForm(forms.ModelForm):

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


class ZahtevekIzvedbaDelaCreateForm(forms.ModelForm):

    class Meta:
        model = ZahtevekIzvedbaDela
        fields = (
            'is_zakonska_obveza',
        )


class PodzahtevekForm(forms.Form):

    VRSTE = (
        (1, 'sestanek'),
        (2, 'izvedba_del')
    )


    vrsta_zahtevka = forms.ChoiceField(choices=VRSTE)
