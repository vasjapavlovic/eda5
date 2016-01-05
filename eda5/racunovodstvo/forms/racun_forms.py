from django import forms
from functools import partial
from django.utils import timezone

from eda5.core.models import ObdobjeLeto

from ..models import Racun, Konto, PodKonto

DateInput = partial(forms.DateInput, {'class': 'datepicker'})
TimeInput = partial(forms.TimeInput, {'class': 'timepicker'})


class RacunCreateForm(forms.ModelForm):

    class Meta:
        model = Racun
        fields = (
            "racunovodsko_leto",
            "oznaka",
            "davcna_klasifikacija",
            )

    def __init__(self, *args, **kwargs):
        super(RacunCreateForm, self).__init__(*args, **kwargs)

        # avtomatska dodelitev oznake
        # ---------------------------
        leto = timezone.now().date().year
        racunovodsko_leto = ObdobjeLeto.objects.get(oznaka=leto)
        self.initial['racunovodsko_leto'] = racunovodsko_leto

        try:  # "try" uporabimo ker če ni nobenega vnosa bo vrnjen error
            racun_zadnji = Racun.objects.filter(racunovodsko_leto=racunovodsko_leto).latest("oznaka")
            oznaka_zadnja = racun_zadnji.oznaka
            print(oznaka_zadnja)
            oznaka_nova = oznaka_zadnja + 1
            self.initial['oznaka'] = oznaka_nova

        except:
            self.initial['oznaka'] = 1


class KontoCreateForm(forms.ModelForm):

    class Meta:
        model = Konto
        fields = (
            'oznaka',
            'naziv',
            'zap_st',
        )


class PodkontoCreateForm(forms.ModelForm):

    class Meta:
        model = PodKonto
        fields = (
            'oznaka',
            'naziv',
            'zap_st',
            'skupina',
        )
