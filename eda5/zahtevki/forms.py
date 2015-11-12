from django import forms
from django.utils import timezone

from .models import Zahtevek


class ZahtevekCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ZahtevekCreateForm, self).__init__(*args, **kwargs)
        # custom initial properties
        # OZNAKA - tuki je napisano z namen, ker je form uporabljen na dveh različnih mestih
        leto = timezone.now().date().year
        zap_st = Zahtevek.objects.all().count()
        zap_st = zap_st +1
        nova_oznaka = "ZHT-%s-%s" % (leto, zap_st)
        self.initial['oznaka'] = nova_oznaka

        self.fields['oznaka'].widget.attrs['readonly'] = True

    def clean_oznaka(self):
        # poskrbimo, post ne more povoziti OZNAKO, ki je readonly
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.oznaka
        else:
            return self.cleaned_data['oznaka']

    class Meta:
        model = Zahtevek
        fields = (
            'oznaka',
            'predmet',
            'rok_izvedbe',
            'narocilo',
            'nosilec',
            'zahtevek_skodni_dogodek',
            'zahtevek_sestanek',
            'zahtevek_izvedba_dela',
        )

    
