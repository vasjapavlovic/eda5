# Django
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
from ..forms import povprasevanje_forms
from eda5.arhiv.forms import ArhiviranjeZahtevekForm
from eda5.zaznamki.forms import ZaznamekForm

class PovprasevanjeCreateFromZahtevekView(LoginRequiredMixin, UpdateView):
    model = Zahtevek
    template_name = "povprasevanje/povprasevanje/create/create_from_zahtevek.html"
    fields = ('id', )


    def get_context_data(self, *args, **kwargs):
        context = super(PovprasevanjeCreateFromZahtevekView, self).get_context_data(*args, **kwargs)

        # zahtevek
        context['povprasevanje_create_from_zahtevek_form'] = povprasevanje_forms.PovprasevanjeCreateFromZahtevekForm

        modul_zavihek = Zavihek.objects.get(oznaka="povprasevanje_create")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        # ====================================
        # FORMS
        # ====================================

        povprasevanje_create_from_zahtevek_form = \
            povprasevanje_forms.PovprasevanjeCreateFromZahtevekForm(request.POST or None)

        ''' Vsi forms za vnose so nazačetku neustrezno izpolnjeni.
        Pomembno zaradi načina struktura View-ja '''

        povprasevanje_create_from_zahtevek_form_is_valid = False

        ###########################################################################
        # PRIDOBIMO PODATKE
        ###########################################################################

        # zahtevek
        zahtevek = Zahtevek.objects.get(id=self.get_object().id)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_CREATE")

        # podatki o opravilu
        if povprasevanje_create_from_zahtevek_form.is_valid():
            oznaka = povprasevanje_create_from_zahtevek_form.cleaned_data['oznaka']
            naziv = povprasevanje_create_from_zahtevek_form.cleaned_data['naziv']
            opis = povprasevanje_create_from_zahtevek_form.cleaned_data['opis']
            datum = povprasevanje_create_from_zahtevek_form.cleaned_data['datum']
            povprasevanje_create_from_zahtevek_form_is_valid = True

        ''' v primeru, da so zgornji Form-i ustrezno izpolnjeni
        izvrši spodnje ukaze '''

        if povprasevanje_create_from_zahtevek_form_is_valid == True:
            ###########################################################################
            # UKAZI
            ###########################################################################

            # Izdelamo povprasevanje

            povprasevanje = Povprasevanje.objects.create_povprasevanje(
                oznaka=oznaka,
                naziv=naziv,
                opis=opis,
                datum=datum,
                zahtevek=zahtevek,
            )


            # spremenimo status povprasevanja v reševanju
            povprasevanje.status = 3
            povprasevanje.save()

            # izvedemo preusmeritev

            return HttpResponseRedirect(
                reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk})
                )

        # če zgornji formi niso ustrezno izpolnjeni

        else:
            return render(request, self.template_name, {
                'povprasevanje_create_from_zahtevek_form': povprasevanje_create_from_zahtevek_form,
                'modul_zavihek': modul_zavihek,
                }
            )


class PovprasevanjeListView(LoginRequiredMixin, ListView):

    model = Povprasevanje
    template_name = "povprasevanje/povprasevanje/list/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PovprasevanjeListView, self).get_context_data(*args, **kwargs)

        # pridobimo instanco izbranega zavihka
        modul_zavihek = Zavihek.objects.get(oznaka="povprasevanje_list")
        context['modul_zavihek'] = modul_zavihek

        # vrnemo context
        return context


class PovprasevanjeDetailView(LoginRequiredMixin, DetailView):
    model = Povprasevanje
    template_name = "povprasevanje/povprasevanje/detail/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PovprasevanjeDetailView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="povprasevanje_detail")
        context['modul_zavihek'] = modul_zavihek

        # ostalo
        postavka_list = Postavka.objects.filter(povprasevanje=self.object.pk).order_by('oznaka')
        context['postavka_list'] = postavka_list


        ponudba_list = Ponudba.objects.filter(povprasevanje=self.object.pk).order_by('oznaka').annotate(
            skupaj_cena=Sum('ponudbapopostavki__vrednost_za_izracun'))
        context['ponudba_list'] = ponudba_list

        return context


class PovprasevanjeZunanjiDetailView(LoginRequiredMixin, DetailView):
    model = Povprasevanje
    template_name = "povprasevanje/povprasevanje/detail-zunanji/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PovprasevanjeZunanjiDetailView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="povprasevanje_detail")
        context['modul_zavihek'] = modul_zavihek

        # ostalo
        postavka_list = Postavka.objects.filter(povprasevanje=self.object.pk).order_by('oznaka')
        context['postavka_list'] = postavka_list


        ponudba_list = Ponudba.objects.filter(povprasevanje=self.object.pk).order_by('oznaka').annotate(
            skupaj_cena=Sum('ponudbapopostavki__vrednost_za_izracun'))
        context['ponudba_list'] = ponudba_list

        return context



class PovprasevanjeUpdateView(UpdateView):
    model = Povprasevanje
    form_class = povprasevanje_forms.PovprasevanjeUpdateForm
    template_name = "povprasevanje/povprasevanje/update/update.html"


    def get_context_data(self, *args, **kwargs):
        context = super(PovprasevanjeUpdateView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="povprasevanje_detail")
        context['modul_zavihek'] = modul_zavihek

        return context