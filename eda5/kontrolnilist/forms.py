from django import forms
from django.forms.models import inlineformset_factory

from .models import Aktivnost
from .models import KontrolaSpecifikacija



class AktivnostCreateForm(forms.ModelForm):

    class Meta:
        model = Aktivnost
        fields = (
            'oznaka',
            'naziv',
            'opis',
        )
        widgets = {

        }

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
    extra=2)


# class KontrolaVrednostUpdateForm(forms.ModelForm):
#     pass





# # FILTRIRAMO FORMSET - KATERI FORMSI SE PRIKAŽEJO
# class BaseVrednostFormSet(BaseModelFormSet):
#     def __init__(self, *args, **kwargs):
#         '''
#         filtriramo formset glede na delovninalog v kateremu se kontrolni list obravnava,
#         Razporedimo obstoječi queryset zaradi uporabe regroup opcije
#         v templates.
#         '''
#         delovninalogid = kwargs.pop('delovninalogid')
#
#         super(BaseVrednostFormSet, self).__init__(*args, **kwargs)
#
#         queryset = ParameterAktivnostiVrednost.objects.filter(delovninalog=delovninalogid)
#
#         queryset = queryset.order_by(
#             # glede na etažo
#             '-projektno_mesto__lokacija__etaza__elevation',
#             # glede na prostor
#             'projektno_mesto__lokacija__prostor',
#             # glede na projektno mesto
#             'projektno_mesto',
#             # glede na aktivnost
#             'parameter_atkivnosti_specifikacija__aktivnost__oznaka',
#             # glede na specifikacijo parametra
#             'parameter_atkivnosti_specifikacija__oznaka',
#             )
#
#         self.queryset = queryset
