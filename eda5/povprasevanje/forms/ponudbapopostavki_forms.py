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
from ..models import PonudbaPoPostavki

# Widgets
DateInput = partial(forms.DateInput, {'class': 'datepicker'})
TimeInput = partial(forms.TimeInput, {'class': 'timepicker'})


class PonudbaPoPostavkiCreateForm(forms.ModelForm):

    class Meta:
        model = PonudbaPoPostavki
        fields = (
            'postavka',
            'vrednost_za_izracun',
            'vrednost_opis',
        )



class PonudbaPoPostavkiUpdateForm(forms.ModelForm):

    class Meta:
        model = PonudbaPoPostavki
        fields = (
            'vrednost_za_izracun',
            'vrednost_opis',
        )


