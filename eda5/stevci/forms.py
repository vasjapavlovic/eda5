from django import forms


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
