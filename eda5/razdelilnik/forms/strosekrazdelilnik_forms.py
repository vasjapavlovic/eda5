# Python
from functools import partial

# Django
from django import forms
from django.db.models import Q

# Models
from ..models import StrosekRazdelilnik, Razdelilnik
from eda5.racunovodstvo.models import Racun, Strosek

DateInput = partial(forms.DateInput, {'class': 'datepicker'})
TimeInput = partial(forms.TimeInput, {'class': 'timepicker'})



class StrosekRazdelilnikUpdateRazdeliForm(forms.ModelForm):
        
    class Meta:
        model = StrosekRazdelilnik
        fields = (
            'is_razdeljen',
            'razdeljen_datum',
        )
        widgets = {
            'razdeljen_datum': DateInput(),
        }
