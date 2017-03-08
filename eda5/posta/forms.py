from functools import partial

from django import forms
from django.utils import timezone
from django.contrib.admin.sites import site  # popup

from .models import Aktivnost, Dokument, SkupinaDokumenta, VrstaDokumenta

from eda5.partnerji.widgets import PartnerSelectWithPop, PartnerMultipleSelectWithPop, PartnerForeignKeyRawIdWidget

DateInput = partial(forms.DateInput, {'class': 'datepicker'})
TimeInput = partial(forms.TimeInput, {'class': 'timepicker'})


class AktivnostCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AktivnostCreateForm, self).__init__(*args, **kwargs)

        datum_aktivnosti = timezone.now().date()
        self.initial['datum_aktivnosti'] = datum_aktivnosti

    class Meta:
        model = Aktivnost
        fields = (
            'datum_aktivnosti',
            
        )
        widgets = {
            'datum_aktivnosti': DateInput(),
        }


class SkupinaDokumentaIzbiraForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(SkupinaDokumentaIzbiraForm, self).__init__(*args, **kwargs)
        
        self.fields['skupina_dokumenta'].required = False

    skupina_dokumenta = forms.ModelChoiceField(queryset=SkupinaDokumenta.objects.all())
    vrsta_dokumenta_hidden = forms.ModelChoiceField(queryset=VrstaDokumenta.objects.all())


class DokumentCreateForm(forms.ModelForm):

    # avtor = forms.IntegerField(widget=SelectWithPop)

    class Meta:
        model = Dokument
        fields = (
            'vrsta_dokumenta',
            'avtor',
            'naslovnik',
            'oznaka',
            'naziv',
            'datum_dokumenta',
            'kraj_izdaje',
            'priponka',
        )
        widgets = {
            'datum_dokumenta': DateInput(),
            'avtor': PartnerForeignKeyRawIdWidget(model._meta.get_field('avtor').rel, site),
            'naslovnik': PartnerForeignKeyRawIdWidget(model._meta.get_field('naslovnik').rel, site),
        }


class SkupinaDokumentaCreateForm(forms.ModelForm):

    class Meta:
        model = SkupinaDokumenta
        fields = (
            'oznaka',
            'naziv',
            'zap_st',
        )


class VrstaDokumentaCreateForm(forms.ModelForm):

    class Meta:
        model = VrstaDokumenta
        fields = (
            'oznaka',
            'naziv',
            'zap_st',
            'skupina',
        )
