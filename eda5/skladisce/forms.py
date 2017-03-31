# Python
from functools import partial

# Django
from django import forms
from django.contrib.admin.sites import site
from django.utils import timezone

# Models
from .models import Dobava, Dnevnik

# Widgets
from eda5.partnerji.widgets import OsebaForeignKeyRawIdWidget
DateInput = partial(forms.DateInput, {'class': 'datepicker'})
TimeInput = partial(forms.TimeInput, {'class': 'timepicker'})


class DobavaCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(DobavaCreateForm, self).__init__(*args, **kwargs)

        # avtomatska oznaka
        try:
            st_dobav = Dobava.objects.all().count() + 1
        except:
            st_dobav = 1

        leto = timezone.now().date().year
        nova_oznaka = 'DOB-' + str(leto) + "-" + str(st_dobav)
        self.initial['oznaka'] = nova_oznaka

    class Meta:
        model = Dobava
        fields = (
            'oznaka',
            'naziv',
            'datum',
            'prevzel',
            'dobavitelj',
            'dobavnica',
        )
        widgets = {
            'datum': DateInput(),
            'prevzel': OsebaForeignKeyRawIdWidget(model._meta.get_field('prevzel').rel, site),
        }


class DnevnikDobavaCreateForm(forms.ModelForm):

    class Meta:
        model = Dnevnik
        fields = (
            'artikel',
            'likvidiral',
            'kom',
            'cena',
            'stopnja_ddv',
        )
        widgets = {
            'likvidiral': OsebaForeignKeyRawIdWidget(model._meta.get_field('likvidiral').rel, site),
        }


class SkladisceDnevnikFromDelovniNalogCreateForm(forms.ModelForm):

    class Meta:
        model = Dnevnik
        fields = (
            'artikel',
            'likvidiral',
            'kom',
        )
        widgets = {
            'likvidiral': OsebaForeignKeyRawIdWidget(model._meta.get_field('likvidiral').rel, site),
        }


class SkladisceDnevnikUpdateForm(forms.ModelForm):

    class Meta:
        model = Dnevnik
        fields = (
            'artikel',
            'likvidiral',
            'kom',
        )
        widgets = {
            'likvidiral': OsebaForeignKeyRawIdWidget(model._meta.get_field('likvidiral').rel, site),
        }
