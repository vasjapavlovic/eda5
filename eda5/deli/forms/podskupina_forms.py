from django import forms

from ..models import Podskupina


class PodskupinaCreateForm(forms.ModelForm):

    class Meta:
        model = Podskupina
        fields = (
            'oznaka',
            'naziv',
            'skupina'
        )