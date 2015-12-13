from functools import partial

from django import forms

from .models import Narocilo, NarociloTelefon, NarociloPogodba


DateInput = partial(forms.DateInput, {'class': 'datepicker'})
TimeInput = partial(forms.TimeInput, {'class': 'timepicker'})



class NarociloIzbiraForm(forms.Form):
    pass


class NarociloSplosnoCreateForm(forms.ModelForm):

    class Meta:
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
        widgets = {
            'datum_narocila': DateInput(),
            'datum_veljavnosti': DateInput(),
        }


class NarociloTelefonCreateForm(forms.ModelForm):

    class Meta:
        model = NarociloTelefon
        fields = [
            'telefonska_stevilka',
            'datum_klica',
            'cas_klica',
            'telefonsko_sporocilo',
        ]
        widgets = {
            'datum_klica': DateInput(),
            'cas_klica': TimeInput(),
        }


class NarociloPogodbaCreateForm(forms.ModelForm):

    class Meta:
        model = NarociloPogodba
        fields = [
            'st_pogodbe',
            'predmet_pogodbe',
        ]