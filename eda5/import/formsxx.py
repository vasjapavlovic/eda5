from django import forms


class UtilitiUvozCsvForm(forms.Form):
    utiliti = forms.BooleanField(initial=False, required=False)

class PartnerjiUvozCsvForm(forms.Form):
    poste = forms.BooleanField(initial=False, required=False)
    poste_tujina = forms.BooleanField(initial=False, required=False)
    partnerji = forms.BooleanField(initial=False, required=False)
    partnerji_edacenter = forms.BooleanField(initial=False, required=False)
    banke = forms.BooleanField(initial=False, required=False)

    partnerji_edafm_update = forms.BooleanField(initial=False, required=False)

class DeliUvozCsvForm(forms.Form):
    skupine_delov_stavbe = forms.BooleanField(initial=False, required=False)

class RacunovodstvoUvozCsvForm(forms.Form):
    stroskovna_mesta = forms.BooleanField(initial=False, required=False)

class DelovniNalogiUvozCsvForm(forms.Form):
    vrste_del = forms.BooleanField(initial=False, required=False)

class EtaznaLastninaUvozCsvForm(forms.Form):
    etazna_lastnina = forms.BooleanField(initial=False, required=False)
    interna_dodatno = forms.BooleanField(initial=False, required=False)
    uporabno_dovoljenje = forms.BooleanField(initial=False, required=False)

class KatalogUvozCsvForm(forms.Form):
    tip_artikla = forms.BooleanField(initial=False, required=False)
    proizvajalec = forms.BooleanField(initial=False, required=False)
    model_artikla = forms.BooleanField(initial=False, required=False)

class PostaUvozCsvForm(forms.Form):
    vrsta_dokumenta = forms.BooleanField(initial=False, required=False)

class PredpisiUvozCsvForm(forms.Form):
    opravila = forms.BooleanField(initial=False, required=False)
    predpisi = forms.BooleanField(initial=False, required=False)
    relacija_predpisi_opravila = forms.BooleanField(initial=False, required=False)

class StevcnoStanjeUvozCsvForm(forms.Form):
    stevci = forms.BooleanField(initial=False, required=False)
    stevci_status = forms.BooleanField(initial=False, required=False)
    delilniki = forms.BooleanField(initial=False, required=False)
    odcitki = forms.BooleanField(initial=False, required=False)

class ModuliUvozCsvForm(forms.Form):
    moduli = forms.BooleanField(initial=False, required=False)
