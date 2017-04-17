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
from ..models import Povprasevanje

# Widgets
from eda5.arhiv.widgets import ArhiviranjeManyToManyRawIdWidget
DateInput = partial(forms.DateInput, {'class': 'datepicker'})
TimeInput = partial(forms.TimeInput, {'class': 'timepicker'})


class PovprasevanjeCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PovprasevanjeCreateForm, self).__init__(*args, **kwargs)

        ''' Avtomatska oznaka pomanjkljivosti. Oznaka = Zaporedna številka '''
        try:
            zap_st = Povprasevanje.objects.all().count()
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
        model = Povprasevanje
        fields = (
            'oznaka',
            'naziv',
            'opis',
            'datum',
        )
        widgets = {
            'datum': DateInput(),
        }




class PovprasevanjeCreateFromZahtevekForm(PovprasevanjeCreateForm):
    pass


class PovprasevanjeUpdateForm(forms.ModelForm):

    class Meta:
        model = Povprasevanje
        fields = (
            'oznaka',
            'naziv',
            'opis',
            'datum',
            'status',
            'priloge',
        )
        widgets = {
            'datum': DateInput(),
            'priloge': ArhiviranjeManyToManyRawIdWidget(model._meta.get_field('priloge').rel, site),
        }
