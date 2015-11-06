from django import forms


class ZaznamekForm(forms.Form):

    tekst = forms.TextField()
    datum = forms.DateField()
    ura = forms.TimeField()
