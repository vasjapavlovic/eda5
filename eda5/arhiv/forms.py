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

        # 1. prikaži samo dokumente z oznako = "RAC" (računi)
        skupina_dokumenta = SkupinaDokumenta.objects.get(oznaka="RAC")
        self.fields["dokument"].queryset = Dokument.objects.filter(arhiviranje__isnull=True
                                                                   ).exclude(
                                                                   vrsta_dokumenta__skupina=skupina_dokumenta
                                                                   )

    class Meta(ArhiviranjeCreateForm.Meta):
        fields = (
            'dokument',
            'arhiviral',
            'elektronski',
            'fizicni',
        )


class ArhiviranjeRacunForm(ArhiviranjeCreateForm):

    def __init__(self, *args, **kwargs):

        super(ArhiviranjeRacunForm, self).__init__(*args, **kwargs)

        # 1. prikaži samo dokumente z oznako = "RAC" (računi) in INR interni računi
        self.fields["dokument"].queryset = Dokument.objects.filter(
            Q(arhiviranje__isnull=True, vrsta_dokumenta__oznaka="RAC",) |
            Q(arhiviranje__isnull=True, vrsta_dokumenta__oznaka="INR",)
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
            'arhiviral',
            'elektronski',
            'fizicni',
        )
        widgets = {'delovninalog': forms.HiddenInput()}
