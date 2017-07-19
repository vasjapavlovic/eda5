from functools import partial

from django import forms
from django.contrib.admin.sites import site  # popup
from django.utils import timezone


# Models
from ..models import Sestanek

# Forms

# Widgets
from eda5.partnerji.widgets import PartnerSelectWithPop, PartnerMultipleSelectWithPop, PartnerForeignKeyRawIdWidget
from eda5.partnerji.widgets import OsebaManyToManyRawIdWidget

DateInput = partial(forms.DateInput, {'class': 'datepicker'})
TimeInput = partial(forms.TimeInput, {'class': 'timepicker'})

class SestanekCreateFromZahtevekForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SestanekCreateFromZahtevekForm, self).__init__(*args, **kwargs)

        #=========================================================
        # oznaka
        #---------------------------------------------------------
        # 2017-1, 2017-2, ...
        leto = timezone.now().date().year

        try:
            st_vnosov = Sestanek.objects.count()
            zap_st = st_vnosov + 1
        except:
            # pri prvi reklamaciji dodelimo št. 1 : count =0
            zap_st = 1

        nova_oznaka = "%s-%s" % (leto, zap_st)
        self.initial['oznaka'] = nova_oznaka
        self.fields['oznaka'].widget.attrs['readonly'] = True

        #======================================================
        # datum
        #-----------------------------------------------------
        self.initial['datum'] = timezone.now().date()


    class Meta:
        model = Sestanek
        fields = (
            'oznaka',
            'naziv',
            'opis',
            'datum',
            'sklicatelj',
        )
        widgets = {
            'datum': DateInput(),
            'sklicatelj': PartnerForeignKeyRawIdWidget(model._meta.get_field('sklicatelj').rel, site),
        }


class SestanekUpdateForm(forms.ModelForm):

    class Meta:
        model = Sestanek
        fields = (
            'oznaka',
            'naziv',
            'opis',
            'datum',
            'sklicatelj',
            'prisotni',
            'status',
        )
        widgets = {
            'datum': DateInput(),
            'sklicatelj': PartnerForeignKeyRawIdWidget(model._meta.get_field('sklicatelj').rel, site),
            'prisotni': OsebaManyToManyRawIdWidget(model._meta.get_field('prisotni').rel, site),
        }

class SestanekPrisotniUpdateForm(forms.ModelForm):

    class Meta:
        model = Sestanek
        fields = (
            'prisotni',
        )
        widgets = {
            'prisotni': OsebaManyToManyRawIdWidget(model._meta.get_field('prisotni').rel, site),
        }