from django import forms

from .models import Narocilo, NarociloTelefon, NarociloPogodba

class NarociloIzbiraForm(forms.Form):
    pass



class NarociloSplosnoCreateForm(forms.ModelForm):
    model = Narocilo
    fields = [
        'narocnik',
        'izvajalec',
        'oznaka',
        'predmet',
        'datum_narocila',
        'datum_veljavnosti',
        'vrednost',
    ]


class NarociloTelefonCreateForm(forms.ModelForm):
    model = NarociloTelefon
    fields = [
        'telefonska_stevilka',
        'datum_klica',
        'cas_klica',
        'telefonsko_sporocilo',
    ]


class NarociloPogodbaCreateForm(forms.ModelForm):
    model = NarociloPogodba
    fields = [
        'st_pogodbe',
        'predmet_pogodbe',
    ]