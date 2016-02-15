from django import forms

from .models import Stevec, Delilnik, Odcitek, StevecStatus


class OdcitekCreateWidget(forms.Form):

    # STATUS = (
    #     ("A", 'pooblaščenec'),
    #     ("B", 'delavec'),
    #     )

    # priimek = forms.CharField()
    # ime = forms.CharField()
    # status = forms.ChoiceField(widget=forms.Select, choices=STATUS)
    # kvalifikacije = forms.CharField(widget=forms.Textarea)

    obdobje_leto = forms.CharField()
    obdobje_mesec = forms.CharField()
    odcital = forms.CharField()
    datum_odcitka = forms.CharField()
    stanje_novo = forms.CharField()


class StevecCreateForm(forms.ModelForm):
    
    class Meta:
        model = Stevec
        fields = [
            'oznaka',
            'naziv',
            'is_distribucija',
            'upravljavec',
        ]


class StevecStatusCreateForm(forms.ModelForm):

    class Meta:
        model = StevecStatus
        fields = [
            'v_okvari',
            'v_delovanju',
            'stevec',
        ]


class DelilnikCreateForm(forms.ModelForm):

    class Meta:
        model = Delilnik
        fields = [
            'oznaka',
            'meritev',
            'stevec',
        ]


class OdcitekCreateForm(forms.ModelForm):

    class Meta:
        model = Odcitek
        fields = [
            'delilnik',
            'odcital',
            'datum_odcitka',
            'obdobje_leto',
            'obdobje_mesec',
            'stanje_staro',
            'stanje_novo',
        ]
