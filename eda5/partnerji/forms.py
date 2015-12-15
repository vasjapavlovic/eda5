from django import forms

from .models import Partner, Oseba, Banka, Posta


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



class UvozPartnerjiCsvForm(forms.Form):

    uvozim = forms.BooleanField()


    # OSEBA MODEL
    # priimek = models.CharField(max_length=50)
    # ime = models.CharField(max_length=50)
    # status = models.CharField(max_length=1, choices=STATUS)
    # kvalifikacije = models.TextField(blank=True)
    # podjetje = models.ForeignKey(Partner)

# def add_new_partners(rows):
#     rows = io.StringIO(rows)
#     records_added = 0

#     seznam = csv.DictReader(rows, delimiter=";")
#     print(seznam.fieldnames)

#     # for row in csv.DictReader(rows, delimiter=";"):
#     for row in seznam:
#     # Generate a dict per row, with the first CSV row being the keys.
    
#     # Bind the row data to the PurchaseForm.
#         print(row)
#         form2 = PartnerCreateForm(row)
#         # Check to see if the row data is valid.
#         if form2.is_valid():
#         # Row data is valid so save the record.
#             form2.save()
#             records_added += 1

#     print(records_added)
#     return records_added

# filename = os.path.abspath("eda5/partnerji/rows1.csv")
# with open(filename, 'r') as file:
#     partnerji_file = file.read()



# add_new_partners(partnerji_file)

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