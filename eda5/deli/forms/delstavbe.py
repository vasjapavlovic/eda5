from django import forms

from ..models import DelStavbe


class DelCreateForm(forms.ModelForm):

    class Meta:
        model = DelStavbe
        fields = (
            'podskupina',
            'oznaka',
            'naziv',
            'funkcija',
            'shema',
            'lastniska_skupina',
        )


class DelUpdateForm(DelCreateForm):
    pass