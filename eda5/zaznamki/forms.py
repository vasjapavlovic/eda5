from django import forms


class ZaznamekForm(forms.Form):

    tekst = forms.CharField(widget=forms.Textarea)
    datum = forms.DateField()
    ura = forms.TimeField()
