from functools import partial
from django.template.loader import render_to_string

from django import forms
from django.contrib.admin.sites import site
from django.utils import timezone

from .models import Zahtevek, ZahtevekSkodniDogodek, ZahtevekSestanek, ZahtevekIzvedbaDela
from .models import ZahtevekAnaliza, ZahtevekPovprasevanje, ZahtevekReklamacija

# Partnerji
from eda5.partnerji.models import Oseba, SkupinaPartnerjev
from eda5.partnerji.widgets import PartnerForeignKeyRawIdWidget, OsebaForeignKeyRawIdWidget

DateInput = partial(forms.DateInput, {'class': 'datepicker'})
TimeInput = partial(forms.TimeInput, {'class': 'timepicker'})


class ZahtevekCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super(ZahtevekCreateForm, self).__init__(*args, **kwargs)
        # custom initial properties
        # OZNAKA - tuki je napisano z namenom, ker je form uporabljen na dveh različnih mestih
        try:
            zap_st = Zahtevek.objects.all().count()
            zap_st = zap_st + 1
        except:
            zap_st = 1

        leto = timezone.now().date().year
        nova_oznaka = "ZHT-%s-%s" % (leto, zap_st)
        self.initial['oznaka'] = nova_oznaka
        self.fields['oznaka'].widget.attrs['readonly'] = True

        # filtriranje dropdown
        self.fields['oseba_hidden'].required = False
        self.fields['skupina_partnerjev_hidden'].required = False


    def clean_oznaka(self):
        # poskrbimo: post ne more povoziti OZNAKO, ki je readonly
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.oznaka
        else:
            return self.cleaned_data['oznaka']

    # zaradi filtriranja "oseba"
    oseba_hidden = forms.ModelChoiceField(queryset=Oseba.objects.all())
    skupina_partnerjev_hidden = forms.ModelChoiceField(queryset=SkupinaPartnerjev.objects.all())

    class Meta:
        model = Zahtevek
        fields = (
            'oznaka',
            'naziv',
            'rok_izvedbe',
            'nosilec',
        )
        widgets = {
            'rok_izvedbe': DateInput(),
            'nosilec': OsebaForeignKeyRawIdWidget(model._meta.get_field('nosilec').rel, site),
        }


class PodzahtevekCreateForm(ZahtevekCreateForm):

    class Meta(ZahtevekCreateForm.Meta):

        model = Zahtevek
        fields = (
            'oznaka',
            'naziv',
            'vrsta',
            'rok_izvedbe',
            'nosilec',
        )
        widgets = {
            'rok_izvedbe': DateInput(),
            'nosilec': OsebaForeignKeyRawIdWidget(model._meta.get_field('nosilec').rel, site),
        }


class ZahtevekUpdateForm(forms.ModelForm):

    class Meta:
        model = Zahtevek
        fields = (
            'naziv',
            'vrsta',
            'rok_izvedbe',
            'nosilec',
            'status',
        )
        widgets = {
            'rok_izvedbe': DateInput(),
            'nosilec': OsebaForeignKeyRawIdWidget(model._meta.get_field('nosilec').rel, site),
        }


class ZahtevekIzbiraForm(forms.Form):

    VRSTE = (
        (1, 'Škodni Dogodek'),
        (2, 'Sestanek'),
        (3, 'Izvedba del'),
        (4, 'Predaja Lastnine'),
        (5, 'Analiza Zahtevka'),
        (6, 'Povpraševanje'),
        (7, 'Reklamacija'),
    )

    vrsta_zahtevka = forms.ChoiceField(choices=VRSTE)


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
            'sklicatelj': OsebaForeignKeyRawIdWidget(model._meta.get_field('sklicatelj').rel, site),
            'udelezenci': OsebaForeignKeyRawIdWidget(model._meta.get_field('udelezenci').rel, site),
        }


class ZahtevekSestanekUpdateForm(ZahtevekSestanekCreateForm):
    # enako "form" ZahtevekSestanekCreateForm
    pass


class ZahtevekIzvedbaDelCreateForm(forms.ModelForm):

    class Meta:
        model = ZahtevekIzvedbaDela
        fields = (
            'is_zakonska_obveza',
        )


class ZahtevekIzvedbaDelUpdateForm(ZahtevekIzvedbaDelCreateForm):
    # enako "form" ZahtevekSestanekCreateForm
    pass
