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
from ..models import Postavka

# Widgets
from eda5.arhiv.widgets import ArhiviranjeManyToManyRawIdWidget
from eda5.partnerji.widgets import PartnerForeignKeyRawIdWidget

DateInput = partial(forms.DateInput, {'class': 'datepicker'})
TimeInput = partial(forms.TimeInput, {'class': 'timepicker'})


class PostavkaCreateForm(forms.ModelForm):

    class Meta:
        model = Postavka
        fields = (
            'oznaka',
            'opis',
        )


class PostavkaUpdateForm(forms.ModelForm):

    class Meta:
        model = Postavka
        fields = (
            'oznaka',
            'opis',
            'priloge',
        )
        widgets = {
            'priloge': ArhiviranjeManyToManyRawIdWidget(model._meta.get_field('priloge').rel, site), 
        }
