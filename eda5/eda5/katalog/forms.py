from django import forms

from .models import TipArtikla, Proizvajalec, ModelArtikla


class TipArtiklaCreateForm(forms.ModelForm):

    class Meta:
        model = TipArtikla
        fields = (
            'oznaka',
            'naziv',
        )


class ProizvajalecCreateForm(forms.ModelForm):

    class Meta:
        model = Proizvajalec
        fields = (
            'oznaka',
            'naziv',
        )


class ModelArtiklaCreateForm(forms.ModelForm):

    class Meta:
        model = ModelArtikla
        fields = (
            'oznaka',
            'naziv',
            'tip_artikla',
            'proizvajalec',
        )
