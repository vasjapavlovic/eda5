from django import forms

from .models import ObdobjeLeto, ObdobjeMesec

from django.db.models import Q


class ObdobjeLetoCreateForm(forms.ModelForm):

    class Meta:
        model = ObdobjeLeto
        fields = (
            'oznaka',
        )


class ObdobjeMesecCreateForm(forms.ModelForm):

    class Meta:
        model = ObdobjeMesec
        fields = (
            'oznaka',
            'naziv',
        )
