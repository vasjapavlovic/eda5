from django import forms
from django.forms import BaseModelFormSet
from django.forms import modelformset_factory
from django.forms.models import inlineformset_factory


from .models import Aktivnost
from .models import KontrolaSpecifikacija
from .models import KontrolaSpecifikacijaOpcijaSelect
from .models import KontrolaVrednost

from django.contrib.admin.sites import site
from eda5.deli.widgets import ProjektnoMestoForeignKeyRawIdWidget, ProjektnoMestoManyToManyRawIdWidget




class AktivnostCreateForm(forms.ModelForm):

    class Meta:
        model = Aktivnost
        fields = (
            'oznaka',
            'naziv',
            'opis',
            'perioda_enota',
            'perioda_enota_kolicina',
            'perioda_kolicina_na_enoto',
            'zap_st',
            'status',

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
            'projektno_mesto',
            'zap_st',
            'status',
        )
        widgets = {
            'projektno_mesto': ProjektnoMestoManyToManyRawIdWidget(model._meta.get_field('projektno_mesto').rel, site),
        }




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
            'kontrola_specifikacija__kontrola_skupina__aktivnost__zap_st',
            'kontrola_specifikacija__kontrola_skupina__aktivnost__oznaka',
            # glede na skupino kontrol
            'kontrola_specifikacija__kontrola_skupina__zap_st',
            'kontrola_specifikacija__kontrola_skupina__oznaka',
            # glede na specifikacijo kontrole
            'kontrola_specifikacija__zap_st',
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
            'vrednost_number',
            'vrednost_yes_no',
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
            'kontrola_specifikacija__kontrola_skupina__aktivnost__zap_st',
            'kontrola_specifikacija__kontrola_skupina__aktivnost__oznaka',
            # glede na del stavbe
            'projektno_mesto__del_stavbe',
            # glede na projektno mesto
            'projektno_mesto__oznaka',
            # glede na skupino kontrol
            'kontrola_specifikacija__kontrola_skupina__zap_st',
            'kontrola_specifikacija__kontrola_skupina__oznaka',
            # glede na specifikacijo kontrole
            'kontrola_specifikacija__zap_st',
            'kontrola_specifikacija__oznaka',
            )

        self.queryset = queryset


KontrolaVrednostUpdateFormSetOblika02 = modelformset_factory(
    KontrolaVrednost,
    extra=0,
    form=KontrolaVrednostUpdateForm,
    formset=BaseKontrolaVrednostUpdateFormSetOblika02,

)
