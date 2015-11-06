from django import forms

from .models import Opravilo

from eda5.deli.models import Element
from eda5.narocila.models import Narocilo


class OpraviloForm(forms.Form):

    # querysets
    NAROCILA = Narocilo.objects.all()
    ELEMENTI = Element.objects.all()

    # FORM
    # **onovno
    oznaka = forms.CharField()
    naziv = forms.CharField()
    rok_izvedbe = forms.DateField()
    # **relacije
    narocilo = forms.ModelChoiceField(queryset=NAROCILA)
    # element = forms.ModelMultipleChoiceField(queryset=ELEMENTI)


class OpraviloModelForm(forms.ModelForm):
    class Meta:
        model = Opravilo
        fields = (
            'narocilo',
            'element',
            'oznaka',
            'naziv',
            'rok_izvedbe',
            )
