from django import forms

from .models import Stavba, Etaza, Prostor

class StavbaCreateForm(forms.ModelForm):

    class Meta:
        model = Etaza


class EtazaCreateForm(forms.ModelForm):

    class Meta:
        model = Etaza


class ProstorCreateForm(forms.ModelForm):

    class Meta:
        model = Prostor

