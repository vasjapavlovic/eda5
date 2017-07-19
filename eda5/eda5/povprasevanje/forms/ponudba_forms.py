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
from ..models import Ponudba

# Widgets
from eda5.arhiv.widgets import ArhiviranjeForeignKeyRawIdWidget
from eda5.partnerji.widgets import PartnerForeignKeyRawIdWidget

DateInput = partial(forms.DateInput, {'class': 'datepicker'})
TimeInput = partial(forms.TimeInput, {'class': 'timepicker'})


class PonudbaCreateForm(forms.ModelForm):

    class Meta:
        model = Ponudba
        fields = (
            'oznaka',
            'ponudnik',
        )
        widgets = {
            'ponudnik': PartnerForeignKeyRawIdWidget(model._meta.get_field('ponudnik').rel, site),
        }



class PonudbaUpdateForm(forms.ModelForm):

    class Meta:
        model = Ponudba
        fields = (
            'oznaka',
            'ponudnik',
            'ponudba_dokument',
            'garancija',
            'referenca_opis',
            'referenca_dokument',
        )
        widgets = {
            'ponudnik': PartnerForeignKeyRawIdWidget(model._meta.get_field('ponudnik').rel, site),
            'ponudba_dokument': ArhiviranjeForeignKeyRawIdWidget(model._meta.get_field('ponudba_dokument').rel, site),
            'referenca_dokument': ArhiviranjeForeignKeyRawIdWidget(model._meta.get_field('referenca_dokument').rel, site),
        }

