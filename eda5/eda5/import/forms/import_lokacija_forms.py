from django import forms

# potrditev ali žeiliš uvoziti ali ne
class LokacijaUvozCsvForm(forms.Form):
    del01_prostori = forms.BooleanField(initial=False, required=False)
    # prostori = forms.BooleanField(initial=False, required=False)

