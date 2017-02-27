from django import forms

from ..models import Nastavitev


class NastavitevCreateForm(forms.ModelForm):

    class Meta:
        model = Nastavitev
        fields = (
            'obratovalni_parameter',
            'vrednost',
            'datum_nastavitve',
            'element',
        )