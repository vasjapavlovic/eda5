from django import forms


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