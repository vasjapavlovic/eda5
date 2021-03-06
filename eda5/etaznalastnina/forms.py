from django import forms

from .models import Program, LastniskaEnotaElaborat, LastniskaEnotaInterna, LastniskaSkupina, InternaDodatno, UporabnoDovoljenje


class ProgramCreateForm(forms.ModelForm):

    class Meta:
        model = Program
        fields = (
            'oznaka',
            'naziv',
            'zap_st',
        )


class LastniskaEnotaElaboratCreateForm(forms.ModelForm):

    class Meta:
        model = LastniskaEnotaElaborat
        fields = (
            'oznaka',
            'naslov',
            'posta',
            'program',
            'opis',
            'povrsina_tlorisna_neto',
            'lastniski_delez',
        )


class LastniskaEnotaInternaCreateForm(forms.ModelForm):

    class Meta:
        model = LastniskaEnotaInterna
        fields = (
            'oznaka',
            'elaborat',
            'povrsina_tlorisna_neto',
            'lastniski_delez',
            'st_oseb',
        )


class LastniskaSkupinaCreateForm(forms.ModelForm):

    class Meta:
        model = LastniskaSkupina
        fields = (
            'oznaka',
            'naziv',
            'opis',
            'program',
            'lastniska_enota',
        )


class InternaDodatnoCreateForm(forms.ModelForm):

    class Meta:
        model = InternaDodatno
        fields = (
            'interna',
            'uporabno_dovoljenje',
            'stanje_prostora',
        )


class UporabnoDovoljenjeCreateForm(forms.ModelForm):

    class Meta:
        model = UporabnoDovoljenje
        fields = (
            'oznaka',
            'st_dokumenta',
            'datum',
            'objekt',
        )
