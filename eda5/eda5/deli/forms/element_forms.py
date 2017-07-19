from django import forms

from ..models import Element


class ElementCreateForm(forms.ModelForm):

    class Meta:
        model = Element
        fields = (
            'tovarniska_st',
            'serijska_st',
            'artikel',
            'projektno_mesto',
        )