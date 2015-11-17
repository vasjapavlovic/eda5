from django import forms

from .models import Dobava, Dnevnik


class DobavaCreateForm(forms.ModelForm):

    # avtomatsko dodeli zaporedno številko

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


class DnevnikDobavaCreateForm(forms.ModelForm):

    class Meta:
        model = Dnevnik
        fields = (
            'artikel',
            'likvidiral',
            'kom',
            'cena',
            'stopnja_ddv',
        )
