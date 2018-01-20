
from django import forms
from django.forms import BaseModelFormSet
from django.forms import modelformset_factory
from django.forms.models import inlineformset_factory


from .models import Plan
from .models import PlaniranoOpravilo
from .models import PlanAktivnost
from .models import PlanKontrolaSkupina
from .models import PlanKontrolaSpecifikacija
from .models import PlanKontrolaSpecifikacijaOpcijaSelect



from django.contrib.admin.sites import site
from eda5.deli.widgets import ProjektnoMestoForeignKeyRawIdWidget, ProjektnoMestoManyToManyRawIdWidget






class PlanCreateform(forms.ModelForm):

    class Meta:
        model = Plan
        fields = (
            'oznaka',
            'naziv',
            'zap_st',
            'opis',
            'sklop',
        )


class PlaniranoOpraviloCreateform(forms.ModelForm):

    class Meta:
        model = PlaniranoOpravilo
        fields = (
            'oznaka',
            'naziv',
            'namen',
            'obseg',
            'perioda_predpisana_enota',
            'perioda_predpisana_enota_kolicina',
            'perioda_predpisana_kolicina_na_enoto',
            'datum_prve_izvedbe',
            'opomba',
            'zmin'
        )

class PlaniranoOpraviloUpdateForm(forms.ModelForm):

    class Meta:
        model = PlaniranoOpravilo
        fields = (
            'naziv',
            'namen',
            'obseg',
            'perioda_predpisana_enota',
            'perioda_predpisana_enota_kolicina',
            'perioda_predpisana_kolicina_na_enoto',
            'opomba',
            'zmin',
        )




class PlanAktivnostCreateForm(forms.ModelForm):


    class Meta:
        model = PlanAktivnost
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



class PlanKontrolaSkupinaCreateForm(forms.ModelForm):


    class Meta:
        model = PlanKontrolaSkupina
        fields = (
            'naziv',
            'zap_st',
            'status',
        )


class PlanKontrolaSpecifikacijaCreateForm(forms.ModelForm):


    class Meta:
        model = PlanKontrolaSpecifikacija
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



class PlanKontrolaSpecifikacijaOpcijaSelectCreateForm(forms.ModelForm):

    class Meta:
        model = PlanKontrolaSpecifikacijaOpcijaSelect
        fields = (
            'naziv',
            'zap_st',
            'status',
        )
