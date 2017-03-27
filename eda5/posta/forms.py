from functools import partial

from django import forms
from django.db.models import Q
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
    def __init__(self, *args, **kwargs):
        super(DokumentCreateForm, self).__init__(*args, **kwargs)

        self.fields['avtor'].widget.attrs['disabled'] = True
        self.fields['naslovnik'].widget.attrs['disabled'] = True


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




# SEARCH FORMS

class DokumentSearchForm(forms.Form):
    oznaka = forms.CharField(label='oznaka', required=False)
    naziv = forms.CharField(label='naziv', required=False)

    # začetne nastavitve prikazanega "form"
    def __init__(self, *args, **kwargs):
        super(DokumentSearchForm, self).__init__(*args, **kwargs)
        # na začetku so okenca za vnos filtrov prazna
        self.initial['oznaka'] = ""
        self.initial['naziv'] = ""

    def filter_queryset(self, request, queryset):

        oznaka_filter = self.cleaned_data['oznaka']
        naziv_filter = self.cleaned_data['naziv']

        # filtriranje samo po oznaki
        if oznaka_filter and not naziv_filter:
            return queryset.filter(
                Q(oznaka__icontains=oznaka_filter)
            )

        # filtriranje ostalo
        if naziv_filter and not oznaka_filter:
            return queryset.filter(
                Q(avtor__kratko_ime__icontains=naziv_filter) |
                Q(avtor__davcna_st__icontains=naziv_filter) |
                Q(naslovnik__davcna_st__icontains=naziv_filter) |
                Q(naslovnik__kratko_ime__icontains=naziv_filter) |
                Q(naziv__icontains=naziv_filter)
            )
        

        # uporabnik filtrira po kratkem imenu in naslovu partnerja
        if oznaka_filter and naziv_filter:
            return queryset.filter(
                (
                    Q(oznaka__icontains=oznaka_filter)
                ) &
                (
                    Q(avtor__kratko_ime__icontains=naziv_filter) |
                    Q(avtor__davcna_st__icontains=naziv_filter) |
                    Q(naslovnik__davcna_st__icontains=naziv_filter) |
                    Q(naslovnik__kratko_ime__icontains=naziv_filter) |
                    Q(naziv__icontains=naziv_filter)
                )
            )

        return queryset
