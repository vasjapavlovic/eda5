from django import forms

from ..models import Podskupina, Skupina


class SkupinaCreateForm(forms.ModelForm):

    class Meta:
        model = Skupina
        fields = (
            'oznaka',
            'naziv',
        )


class SkupinaIzbiraForm(forms.Form):

    skupina = forms.ModelChoiceField(queryset=Skupina.objects.all())
    podskupina_hidden = forms.ModelChoiceField(queryset=Podskupina.objects.all())