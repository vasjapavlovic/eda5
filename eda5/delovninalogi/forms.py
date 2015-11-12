from django import forms
from django.utils import timezone

from .models import Opravilo, DelovniNalog, Delo

from eda5.deli.models import Element
from eda5.narocila.models import Narocilo
from eda5.partnerji.models import Oseba


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
        super(DelovniNalogVcakanjuModelForm, self).__init__(*args, **kwargs)
        # custom initial properties
        self.initial['status'] = 2

        
class DelovniNalogVplanuModelForm(forms.ModelForm):

    class Meta:
        model = DelovniNalog
        fields = (
            'status',
            )
        widgets = {
            'status': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        super(DelovniNalogVplanuModelForm, self).__init__(*args, **kwargs)
        # custom initial properties
        self.initial['status'] = 3


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
        super(DelovniNalogVresevanjuModelForm, self).__init__(*args, **kwargs)
        # custom initial properties
        self.initial['status'] = 4
        self.initial['datum_stop'] = timezone.now().date()


class DeloForm(forms.Form):

    DELAVCI = Oseba.objects.all()

    delavec = forms.ModelChoiceField(queryset=DELAVCI)


class DeloZacetoUpdateModelForm(forms.ModelForm):

    class Meta:
        model = Delo
        fields = ('time_stop',)
        widgets = {'time_stop': forms.HiddenInput(),}

    def __init__(self, *args, **kwargs):
        super(DeloZacetoUpdateModelForm, self).__init__(*args, **kwargs)
        # custom initial properties
        self.initial['time_stop'] = timezone.now().time().strftime("%H:%M:%S")

