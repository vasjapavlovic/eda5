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
from ..forms import postavka_forms
from eda5.arhiv.forms import ArhiviranjeZahtevekForm
from eda5.zaznamki.forms import ZaznamekForm


class PostavkaCreateFromPovprasevanjeView(LoginRequiredMixin, UpdateView):
    model = Povprasevanje
    template_name = "povprasevanje/ponudba/create/create_from_povprasevanje.html"
    fields = ('id', )


    def get_context_data(self, *args, **kwargs):
        context = super(PostavkaCreateFromPovprasevanjeView, self).get_context_data(*args, **kwargs)

        # zahtevek
        context['postavka_create_from_povprasevanje_form'] = postavka_forms.PostavkaCreateForm

        modul_zavihek = Zavihek.objects.get(oznaka="povprasevanje_create")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        # ====================================
        # FORMS
        # ====================================

        postavka_create_from_povprasevanje_form = \
            postavka_forms.PostavkaCreateForm(request.POST or None)

        ''' Vsi forms za vnose so nazačetku neustrezno izpolnjeni.
        Pomembno zaradi načina struktura View-ja '''

        postavka_create_from_povprasevanje_form_is_valid = False

        ###########################################################################
        # PRIDOBIMO PODATKE
        ###########################################################################

        # zahtevek
        povprasevanje = Povprasevanje.objects.get(id=self.get_object().id)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_CREATE")

        # podatki o opravilu
        if postavka_create_from_povprasevanje_form.is_valid():
            oznaka = postavka_create_from_povprasevanje_form_is_valid.cleaned_data['oznaka']
            opis = postavka_create_from_povprasevanje_form_is_valid.cleaned_data['opis']

            # custom validation - postavka se v ponudbi pojavi samo enkrat
            postavka_create_from_povprasevanje_form_is_valid = True

        ''' v primeru, da so zgornji Form-i ustrezno izpolnjeni
        izvrši spodnje ukaze '''

        if postavka_create_from_povprasevanje_form_is_valid == True:
            ###########################################################################
            # UKAZI
            ###########################################################################

            # Izdelamo povprasevanje

            postavka = Postavka.objects.create_postavka(
                oznaka=oznaka,
                opis=opis,
                povprasevanje=povprasevanje,
            )


            # izvedemo preusmeritev

            return HttpResponseRedirect(
                reverse('moduli:povprasevanje:povprasevanje_detail', kwargs={'pk': povprasevanje.pk})
                )

        # če zgornji formi niso ustrezno izpolnjeni

        else:
            return render(request, self.template_name, {
                'postavka_create_from_povprasevanje_form': postavka_create_from_povprasevanje_form,
                'modul_zavihek': modul_zavihek,
                }
            )



class PostavkaUpdateView(UpdateView):
    model = Postavka
    form_class = postavka_forms.PostavkaUpdateForm
    template_name = "povprasevanje/postavka/update/update.html"


    def get_context_data(self, *args, **kwargs):
        context = super(PostavkaUpdateView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="povprasevanje_detail")
        context['modul_zavihek'] = modul_zavihek

        return context