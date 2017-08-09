# Python
from functools import partial

# Django
from django import forms
from django.db.models import Q

# Models
from ..models import StrosekRazdelilnik, Razdelilnik
from eda5.racunovodstvo.models import Racun, Strosek

DateInput = partial(forms.DateInput, {'class': 'datepicker'})
TimeInput = partial(forms.TimeInput, {'class': 'timepicker'})




class StrosekRazdelilnikCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(StrosekRazdelilnikCreateForm, self).__init__(*args, **kwargs)
        # custom initial properties

        razdelilnik = self.instance.pk

        # querysets
        self.fields["strosek"].queryset = Strosek.objects\
            .filter(
                # prikaži samo stroške, ki so klasificirani kot razdelilnik
                racun__davcna_klasifikacija=1,
                # prikazi samo stroške, ki še niso likvidirani
                
                # prikaži stroške, ki so del obravnavanega razdelilnika (instance)
                #obdobje_obracuna_leto=razdelilnik.obdobje_obracuna_leto,
                #obdobje_obracuna_mesec=razdelilnik.obdobje_obracuna_mesec)
                strosekrazdelilnik__isnull=True)\
            .order_by('-racun__arhiviranje__dokument__aktivnost__datum_aktivnosti')  # davcna_klasifikacija=1 --> Razdelilnik,
        
    class Meta:
        model = StrosekRazdelilnik
        fields = (
            'strosek',
        )



class StrosekRazdelilnikUpdateForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(StrosekRazdelilnikUpdateForm, self).__init__(*args, **kwargs)
        # custom initial properties

        razdelilnik = self.instance

        # querysets
        self.fields["strosek"].queryset = Strosek.objects\
            .filter(
                # prikaži samo stroške, ki so klasificirani kot razdelilnik
                racun__davcna_klasifikacija=1,
                # prikazi samo stroške, ki še niso likvidirani
                strosekrazdelilnik__isnull=False,
                # prikaži stroške, ki so del obravnavanega razdelilnika (instance)
                obdobje_obracuna_leto=razdelilnik.obdobje_obracuna_leto,
                obdobje_obracuna_mesec=razdelilnik.obdobje_obracuna_mesec)\
            .order_by('-arhiviranje__dokument__aktivnost__datum_aktivnosti')  # davcna_klasifikacija=1 --> Razdelilnik,
        
    class Meta:
        model = StrosekRazdelilnik
        fields = (
            'strosek',
        )
        widgets = {
            'razdeljen_datum': DateInput(),
        }



