from functools import partial

# Django

from django import forms
# potrebno za RawIdWidget
from django.contrib.admin.sites import site
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.core.exceptions import ValidationError
from django.template.loader import render_to_string
from django.utils import timezone

# Models
from .models import Naloga

# Widgets
from eda5.partnerji.widgets import OsebaForeignKeyRawIdWidget
DateInput = partial(forms.DateInput, {'class': 'datepicker'})
TimeInput = partial(forms.TimeInput, {'class': 'timepicker'})


class NalogaCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(NalogaCreateForm, self).__init__(*args, **kwargs)

        ''' Avtomatska oznaka pomanjkljivosti. Oznaka = Zaporedna številka '''
        try:
            zap_st = Naloga.objects.all().count()
            zap_st = zap_st + 1
        except:
            zap_st = 1

        oznaka = zap_st
        self.initial['oznaka'] = oznaka
        self.fields['oznaka'].widget.attrs['readonly'] = True


    def clean_oznaka(self):

        ''' poskrbimo: post ne more povoziti OZNAKO, ki je readonly'''
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.oznaka
        else:
            return self.cleaned_data['oznaka']


    class Meta:
        model = Naloga
        fields = (
            
            # za uporabnika
            'oznaka',
            'naziv',
            'opis',
            'rok_izvedbe',
            'prioriteta',
            'nosilec',
            'vnos_sestanka',
            'status',
        )
        widgets = {
            'rok_izvedbe': DateInput(),
            'nosilec': OsebaForeignKeyRawIdWidget(model._meta.get_field('nosilec').rel, site),
        }




class NalogaCreateFromZahtevekForm(NalogaCreateForm):
    pass


class NalogaUpdateForm(forms.ModelForm):

    class Meta:
        model = Naloga
        fields = (
            'oznaka',
            'naziv',
            'opis',
            'rok_izvedbe',
            'prioriteta',
            'nosilec',
            'vnos_sestanka',
            'status',
        )
        widgets = {
            'rok_izvedbe': DateInput(),
            'nosilec': OsebaForeignKeyRawIdWidget(model._meta.get_field('nosilec').rel, site),
        }


class NalogaIzbiraFrom(forms.Form):

    def __init__(self, *args, **kwargs):
        super(NalogaIzbiraFrom, self).__init__(*args, **kwargs)

        # nastavimo, da je izbira pomanjkljivosti obvezna
        self.fields['naloga'].required = True

    # definiramo atribut v formu
    naloga = forms.ModelChoiceField(
        queryset=Naloga.objects.filter(zahtevek__isnull=True))





