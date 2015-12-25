from functools import partial

from django import forms

from .models import Aktivnost, Dokument, SkupinaDokumenta, VrstaDokumenta

DateInput = partial(forms.DateInput, {'class': 'datepicker'})
TimeInput = partial(forms.TimeInput, {'class': 'timepicker'})


class AktivnostCreateForm(forms.ModelForm):

    class Meta:
        model = Aktivnost
        fields = (
            'vrsta_aktivnosti',
            'izvajalec',
            'likvidiral',
            'datum_aktivnosti',
        )
        widgets = {
            'datum_aktivnosti': DateInput(),
        }


class DokumentCreateForm(forms.ModelForm):

    class Meta:
        model = Dokument
        fields = (
            'vrsta_dokumenta',
            'avtor',
            'naslovnik',
            'oznaka',
            'naziv',
            'datum_dokumenta',
            'priponka',
        )
        widgets = {
            'datum_dokumenta': DateInput(),
        }


class SkupinaDokumentaCreateForm(forms.ModelForm):

    class Meta:
        model = SkupinaDokumenta
        fields = (
            'oznaka',
            'naziv',
            'zap_st',
        )


class VrstaDokumentaCreateForm(forms.ModelForm):

    class Meta:
        model = VrstaDokumenta
        fields = (
            'oznaka',
            'naziv',
            'zap_st',
            'skupina',
        )
