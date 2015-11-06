from django import forms

from .models import Partner, Oseba, Banka


class PartnerCreateForm(forms.ModelForm):

    class Meta:
        model = Partner
        fields = (
            "is_pravnaoseba",
            "davcni_zavezanec",
            "davcna_st",
            "maticna_st",
            "dolgo_ime",
            "kratko_ime",
            "naslov",
            "posta",
            )


class PartnerUpdateForm(PartnerCreateForm):

    def __init__(self, *args, **kwargs):
        super(PartnerUpdateForm, self).__init__(*args, **kwargs)

        # make fields required
        self.fields['dolgo_ime'].required = True
        self.fields['davcna_st'].required = True

    # model fields on which the search can be applied
    # davcna_st
    # maticna_st
    # dolgo_ime
    # kratko_ime
    # naslov
    # posta


class OsebaCreateForm(forms.ModelForm):

    class Meta:
        model = Oseba
        fields = (
            'priimek',
            'ime',
            'status',
            'kvalifikacije',
            'podjetje',
            )


class OsebaUpdateForm(OsebaCreateForm):
    pass


class OsebaCreateWidget(forms.Form):

    STATUS = (
        ("A", 'pooblaščenec'),
        ("B", 'delavec'),
        )

    priimek = forms.CharField()
    ime = forms.CharField()
    status = forms.ChoiceField(widget=forms.Select, choices=STATUS)
    kvalifikacije = forms.CharField(widget=forms.Textarea)


class TrrCreateWidget(forms.Form):

    BANKE = Banka.objects.all()

    iban = forms.CharField()
    banka = forms.ModelChoiceField(queryset=BANKE)



    # OSEBA MODEL
    # priimek = models.CharField(max_length=50)
    # ime = models.CharField(max_length=50)
    # status = models.CharField(max_length=1, choices=STATUS)
    # kvalifikacije = models.TextField(blank=True)
    # podjetje = models.ForeignKey(Partner)