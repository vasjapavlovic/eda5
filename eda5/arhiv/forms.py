from django import forms
from django.db.models import Q

from .models import Arhiviranje, ArhivMesto

from eda5.posta.models import Dokument, VrstaDokumenta, SkupinaDokumenta
from eda5.partnerji.models import Oseba



class ArhiviranjeCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super(ArhiviranjeCreateForm, self).__init__(*args, **kwargs)

        # 1. prikaži samo nearhivirane dokumente
        # 2. prikazati samo specifično vrsto dokumentov


        self.fields["dokument"].queryset = Dokument.objects.filter(arhiviranje__isnull=True)
        self.fields["dokument"].required = True

    class Meta:
        model = Arhiviranje
        fields = (
            'dokument',
            'arhiviral',
            'elektronski',
            'fizicni',
            'lokacija_hrambe',
        )


class ArhiviranjeZahtevekForm(ArhiviranjeCreateForm):

    def __init__(self, *args, **kwargs):
        super(ArhiviranjeZahtevekForm, self).__init__(*args, **kwargs)

        # 1. prikaži samo neračunovodske dokumente (skupni_dokumenta not "RAC")
        skupina_dokumenta = SkupinaDokumenta.objects.get(oznaka="RAC")
        self.fields["dokument"].queryset = Dokument.objects.filter(arhiviranje__isnull=True
                                                                   ).exclude(
                                                                   vrsta_dokumenta__skupina=skupina_dokumenta
                                                                   )

    class Meta(ArhiviranjeCreateForm.Meta):
        fields = (
            'dokument',
            'elektronski',
            'fizicni',
        )


class ArhiviranjeRacunForm(ArhiviranjeCreateForm):

    def __init__(self, *args, **kwargs):

        super(ArhiviranjeRacunForm, self).__init__(*args, **kwargs)

        # 1. prikaži samo dokumente z oznako = "RAC" (računi) in INR interni računi
        self.fields["dokument"].queryset = Dokument.objects.filter(
            Q(arhiviranje__isnull=True, vrsta_dokumenta__oznaka="RAC",) |
            Q(arhiviranje__isnull=True, vrsta_dokumenta__oznaka="INR",) |
            Q(arhiviranje__isnull=True, vrsta_dokumenta__oznaka="PRV",) |
            Q(arhiviranje__isnull=True, vrsta_dokumenta__oznaka="DBR",) |
            Q(arhiviranje__isnull=True, vrsta_dokumenta__oznaka="AVR",)
            )

    class Meta(ArhiviranjeCreateForm.Meta):
        fields = (
            'dokument',
        )


class ArhiviranjeDelovniNalogForm(ArhiviranjeCreateForm):

    class Meta(ArhiviranjeCreateForm.Meta):
        fields = (
            'delovninalog',
            'dokument',
            'elektronski',
            'fizicni',
        )
        widgets = {'delovninalog': forms.HiddenInput()}


class ArhiviranjeNarociloForm(ArhiviranjeCreateForm):

    def __init__(self, *args, **kwargs):

        super(ArhiviranjeNarociloForm, self).__init__(*args, **kwargs)

        # 1. prikaži samo dokumente z oznako = "RAC" (računi) in INR interni računi
        self.fields["dokument"].queryset = Dokument.objects.filter(
            Q(arhiviranje__isnull=True, vrsta_dokumenta__oznaka="PGD",) |
            Q(arhiviranje__isnull=True, vrsta_dokumenta__oznaka="NRC",)
            )

    class Meta(ArhiviranjeCreateForm.Meta):
        fields = (
            'dokument',
        )



# SEARCH FORMS

class ArhiviranjeSearchForm(forms.Form):
    oznaka = forms.CharField(label='oznaka', required=False)
    naziv = forms.CharField(label='naziv', required=False)

    # začetne nastavitve prikazanega "form"
    def __init__(self, *args, **kwargs):
        super(ArhiviranjeSearchForm, self).__init__(*args, **kwargs)
        # na začetku so okenca za vnos filtrov prazna
        self.initial['oznaka'] = ""
        self.initial['naziv'] = ""

    def filter_queryset(self, request, queryset):

        oznaka_filter = self.cleaned_data['oznaka']
        naziv_filter = self.cleaned_data['naziv']

        # filtriranje samo po oznaki
        if oznaka_filter and not naziv_filter:
            return queryset.filter(dokument__oznaka__icontains=oznaka_filter)

        # filtriranje ostalo
        if naziv_filter and not oznaka_filter:
            return queryset.filter(
                Q(dokument__naziv__icontains=naziv_filter)
                )

        # uporabnik filtrira po kratkem imenu in naslovu partnerja
        if oznaka_filter and naziv_filter:
            return queryset.filter(
                Q(dokument__oznaka__icontains=oznaka_filter) & (
                    Q(dokument__naziv__icontains=naziv_filter)
                )
            )

        return queryset
