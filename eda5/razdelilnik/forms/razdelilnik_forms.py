# Python
from functools import partial

# Django
from django import forms
from django.db.models import Q

# Models
from ..models import Razdelilnik
from eda5.racunovodstvo.models import Racun

DateInput = partial(forms.DateInput, {'class': 'datepicker'})
TimeInput = partial(forms.TimeInput, {'class': 'timepicker'})


class RazdelilnikCreateFromZahtevekForm(forms.ModelForm):

    class Meta:
        model = Razdelilnik
        fields = (
            'stavba',
            'obdobje_obracuna_leto',
            'obdobje_obracuna_mesec',
            'oznaka',
            'naziv',
        )
        widgets = {
        }



# class RacunRazdelilnikCreateForm(forms.ModelForm):

#     def __init__(self, *args, **kwargs):
#         super(RacunRazdelilnikCreateForm, self).__init__(*args, **kwargs)
#         # custom initial properties

#         # querysets
#         self.fields["racun"].queryset = Racun.objects.filter(davcna_klasifikacija=1).exclude(
#             racunrazdelilnik__isnull=False).order_by('-arhiviranje__dokument__aktivnost__datum_aktivnosti')  # davcna_klasifikacija=1 --> Razdelilnik,
#         self.fields["razdelilnik"].queryset = Razdelilnik.objects.exclude(status=4)  # status=4 --> zaključeno

#     class Meta:
#         model = RacunRazdelilnik
#         fields = (
#             'razdelilnik',
#             'racun',
#         )



# class RacunRazdelilnikUpdateForm(forms.ModelForm):

#     def __init__(self, *args, **kwargs):
#         super(RacunRazdelilnikUpdateForm, self).__init__(*args, **kwargs)
#         # custom initial properties

#         # querysets
#         self.fields["racun"].queryset = Racun.objects.filter(davcna_klasifikacija=1).exclude(racunrazdelilnik__isnull=True)  # davcna_klasifikacija=1 --> Razdelilnik
#         self.fields["razdelilnik"].queryset = Razdelilnik.objects.exclude(status=4)  # status=4 --> zaključeno

#     class Meta:
#         model = RacunRazdelilnik
#         fields = (
#             'razdelilnik',
#             'racun',
#             'is_razdeljen',
#             'razdeljen_datum',
#         )
#         widgets = {
#             'razdeljen_datum': DateInput(),
#         }



class RazdelilnikSearchForm(forms.Form):
    oznaka = forms.CharField(label='oznaka', required=False)
    naziv = forms.CharField(label='naziv', required=False)

    # začetne nastavitve prikazanega "form"
    def __init__(self, *args, **kwargs):
        super(RazdelilnikSearchForm, self).__init__(*args, **kwargs)
        # na začetku so okenca za vnos filtrov prazna
        self.initial['oznaka'] = ""
        self.initial['naziv'] = ""


    def filter_queryset(self, request, queryset):

        oznaka_filter = self.cleaned_data['oznaka']
        naziv_filter = self.cleaned_data['naziv']

        # filtriranje samo po oznaki
        if oznaka_filter and not naziv_filter:
            return queryset.filter(
                Q(oznaka__icontains=oznaka_filter)
            )

        # filtriranje ostalo
        if naziv_filter and not oznaka_filter:
            return queryset.filter(
                Q(naziv__icontains=naziv_filter)
            )
        

        # uporabnik filtrira po kratkem imenu in naslovu partnerja
        if oznaka_filter and naziv_filter:
            return queryset.filter(
                Q(oznaka__icontains=oznaka_filter) &
                Q(naziv__icontains=naziv_filter)
            )

        return queryset

