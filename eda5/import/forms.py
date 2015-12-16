from django import forms


class UvozCsvForm(forms.Form):

    utiliti = forms.BooleanField(initial=True, required=False)
    poste = forms.BooleanField(initial=False, required=False)
    partnerji = forms.BooleanField(initial=False, required=False)
    banke = forms.BooleanField(initial=False, required=False)
    skupine_delov_stavbe = forms.BooleanField(initial=False, required=False)
    stroskovna_mesta = forms.BooleanField(initial=False, required=False)
    vrste_del = forms.BooleanField(initial=False, required=False)
    etazna_lastnina = forms.BooleanField(initial=False, required=False)

