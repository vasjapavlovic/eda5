from functools import partial

from django import forms
from django.utils import timezone

from .models import Narocilo, NarociloTelefon, NarociloPogodba


DateInput = partial(forms.DateInput, {'class': 'datepicker'})
TimeInput = partial(forms.TimeInput, {'class': 'timepicker'})


class NarociloIzbiraForm(forms.Form):
    pass


class NarociloSplosnoCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(NarociloSplosnoCreateForm, self).__init__(*args, **kwargs)

        # Dodelitev številke naročila
        predoznaka = "NRC"
        leto = timezone.now().date().year
        zap_st = Narocilo.objects.all().count() + 1

        nova_oznaka = "%s-%s-%s" % (predoznaka, leto, zap_st)
        self.initial['oznaka'] = nova_oznaka
        # avtomatsko dodeljena oznaka = ReadOnly
        self.fields['oznaka'].widget.attrs['readonly'] = True

    # post ne more povozit okence ki je readonly
    def clean_oznaka(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.oznaka
        else:
            return self.cleaned_data['oznaka']

    class Meta:
        model = Narocilo
        fields = [
            'oznaka',
            'predmet',
            'narocnik',
            'izvajalec',
            'datum_narocila',
            'datum_veljavnosti',
            'vrednost',
        ]
        widgets = {
            'datum_narocila': DateInput(),
            'datum_veljavnosti': DateInput(),
        }


class NarociloTelefonCreateForm(forms.ModelForm):

    class Meta:
        model = NarociloTelefon
        fields = [
            'oseba',
            'telefonska_stevilka',
            'datum_klica',
            'cas_klica',
            'telefonsko_sporocilo',
        ]
        widgets = {
            'datum_klica': DateInput(),
            'cas_klica': TimeInput(),
        }


class NarociloPogodbaCreateForm(forms.ModelForm):

    class Meta:
        model = NarociloPogodba
        fields = [
            'st_pogodbe',
            'predmet_pogodbe',
        ]
