from django import forms
from django.utils import timezone

from .models import Opravilo, DelovniNalog

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

class DelovniNalogVcakanjuModelForm(forms.ModelForm):

    class Meta:
        model = DelovniNalog
        fields = (
            'status',
            'datum_plan',
            )
        widgets = {
            'status': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        
        initial = kwargs.get('initial', {})

        # custom initial properties
        initial['status'] = 2

        kwargs['initial'] = initial
        super(DelovniNalogVcakanjuModelForm, self).__init__(*args, **kwargs)


class DelovniNalogVresevanjuModelForm(forms.ModelForm):

    class Meta:
        model = DelovniNalog
        fields = (
            'status',
            'datum_stop',
            )
        widgets = {
            'status': forms.HiddenInput(),
            'datum_stop': forms.TextInput(attrs={'readonly':'True'})
            }

    def __init__(self, *args, **kwargs):
        # initial1 = kwargs.get('initial', {})
        # initial2 = kwargs.get('initial', {})
        super(DelovniNalogVresevanjuModelForm, self).__init__(*args, **kwargs)
        self.initial['status'] = 4
        self.initial['datum_stop'] = timezone.now().date()

        #kwargs['initial'] = initial

        