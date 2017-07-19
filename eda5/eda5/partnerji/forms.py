from django import forms

from django.db.models import Q

from .models import Partner, Oseba, Banka, Posta, Drzava


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
            "kontakt_tel",
            "kontakt_email",
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

class PartnerSearchForm(forms.Form):
    kratko_ime = forms.CharField(label='kratko_ime', required=False)
    davcna_st = forms.CharField(label='davcna_st', required=False)

    # začetne nastavitve prikazanega "form"
    def __init__(self, *args, **kwargs):
        super(PartnerSearchForm, self).__init__(*args, **kwargs)
        # na začetku so okenca za vnos filtrov prazna
        self.initial['kratko_ime'] = ""
        self.initial['davcna_st'] = ""

    def filter_queryset(self, request, queryset):

        kratko_ime_filter = self.cleaned_data['kratko_ime']
        davcna_st_filter = self.cleaned_data['davcna_st']

        # uporabnik filtrira samo po krakem imenu partnerja
        if kratko_ime_filter and not davcna_st_filter:
            return queryset.filter(kratko_ime__icontains=kratko_ime_filter)

        # uporabnik filtrira samo po naslovu partnerja
        if davcna_st_filter and not kratko_ime_filter:
            return queryset.filter(davcna_st__icontains=davcna_st_filter)
        

        # uporabnik filtrira po kratkem imenu in naslovu partnerja
        if kratko_ime_filter and davcna_st_filter:
            return queryset.filter(
                Q(kratko_ime__icontains=kratko_ime_filter) &
                Q(davcna_st__icontains=davcna_st_filter))

        return queryset


class OsebaSearchForm(forms.Form):
    oznaka = forms.CharField(label='partner', required=False)
    naziv = forms.CharField(label='naziv', required=False)

    # začetne nastavitve prikazanega "form"
    def __init__(self, *args, **kwargs):
        super(OsebaSearchForm, self).__init__(*args, **kwargs)
        # na začetku so okenca za vnos filtrov prazna
        self.initial['oznaka'] = ""
        self.initial['naziv'] = ""

    def filter_queryset(self, request, queryset):

        oznaka_filter = self.cleaned_data['oznaka']
        naziv_filter = self.cleaned_data['naziv']

        # filtriranje samo po oznaki
        if oznaka_filter and not naziv_filter:
            return queryset.filter(
                Q(podjetje__kratko_ime__icontains=oznaka_filter) |
                Q(podjetje__davcna_st__icontains=oznaka_filter)
            )

        # filtriranje ostalo
        if naziv_filter and not oznaka_filter:
            return queryset.filter(
                Q(priimek__icontains=naziv_filter) |
                Q(ime__icontains=naziv_filter)
            )
        

        # uporabnik filtrira po kratkem imenu in naslovu partnerja
        if oznaka_filter and naziv_filter:
            return queryset.filter(
                (
                    Q(podjetje__kratko_ime__icontains=oznaka_filter) |
                    Q(podjetje__davcna_st__icontains=oznaka_filter)
                ) &
                (
                    Q(priimek__icontains=naziv_filter) |
                    Q(ime__icontains=naziv_filter)
                )
            )

        return queryset

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



class UvozPartnerjiCsvForm(forms.Form):

    uvozim = forms.BooleanField()




class PostaCreateForm(forms.ModelForm):

    class Meta:
        model = Posta
        fields = (
            'postna_stevilka',
            'naziv',
            'drzava',
            )


class BankaCreateForm(forms.ModelForm):

    class Meta:
        model = Banka
        fields = (
            'bic_koda',
            'bancna_oznaka',
            'partner',
        )


class DrzavaCreateForm(forms.ModelForm):

    class Meta:
        model = Drzava
        fields = (
            'naziv',
            'iso_koda',
        )