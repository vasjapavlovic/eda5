# Python
from functools import partial

# Django
from django import forms
from django.contrib.admin.sites import site
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.db.models import Q
from django.template.loader import render_to_string
from django.utils import timezone

# Models
from .models import Zahtevek, ZahtevekSkodniDogodek, ZahtevekSestanek, ZahtevekIzvedbaDela
from .models import ZahtevekAnaliza, ZahtevekPovprasevanje, ZahtevekReklamacija
from eda5.partnerji.models import Oseba, SkupinaPartnerjev

# Forms

# Widgets
from .widgets import ZahtevekForeignKeyRawIdWidget, ZahtevekManyToManyRawIdWidget
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
        self.fields['nosilec'].widget.attrs['readonly'] = True

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

    def clean_nosilec(self):
        # poskrbimo: post ne more povoziti OZNAKO, ki je readonly
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.nosilec
        else:
            return self.cleaned_data['nosilec']

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

    def __init__(self, *args, **kwargs):

        super(ZahtevekUpdateForm, self).__init__(*args, **kwargs)
        # custom initial properties

        self.fields['nosilec'].widget.attrs['readonly'] = True


    class Meta:
        model = Zahtevek
        fields = (
            'naziv',
            'vrsta',
            'rok_izvedbe',
            'nosilec',
            'status',
            'zahtevek_parent',
            'zahtevek_povezava',
        )
        widgets = {
            'rok_izvedbe': DateInput(),
            'nosilec': OsebaForeignKeyRawIdWidget(model._meta.get_field('nosilec').rel, site),
            'zahtevek_parent': ZahtevekForeignKeyRawIdWidget(model._meta.get_field('zahtevek_parent').rel, site),
            'zahtevek_povezava': ZahtevekManyToManyRawIdWidget(model._meta.get_field('zahtevek_povezava').rel, site),
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



# SEARCH FORMS

class ZahtevekSearchForm(forms.Form):
    oznaka = forms.CharField(label='oznaka', required=False)
    naziv = forms.CharField(label='naziv', required=False)

    # začetne nastavitve prikazanega "form"
    def __init__(self, *args, **kwargs):
        super(ZahtevekSearchForm, self).__init__(*args, **kwargs)
        # na začetku so okenca za vnos filtrov prazna
        self.initial['oznaka'] = ""
        self.initial['naziv'] = ""


    def filter_queryset(self, request, queryset):

        oznaka_filter = self.cleaned_data['oznaka']
        naziv_filter = self.cleaned_data['naziv']

        # filtriranje samo po oznaki
        if oznaka_filter and not naziv_filter:
            return queryset.filter(
                Q(oznaka__icontains=oznaka_filter)
            )

        # filtriranje ostalo
        if naziv_filter and not oznaka_filter:
            return queryset.filter(
                Q(naziv__icontains=naziv_filter)
            )
        

        # uporabnik filtrira po kratkem imenu in naslovu partnerja
        if oznaka_filter and naziv_filter:
            return queryset.filter(
                Q(oznaka__icontains=oznaka_filter) &
                Q(naziv__icontains=naziv_filter)
            )

        return queryset