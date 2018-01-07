from django import forms

from .models import Aktivnost
from .models import KontrolaSpecifikacija



class AktivnostCreateForm(forms.ModelForm):

    class Meta:
        model = Aktivnost
        fields = (
            'oznaka',
            'naziv',
            'opis',
        )
        widgets = {

        }

    def __init__(self, *args, **kwargs):
        super(AktivnostCreateForm, self).__init__(*args, **kwargs)

        self.fields['naziv'].required = True


class KontrolaSpecifikacijaCreateForm(forms.ModelForm):

    class Meta:
        model = KontrolaSpecifikacija
        fields = (
            'oznaka',
            'naziv',
            'opis',
            'vrednost_vrsta',
        )
