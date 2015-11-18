from django import forms

from . import models

class PomanjkljivostCreateForm(forms.ModelForm):

    class Meta:
        model = models.Pomanjkljivost
        fields = (
            'oznaka',
            'naziv',
            'prijavil',
            'datum_ugotovitve',
            'element',
            'etaza',
            'lokacija',
        )