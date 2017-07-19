from django import forms

# potrditev ali žeiliš uvoziti ali ne
class DeliUvozCsvForm(forms.Form):
    skupine_delov_stavbe = forms.BooleanField(initial=False, required=False)
    podskupine_delov_stavbe = forms.BooleanField(initial=False, required=False)
    del02_ostali_deli_stavbe = forms.BooleanField(initial=False, required=False)

