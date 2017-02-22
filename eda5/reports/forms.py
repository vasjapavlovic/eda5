from django import forms
from django.utils.html import conditional_escape, mark_safe
from django.utils.encoding import smart_text

from eda5.racunovodstvo.models import SkupinaVrsteStroska
from eda5.etaznalastnina.models import Program


class ReportForm(forms.Form):

    q = forms.ModelMultipleChoiceField(
        queryset=SkupinaVrsteStroska.objects.filter(skupina__skupina__oznaka="O"),
        widget=forms.CheckboxSelectMultiple,
    )


class FormatForm(forms.Form):
    FORMAT_CHOICES = (
        ('pdf', 'PDF'),
        ('docx', 'MS Word'),
        ('html', 'HTML'),
        ('xlsx', 'MS Excel'),
    )

    format_field = forms.ChoiceField(choices=FORMAT_CHOICES)


class DeliSeznamFilterForm(forms.Form):

    program = forms.ModelMultipleChoiceField(
        queryset=Program.objects.all())