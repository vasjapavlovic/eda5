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
from ..forms import ponudba_forms
from eda5.arhiv.forms import ArhiviranjeZahtevekForm
from eda5.zaznamki.forms import ZaznamekForm


class PonudbaCreateFromPovprasevanjeView(LoginRequiredMixin, UpdateView):
    model = Povprasevanje
    template_name = "povprasevanje/ponudba/create/create_from_povprasevanje.html"
    fields = ('id', )


    def get_context_data(self, *args, **kwargs):
        context = super(PonudbaCreateFromPovprasevanjeView, self).get_context_data(*args, **kwargs)

        # zahtevek
        context['ponudba_create_from_povprasevanje_form'] = ponudba_forms.PonudbaCreateForm

        modul_zavihek = Zavihek.objects.get(oznaka="povprasevanje_create")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        # ====================================
        # FORMS
        # ====================================

        ponudba_create_from_povprasevanje_form = \
            ponudba_forms.PonudbaCreateForm(request.POST or None)

        ''' Vsi forms za vnose so nazačetku neustrezno izpolnjeni.
        Pomembno zaradi načina struktura View-ja '''

        ponudba_create_from_povprasevanje_form_is_valid = False

        ###########################################################################
        # PRIDOBIMO PODATKE
        ###########################################################################

        # zahtevek
        povprasevanje = Povprasevanje.objects.get(id=self.get_object().id)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_CREATE")

        # podatki o opravilu
        if ponudba_create_from_povprasevanje_form.is_valid():
            oznaka = ponudba_create_from_povprasevanje_form.cleaned_data['oznaka']
            ponudnik = ponudba_create_from_povprasevanje_form.cleaned_data['ponudnik']

            # custom validation - postavka se v ponudbi pojavi samo enkrat
            if Ponudba.objects.filter(povprasevanje=povprasevanje, ponudnik=ponudnik).exists():
                # opozorilo
                messages.error(self.request, "Ta ponudnik v povpraševanju že obstaja.")
                #preusmeritev
                return HttpResponseRedirect(reverse('moduli:povprasevanje:povprasevanje_detail', 
                    kwargs={'pk': povprasevanje.pk }))

            else:
                ponudba_create_from_povprasevanje_form_is_valid = True

        ''' v primeru, da so zgornji Form-i ustrezno izpolnjeni
        izvrši spodnje ukaze '''

        if ponudba_create_from_povprasevanje_form_is_valid == True:
            ###########################################################################
            # UKAZI
            ###########################################################################

            # Izdelamo povprasevanje

            ponudba = Ponudba.objects.create_ponudba(
                oznaka=oznaka,
                ponudnik=ponudnik,
                povprasevanje=povprasevanje,
            )


            # izvedemo preusmeritev

            return HttpResponseRedirect(
                reverse('moduli:povprasevanje:povprasevanje_detail', kwargs={'pk': povprasevanje.pk})
                )

        # če zgornji formi niso ustrezno izpolnjeni

        else:
            return render(request, self.template_name, {
                'ponudba_create_from_povprasevanje_form': ponudba_create_from_povprasevanje_form,
                'modul_zavihek': modul_zavihek,
                }
            )



class PonudbaUpdateView(UpdateView):
    model = Ponudba
    form_class = ponudba_forms.PonudbaUpdateForm
    template_name = "povprasevanje/ponudba/update/update.html"


    def get_context_data(self, *args, **kwargs):
        context = super(PonudbaUpdateView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="povprasevanje_detail")
        context['modul_zavihek'] = modul_zavihek

        return context