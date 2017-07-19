from django import forms
from django.db.models import Q


from ..models import Podskupina, Skupina, DelStavbe, ProjektnoMesto



class ProjektnoMestoCreateForm(forms.ModelForm):

    class Meta:
        model = ProjektnoMesto
        fields = (
            'oznaka',
            'naziv',
            'funkcija',
            'bim_id',
            'tip_elementa',
            'lokacija',
            'del_stavbe',
        )



class ElementIzbiraForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(ElementIzbiraForm, self).__init__(*args, **kwargs)

        self.fields['skupina'].required = False
        self.fields['podskupina'].required = False
        self.fields['del_stavbe'].required = False

        self.fields['podskupina_hidden'].required = False
        self.fields['del_stavbe_hidden'].required = False
        self.fields['element_hidden'].required = False

    skupina = forms.ModelChoiceField(queryset=Skupina.objects.all())
    podskupina = forms.ModelChoiceField(queryset=Podskupina.objects.all())
    del_stavbe = forms.ModelChoiceField(queryset=DelStavbe.objects.all())

    # za filtriranje
    podskupina_hidden = forms.ModelChoiceField(queryset=Podskupina.objects.all())
    del_stavbe_hidden = forms.ModelChoiceField(queryset=DelStavbe.objects.all())
    element_hidden = forms.ModelChoiceField(queryset=ProjektnoMesto.objects.all())



class ProjektnoMestoSearchForm(forms.Form):
    oznaka = forms.CharField(label='oznaka', required=False)
    naziv = forms.CharField(label='naziv', required=False)

    # začetne nastavitve prikazanega "form"
    def __init__(self, *args, **kwargs):
        super(ProjektnoMestoSearchForm, self).__init__(*args, **kwargs)
        # na začetku so okenca za vnos filtrov prazna
        self.initial['oznaka'] = ""
        self.initial['naziv'] = ""

    def filter_queryset(self, request, queryset):

        oznaka_filter = self.cleaned_data['oznaka']
        naziv_filter = self.cleaned_data['naziv']

        # filtriranje samo po oznaki
        if oznaka_filter and not naziv_filter:
            return queryset.filter(oznaka__icontains=oznaka_filter)

        # filtriranje ostalo
        if naziv_filter and not oznaka_filter:
            return queryset.filter(
                Q(naziv__icontains=naziv_filter) |
                Q(tip_elementa__oznaka__icontains=naziv_filter) |
                Q(tip_elementa__naziv__icontains=naziv_filter) |
                Q(del_stavbe__oznaka__icontains=naziv_filter) |
                Q(del_stavbe__naziv__icontains=naziv_filter) |
                Q(del_stavbe__podskupina__oznaka__icontains=naziv_filter) |
                Q(del_stavbe__podskupina__naziv__icontains=naziv_filter)
                )
        

        # uporabnik filtrira po kratkem imenu in naslovu partnerja
        if oznaka_filter and naziv_filter:
            return queryset.filter(
                Q(oznaka__icontains=oznaka_filter) &
                (
                Q(naziv__icontains=naziv_filter) |
                Q(tip_elementa__oznaka__icontains=naziv_filter) |
                Q(tip_elementa__naziv__icontains=naziv_filter) |
                Q(del_stavbe__oznaka__icontains=naziv_filter) |
                Q(del_stavbe__naziv__icontains=naziv_filter) |
                Q(del_stavbe__podskupina__oznaka__icontains=naziv_filter) |
                Q(del_stavbe__podskupina__naziv__icontains=naziv_filter)
                )
                )

        return queryset