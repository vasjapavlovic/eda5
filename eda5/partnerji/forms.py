from django import forms

from .models import Partner


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
