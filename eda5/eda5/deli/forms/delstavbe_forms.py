from django import forms
from django.db.models import Q

from ..models import DelStavbe


class DelCreateForm(forms.ModelForm):

    class Meta:
        model = DelStavbe
        fields = (
            'podskupina',
            'oznaka',
            'naziv',
            'funkcija',
            'bim_id',
            #'shema',
            'lastniska_skupina',
        )


class DelUpdateForm(DelCreateForm):
    pass







