from django import forms

from .models import Aktivnost, Dokument


class AktivnostCreateForm(forms.ModelForm):

    class Meta:
        model = Aktivnost
        fields = (
            'vrsta_aktivnosti',
            'izvajalec',
            'likvidiral',
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
