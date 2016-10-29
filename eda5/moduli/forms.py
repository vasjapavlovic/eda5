from django import forms

from .models import Modul, Zavihek


class ModulCreateForm(forms.ModelForm):

    class Meta:
        model = Modul
        fields = (
            'oznaka',
            'naziv',
            'opis',
            'barva',
            'url_ref',
            'zap_st',
        )

class ZavihekCreateForm(forms.ModelForm):

    class Meta:
        model = Zavihek
        fields = (
            'oznaka',
            'naziv',
            'url_ref',
            'zap_st',
            'parent',
            'modul',
        )
