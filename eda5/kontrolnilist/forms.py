from django import forms

from .models import Aktivnost



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

        # filtriranje dropdown
        self.fields['naziv'].required = True
