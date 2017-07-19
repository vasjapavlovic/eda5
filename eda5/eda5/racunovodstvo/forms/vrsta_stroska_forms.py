from django import forms

from ..models import Konto, PodKonto, SkupinaVrsteStroska, VrstaStroska


class SkupinaVrsteStroskaCreateForm(forms.ModelForm):

    class Meta:
        model = SkupinaVrsteStroska
        fields = (
            'oznaka',
            'naziv',
            'zap_st',
            'skupina',
        )


class VrstaStroskaCreateForm(forms.ModelForm):

    class Meta:
        model = VrstaStroska
        fields = (
            'oznaka',
            'naziv',
            'zap_st',
            'skupina',
        )


class VrstaStroskaIzbiraForm(forms.Form):

    konto = forms.ModelChoiceField(queryset=Konto.objects.all())
    podkonto = forms.ModelChoiceField(queryset=PodKonto.objects.all())
    skupina_vrste_stroska = forms.ModelChoiceField(queryset=SkupinaVrsteStroska.objects.all())
    vrsta_stroska = forms.ModelChoiceField(queryset=VrstaStroska.objects.all())

    # za filtriranje
    konto_hidden = forms.ModelChoiceField(queryset=Konto.objects.all())
    podkonto_hidden = forms.ModelChoiceField(queryset=PodKonto.objects.all())
    skupina_vrste_stroska_hidden = forms.ModelChoiceField(queryset=SkupinaVrsteStroska.objects.all())
    vrsta_stroska_hidden = forms.ModelChoiceField(queryset=VrstaStroska.objects.all())

    def __init__(self, *args, **kwargs):

        davcna_klasifikacija = kwargs.pop('davcna_klasifikacija')

        super(VrstaStroskaIzbiraForm, self).__init__(*args, **kwargs)

        # filter
        self.fields['konto_hidden'].required = False
        self.fields['podkonto_hidden'].required = False
        self.fields['skupina_vrste_stroska_hidden'].required = False
        self.fields['vrsta_stroska_hidden'].required = False

        # 0=Podjetje, 1=Razdelilnik

        if davcna_klasifikacija == 0:
            self.fields['konto'].queryset = Konto.objects.filter(oznaka='E')

        if davcna_klasifikacija == 1:
            self.fields['konto'].queryset = Konto.objects.exclude(oznaka='E')
