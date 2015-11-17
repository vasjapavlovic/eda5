from django import forms

from .models import Arhiviranje, ArhivMesto


class ArhiviranjeCreateForm(forms.ModelForm):

    class Meta:
        model = Arhiviranje
        fields = (
            'arhiviral',
            'lokacija_hrambe',
            'elektronski',
            'fizicni',
        )
