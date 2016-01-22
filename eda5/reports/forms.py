from django import forms

from eda5.racunovodstvo.models import SkupinaVrsteStroska


class ReportForm(forms.Form):

    q = forms.ModelMultipleChoiceField(
        queryset=SkupinaVrsteStroska.objects.filter(skupina__skupina__oznaka="O"),
        widget=forms.CheckboxSelectMultiple,
    )
