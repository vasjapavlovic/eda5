from django import forms

from .models import Aktivnost, Dokument


class AktivnostCreateForm(forms.ModelForm):

    class Meta:
        model = Aktivnost
        fields = (
            'izvajalec',
            'vrsta_aktivnosti',
            'datum',
        )


class DokumentCreateForm(forms.ModelForm):

    class Meta:
        model = Dokument
        fields = (
            # 'aktivnost',
            'vrsta_dokumenta',
            'avtor',
            'naslovnik',
            'oznaka',
            'naziv',
            'datum',
            'priponka',
        )
