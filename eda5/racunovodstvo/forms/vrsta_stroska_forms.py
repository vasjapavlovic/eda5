from django import forms


from ..models import SkupinaVrsteStroska, VrstaStroska


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

    skupina_vrste_stroska = forms.ModelChoiceField(queryset=SkupinaVrsteStroska.objects.all())
    vrsta_stroska = forms.ModelChoiceField(queryset=VrstaStroska.objects.all())

    # za filtriranje
    skupina_vrste_stroska_hidden = forms.ModelChoiceField(queryset=SkupinaVrsteStroska.objects.all())
    vrsta_stroska_hidden = forms.ModelChoiceField(queryset=VrstaStroska.objects.all())
