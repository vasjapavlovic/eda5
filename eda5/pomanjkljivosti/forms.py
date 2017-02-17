from django import forms
from django.utils import timezone


from .models import Pomanjkljivost



class PomanjkljivostCreateForm(forms.ModelForm):

    class Meta:
        model = Pomanjkljivost
        fields = (
            'oznaka',
            'naziv',
            'prijavil_text',
            'prijava_dne',
            'element_text',
            'etaza_text',
            'lokacija_text',
            'prioriteta',
        )


class PomanjkljivostCreateFromZahtevekForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super(PomanjkljivostCreateFromZahtevekForm, self).__init__(*args, **kwargs)

        ''' Avtomatska oznaka pomanjkljivosti. Oznaka = Zaporedna številka '''
        try:
            zap_st = Pomanjkljivost.objects.all().count()
            zap_st = zap_st + 1
        except:
            zap_st = 1

        oznaka = zap_st
        self.initial['oznaka'] = oznaka
        self.fields['oznaka'].widget.attrs['readonly'] = True


        ''' Avtomatska izdelava datuma vnosa pomanjkljivosti '''
        prijava_dne = timezone.now().date()
        self.initial['prijava_dne'] = prijava_dne

    def clean_oznaka(self):

        ''' poskrbimo: post ne more povoziti OZNAKO, ki je readonly'''

        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.oznaka
        else:
            return self.cleaned_data['oznaka']


    class Meta:
        model = Pomanjkljivost
        fields = (
            'oznaka',
            'naziv',
            'prijavil_text',
            'prijava_dne',
            'element_text',
            'element',
            'etaza_text',
            'lokacija_text',
            'prioriteta',
        )