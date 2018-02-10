from django import forms

from .models import ObdobjeLeto, ObdobjeMesec

from django.db.models import Q


class ObdobjeLetoCreateForm(forms.ModelForm):

    class Meta:
        model = ObdobjeLeto
        fields = (
            'oznaka',
        )


class ObdobjeMesecCreateForm(forms.ModelForm):

    class Meta:
        model = ObdobjeMesec
        fields = (
            'oznaka',
            'naziv',
        )



class OsnovnaKombinacijaSearchForm(forms.Form):

    no_filter = 0
    opened = 1
    closed = 2
    dogodki = 3

    STATUS = (
        (no_filter, ''),
        (closed, 'zaključeni'),
        (dogodki, 'z dogodki'),
        (opened, 'v reševanju'),
    )

    oznaka = forms.CharField(label='oznaka', required=False)
    naziv = forms.CharField(label='naziv', required=False)
    status = forms.MultipleChoiceField(choices=STATUS)


    # začetne nastavitve prikazanega "form"
    def __init__(self, *args, **kwargs):
        super(OsnovnaKombinacijaSearchForm, self).__init__(*args, **kwargs)
        # na začetku so okenca za vnos filtrov prazna
        self.initial['oznaka'] = ""
        self.initial['naziv'] = ""
        self.initial['status'] = 0


    def filter_queryset(self, request, queryset):

        oznaka = self.cleaned_data['oznaka']
        naziv = self.cleaned_data['naziv']
        status = self.cleaned_data['status']

        print(status)

        # filtriranje samo po oznaki
        if oznaka:
            queryset = queryset.filter(oznaka__icontains=oznaka)

        if naziv:
            queryset = queryset.filter(naziv__icontains=naziv)


        if '2' in status:
            status_zakljuceni = 4
            queryset = queryset.filter(status=status_zakljuceni)

        if '3' in status:
            queryset = queryset.filter(dogodek__isnull=False)



        return queryset
