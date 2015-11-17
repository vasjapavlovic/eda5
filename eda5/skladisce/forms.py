from django import forms

from .models import Dobava


class DobavaCreateForm(forms.ModelForm):

    class Meta:
        model = Dobava
        fields = (
            'oznaka',
            'naziv',
            'datum',
            'prevzel',
            'dobavitelj',
            'dobavnica',
        )
