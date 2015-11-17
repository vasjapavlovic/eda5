from django import forms
from django.utils import timezone

from .models import Zahtevek, ZahtevekSkodniDogodek, ZahtevekSestanek, ZahtevekIzvedbaDela

from eda5.posta.models import Dokument


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

    def clean_oznaka(self):
        # poskrbimo, post ne more povoziti OZNAKO, ki je readonly
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
            'dokument_prijava_skode',
            'dokument_zapisnik_ogleda',
            'dokument_poravnava',
            'dokazno_gradivo',
            'datum_nastanka_skode',
            'vzrok_skode',
            'is_prijava_policiji',
            'povzrocitelj',
            'predvidena_visina_skode',
            'poskodovane_stvari',
        )
        widgets = {"poskodovane_stvari": forms.CheckboxSelectMultiple}


class ZahtevekSestanekUpdateForm(forms.ModelForm):

    class Meta:
        model = ZahtevekSestanek
        fields = (
            'sklicatelj',
            'zapisnik',
            'datum',
            'udelezenci',
        )
        widgets = {"udelezenci": forms.CheckboxSelectMultiple}


class ZahtevekIzvedbaDelUpdateForm(forms.ModelForm):

    class Meta:
        model = ZahtevekIzvedbaDela
        fields = (
            'is_zakonska_obveza',
        )
