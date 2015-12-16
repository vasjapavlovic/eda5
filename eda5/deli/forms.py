from django import forms

from .models import Podskupina, Skupina, DelStavbe


class DelCreateForm(forms.ModelForm):

    class Meta:
        model = DelStavbe
        fields = (
            'podskupina',
            'oznaka',
            'naziv',
            'shema',
            'lastniska_skupina',
        )


class SkupinaCreateForm(forms.ModelForm):

    class Meta:
        model = Skupina
        fields = (
            'oznaka',
            'naziv',
        )


class PodskupinaCreateForm(forms.ModelForm):

    class Meta:
        model = Podskupina
        fields = (
            'oznaka',
            'naziv',
            'skupina'
        )
