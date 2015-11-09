from django import forms

from .models import Podskupina, Skupina
from eda5.etaznalastnina.models import LastniskaSkupina


class DelCreateForm(forms.Form):

    # def __init__(self, *args, **kwargs):
    #     super(DelCreateForm, self).__init__(*args, **kwargs)
    #     # access object through self.instance...
    #     self.fields['podskupina'].queryset = Podskupina.objects.filter(skupina=self.instance.skupina)

    # SKUPINE = Skupina.objects.all()
    PODSKUPINE = Podskupina.objects.all()

    LASTNISKE_SKUPINE = LastniskaSkupina.objects.all()


    # skupina = forms.ModelChoiceField(queryset=SKUPINE)
    podskupina = forms.ModelChoiceField(queryset=PODSKUPINE)
    # oznaka = forms.CharField(max_length=20)
    naziv = forms.CharField(max_length=255)
    shema = forms.FileField(required=False)
    lastniska_skupina = forms.ModelChoiceField(required=False, queryset=LASTNISKE_SKUPINE)
