from django import forms
#import floppyforms.__future__ as forms

from .models import Aktivnost, Dokument


class AktivnostCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AktivnostCreateForm, self).__init__(*args, **kwargs)

        aktivnost_id = Aktivnost.objects.all().count()
        aktivnost_id = aktivnost_id + 1

        self.initial['id_1'] = aktivnost_id

    class Meta:
        model = Aktivnost
        fields = (
            'id_1',
            'izvajalec',
            'vrsta_aktivnosti',
            'datum',
        )
        widgets = {
            'id_1': forms.HiddenInput(),
        }


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
