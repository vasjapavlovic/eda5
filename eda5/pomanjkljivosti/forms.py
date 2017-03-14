from functools import partial

from django import forms
from django.contrib.admin.sites import site
from django.utils import timezone

# Pomanjkljivosti
from .models import Pomanjkljivost

# Deli
from eda5.deli.widgets import ProjektnoMestoManyToManyRawIdWidget

DateInput = partial(forms.DateInput, {'class': 'datepicker'})
TimeInput = partial(forms.TimeInput, {'class': 'timepicker'})



class PomanjkljivostCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PomanjkljivostCreateForm, self).__init__(*args, **kwargs)

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
        ugotovljeno_dne = timezone.now().date()
        self.initial['ugotovljeno_dne'] = ugotovljeno_dne

        # Prijavo želim oddati kot anonimen
        self.initial['prijavil_text'] = 'Hočem ostati anonimen.'

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
            
            # za uporabnika
            'oznaka',
            'opis_text',
            'prijavil_text',
            'ugotovljeno_dne',
            'element_text',
            'lokacija_text',
        )
        widgets = {
            'ugotovljeno_dne': DateInput(),
        }




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
        ugotovljeno_dne = timezone.now().date()
        self.initial['ugotovljeno_dne'] = ugotovljeno_dne

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
            'opis',
            'prijavil_text',
            'ugotovljeno_dne',
            'prioriteta',
            # element se doda ločeno z widgetom za many-to-many
        )
        widgets = {
            'ugotovljeno_dne': DateInput(),
        }


class PomanjkljivostLikvidirajPodZahtevek(forms.ModelForm):

    class Meta:
        model = Pomanjkljivost
        fields = (

            # dodatno samo za administratorja
            'naziv',
            'opis',
            'prioriteta',
            # element se doda ločeno z widgetom za many-to-many
        )


class PomanjkljivostIzbiraFrom(forms.Form):

    def __init__(self, *args, **kwargs):
        super(PomanjkljivostIzbiraFrom, self).__init__(*args, **kwargs)

        # nastavimo, da je izbira pomanjkljivosti obvezna
        self.fields['pomanjkljivost'].required = True

    # definiramo atribut v formu
    pomanjkljivost = forms.ModelChoiceField(
        queryset=Pomanjkljivost.objects.filter(zahtevek__isnull=True))


class PomanjkljivostElementUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Pomanjkljivost
        fields = (
            'element',
        )
        widgets = {
            'element': ProjektnoMestoManyToManyRawIdWidget(model._meta.get_field('element').rel, site),
        }



