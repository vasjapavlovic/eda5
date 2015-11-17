from django import forms

from .models import Arhiviranje, ArhivMesto

from eda5.posta.models import Dokument


class ArhiviranjeCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ArhiviranjeCreateForm, self).__init__(*args, **kwargs)

        # 1. prikaži samo nearhivirane dokumente
        # 2. prikazati samo specifično vrsto dokumentov

        self.fields["dokument"].queryset = Dokument.objects.filter(arhiviranje__isnull=True)

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

    class Meta(ArhiviranjeCreateForm.Meta):
        fields = (
            'zahtevek',
            'dokument',
            'arhiviral',
            'elektronski',
            'fizicni',
            'lokacija_hrambe',
        )
        widgets = {'zahtevek': forms.HiddenInput()}


class ArhiviranjeDelovniNalogForm(ArhiviranjeCreateForm):

    class Meta(ArhiviranjeCreateForm.Meta):
        fields = (
            'delovninalog',
            'dokument',
            'arhiviral',
            'elektronski',
            'fizicni',
            'lokacija_hrambe',
        )
        widgets = {'delovninalog': forms.HiddenInput()}
