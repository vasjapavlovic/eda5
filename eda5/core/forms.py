from django import forms

from .models import ObdobjeLeto, ObdobjeMesec

from django.db.models import Q


class ObdobjeLetoCreateForm(forms.ModelForm):

    class Meta:
        model = ObdobjeLeto
        fields = (
            'oznaka',
        )


class ObdobjeMesecCreateForm(forms.ModelForm):

    class Meta:
        model = ObdobjeMesec
        fields = (
            'oznaka',
            'naziv',
        )







        # # uporabnik filtrira samo po krakem imenu partnerja
        # if \
        #     self.cleaned_data['kratko_ime'] and not \
        #     self.cleaned_data['davcna_st'] and not \
        #     self.cleaned_data['naslov']:

        #     return queryset.filter(kratko_ime__icontains=self.cleaned_data['kratko_ime'])

        # # uporabnik filtrira samo po naslovu partnerja
        # if \
        #     self.cleaned_data['naslov'] and not \
        #     self.cleaned_data['davcna_st'] and not \
        #     self.cleaned_data['kratko_ime']:

        #     return queryset.filter(naslov__icontains=self.cleaned_data['naslov'])

        # # uporabnik filtrira samo po davčni št. partnerja
        # if \
        #     self.cleaned_data['davcna_st'] and not \
        #     self.cleaned_data['kratko_ime'] and not \
        #     self.cleaned_data['naslov']:

        #     return queryset.filter(davcna_st__icontains=self.cleaned_data['davcna_st'])



        # # uporabnik filtrira po davčni in kratkem imenu
        # if \
        #     self.cleaned_data['davcna_st'] and \
        #     self.cleaned_data['kratko_ime'] and not \
        #     self.cleaned_data['naslov']:
        #     return queryset.filter(
        #         Q(davcna_st__icontains=self.cleaned_data['davcna_st']) &
        #         Q(kartko_ime__icontains=self.cleaned_data['kratko_ime']))


        # # uporabnik filtrira po davčni in naslovu
        # if \
        #     self.cleaned_data['davcna_st'] and \
        #     self.cleaned_data['naslov'] and not \
        #     self.cleaned_data['kratko_ime']:
        #     return queryset.filter(
        #         Q(davcna_st__icontains=self.cleaned_data['davcna_st']) &
        #         Q(kartko_ime__icontains=self.cleaned_data['kratko_ime']))