# Django
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db.models import Count, Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DetailView, UpdateView, ListView

# Mixins
from braces.views import LoginRequiredMixin

# Models
from ..models import Povprasevanje, Postavka, Ponudba, PonudbaPoPostavki
from eda5.arhiv.models import ArhivMesto, Arhiviranje
from eda5.moduli.models import Zavihek
from eda5.partnerji.models import Oseba, Partner
from eda5.zahtevki.models import Zahtevek
from eda5.zaznamki.models import Zaznamek

# Forms
from ..forms import ponudbapopostavki_forms
from eda5.arhiv.forms import ArhiviranjeZahtevekForm
from eda5.zaznamki.forms import ZaznamekForm

class PonudbaPoPostavkiCreateFromPovprasevanjeView(LoginRequiredMixin, UpdateView):
    model = Ponudba
    template_name = "povprasevanje/ponudbapopostavki/create/create_from_povprasevanje.html"
    fields = ('id', )


    def get_context_data(self, *args, **kwargs):
        context = super(PonudbaPoPostavkiCreateFromPovprasevanjeView, self).get_context_data(*args, **kwargs)

        # zahtevek
        context['ponudbapopostavki_create_from_povprasevanje_form'] = ponudbapopostavki_forms.PonudbaPoPostavkiCreateForm

        modul_zavihek = Zavihek.objects.get(oznaka="povprasevanje_create")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        # ====================================
        # FORMS
        # ====================================

        ponudbapopostavki_create_from_povprasevanje_form = \
            ponudbapopostavki_forms.PonudbaPoPostavkiCreateForm(request.POST or None)

        ''' Vsi forms za vnose so nazačetku neustrezno izpolnjeni.
        Pomembno zaradi načina struktura View-ja '''

        ponudbapopostavki_create_from_povprasevanje_form_is_valid = False

        ###########################################################################
        # PRIDOBIMO PODATKE
        ###########################################################################

        # zahtevek
        ponudba = Ponudba.objects.get(id=self.get_object().id)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_CREATE")

        # podatki o opravilu
        if ponudbapopostavki_create_from_povprasevanje_form.is_valid():
            postavka = ponudbapopostavki_create_from_povprasevanje_form.cleaned_data['postavka']
            vrednost_za_izracun = ponudbapopostavki_create_from_povprasevanje_form.cleaned_data['vrednost_za_izracun']
            vrednost_opis = ponudbapopostavki_create_from_povprasevanje_form.cleaned_data['vrednost_opis']

            # custom validation - postavka se v ponudbi pojavi samo enkrat
            if PonudbaPoPostavki.objects.filter(postavka=postavka, ponudba=ponudba).exists():
                # opozorilo
                messages.error(self.request, "Ta postavka v ponudbi že obstaja.")
                #preusmeritev
                return HttpResponseRedirect(reverse('moduli:povprasevanje:povprasevanje_detail', 
                    kwargs={'pk': ponudba.povprasevanje.pk }))

            else:
                ponudbapopostavki_create_from_povprasevanje_form_is_valid = True

        ''' v primeru, da so zgornji Form-i ustrezno izpolnjeni
        izvrši spodnje ukaze '''

        if ponudbapopostavki_create_from_povprasevanje_form_is_valid == True:
            ###########################################################################
            # UKAZI
            ###########################################################################

            # Izdelamo povprasevanje

            ponudbapopostavki = PonudbaPoPostavki.objects.create_ponudbapopostavki(
                vrednost_za_izracun=vrednost_za_izracun,
                vrednost_opis=vrednost_opis,
                postavka=postavka,
                ponudba=ponudba,
            )


            # izvedemo preusmeritev

            return HttpResponseRedirect(
                reverse('moduli:povprasevanje:povprasevanje_detail', kwargs={'pk': ponudba.povprasevanje.pk})
                )

        # če zgornji formi niso ustrezno izpolnjeni

        else:
            return render(request, self.template_name, {
                'ponudbapopostavki_create_from_povprasevanje_form': ponudbapopostavki_create_from_povprasevanje_form,
                'modul_zavihek': modul_zavihek,
                }
            )


class PonudbaPoPostavkiUpdateView(UpdateView):
    model = PonudbaPoPostavki
    form_class = ponudbapopostavki_forms.PonudbaPoPostavkiUpdateForm
    template_name = "povprasevanje/povprasevanje/update/update.html"


    def get_context_data(self, *args, **kwargs):
        context = super(PonudbaPoPostavkiUpdateView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="povprasevanje_detail")
        context['modul_zavihek'] = modul_zavihek

        return context