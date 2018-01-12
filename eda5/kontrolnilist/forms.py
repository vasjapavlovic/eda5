from django import forms
from django.forms import BaseModelFormSet
from django.forms import modelformset_factory
from django.forms.models import inlineformset_factory


from .models import Aktivnost
from .models import KontrolaSpecifikacija
from .models import KontrolaSpecifikacijaOpcijaSelect
from .models import KontrolaVrednost




class AktivnostCreateForm(forms.ModelForm):

    class Meta:
        model = Aktivnost
        fields = (
            'oznaka',
            'naziv',
            'opis',
        )


    def __init__(self, *args, **kwargs):
        # kwargs pop
        super(AktivnostCreateForm, self).__init__(*args, **kwargs)
        # ostalo
        self.fields['naziv'].required = True


class KontrolaSpecifikacijaCreateForm(forms.ModelForm):

    class Meta:
        model = KontrolaSpecifikacija
        fields = (
            'oznaka',
            'naziv',
            'opis',
            'vrednost_vrsta',
        )

KontrolaSpecifikacijaFormSet = inlineformset_factory(
    Aktivnost,
    KontrolaSpecifikacija,
    form=KontrolaSpecifikacijaCreateForm,
    extra=1)


class BaseKontrolaVrednostUpdateFormSetOblika01(BaseModelFormSet):
    '''
    base form set potrebujemo, da izvedemo razporejanje (ordering)
    glede na naše želje
    '''
    def __init__(self, *args, **kwargs):
        delovninalog = kwargs.pop('delovninalog')
        super(BaseKontrolaVrednostUpdateFormSetOblika01, self).__init__(*args, **kwargs)

        queryset = KontrolaVrednost.objects.filter(delovni_nalog=delovninalog)
        queryset = queryset.order_by(
            # glede na etažo
            '-projektno_mesto__lokacija__etaza__elevation',
            # glede na prostor
            'projektno_mesto__lokacija__prostor',
            # glede na projektno mesto
            'projektno_mesto',
            # glede na aktivnost
            'kontrola_specifikacija__aktivnost__oznaka',
            # glede na specifikacijo kontrole
            'kontrola_specifikacija__oznaka',
            )

        self.queryset = queryset




class KontrolaVrednostUpdateForm(forms.ModelForm):
    '''
    Form za update vrednosti - izpolnjevanje e-kontrolnega lista
    '''

    def __init__(self, *args, **kwargs):
        super(KontrolaVrednostUpdateForm, self).__init__(*args, **kwargs)

        # če je izbrana vrsta_vrednosti = SELECT
        if self.instance.kontrola_specifikacija.vrednost_vrsta == 3:
            self.fields['vrednost_select'].queryset = KontrolaSpecifikacijaOpcijaSelect.objects.filter(
                kontrola_specifikacija=self.instance.kontrola_specifikacija)


    class Meta:
        model = KontrolaVrednost
        fields = (
            'vrednost_select',
            'vrednost_text',
            'vrednost_check',
        )


KontrolaVrednostUpdateFormSetOblika01 = modelformset_factory(
    KontrolaVrednost,
    extra=0,
    form=KontrolaVrednostUpdateForm,
    formset=BaseKontrolaVrednostUpdateFormSetOblika01,

)





class BaseKontrolaVrednostUpdateFormSetOblika02(BaseModelFormSet):
    '''
    base form set potrebujemo, da izvedemo razporejanje (ordering)
    glede na naše želje
    '''
    def __init__(self, *args, **kwargs):
        delovninalog = kwargs.pop('delovninalog')
        super(BaseKontrolaVrednostUpdateFormSetOblika02, self).__init__(*args, **kwargs)

        queryset = KontrolaVrednost.objects.filter(delovni_nalog=delovninalog)
        queryset = queryset.order_by(
            # glede na aktivnost
            'kontrola_specifikacija__aktivnost__oznaka',
            # glede na specifikacijo kontrole
            'kontrola_specifikacija__oznaka',
            # glede na del stavbe
            'projektno_mesto__del_stavbe',
            # glede na projektno mesto
            'projektno_mesto__oznaka',
            )

        self.queryset = queryset


KontrolaVrednostUpdateFormSetOblika02 = modelformset_factory(
    KontrolaVrednost,
    extra=0,
    form=KontrolaVrednostUpdateForm,
    formset=BaseKontrolaVrednostUpdateFormSetOblika02,

)
