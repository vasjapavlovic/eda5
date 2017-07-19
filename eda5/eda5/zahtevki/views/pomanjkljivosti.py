# Splošno Django
from django.views.generic import UpdateView

# Pomanjkljivosti
from eda5.pomanjkljivosti.models import PomanjkljivostCreateFromZahtevekForm

# Zahtevki
from eda5.zahtevki.models import Zahtevek


class PomanjkljivostCreateFromZahtevekView(UpdateView):

    model = Zahtevek
    template_name = 'pomanjljivosti/pomanjkljivost/create_from_zahtevek.html'
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):

        context = super(PomanjkljivostCreateFromZahtevekView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="pomanjkljivost_create")
        context['modul_zavihek'] = modul_zavihek

        # pomanjkljivost
        context['pomanjkljivost_create_from_zahtevek_form'] = PomanjkljivostCreateFromZahtevekForm

        return context


    def post(self, request, *args, **kwargs):

        ''' Pridobimo instanco zahtevka kjer se pomanjkljivost dodaja '''
        zahtevek = Zahtevek.objects.get(id=self.get_object().id)

        ''' Pridobimo instanco Zavihka '''
        modul_zavihek = Zavihek.objects.get(oznaka="pomanjkljivost_create")

        #FORMS
        pomanjkljivost_create_from_zahtevek_form = PomanjkljivostCreateFromZahtevekForm(request.POST or None)


        ''' Izdelamo pomanjkljivost iz zahtevka '''

        if pomanjkljivost_create_from_zahtevek_form.is_valid():
            oznaka = pomanjkljivost_create_from_zahtevek_form.celaned_data['oznaka']
            naziv = pomanjkljivost_create_from_zahtevek_form.celaned_data['naziv']
            prijavil_text = pomanjkljivost_create_from_zahtevek_form.celaned_data['prijavil_text']
            datum_ugotovitve = pomanjkljivost_create_from_zahtevek_form.celaned_data['datum_ugotovitve']
            element_text = pomanjkljivost_create_from_zahtevek_form.celaned_data['element_text']
            etaza_text = pomanjkljivost_create_from_zahtevek_form.celaned_data['etaza_text']
            lokacija_text = pomanjkljivost_create_from_zahtevek_form.celaned_data['lokacija_text']
            element = pomanjkljivost_create_from_zahtevek_form.celaned_data['element']

            Pomanjkljivost.objects.create_pomanjkljivost(
                oznaka=oznaka,
                naziv=naziv,
                prijavil_text=prijavil_text,
                datum_ugotovitve=datum_ugotovitve,
                element_text=element_text,
                etaza_text=etaza_text,
                lokacija_text=lokacija_text,
                element=element
            )


        ''' v primeru, da so pri vnosu podatkov v form napačne '''
        else:

            return render(request, self.template_name, {
                'pomanjkljivost_create_from_zahtevek_form': pomanjkljivost_create_from_zahtevek_form,
                'modul_zavihek': modul_zavihek,
                }
            )


        ''' po končanem vnosu se izvede preusmeritev '''

        return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk}))




