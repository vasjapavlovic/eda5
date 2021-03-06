# Python


# Django
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, UpdateView

# Mixins
from braces.views import LoginRequiredMixin

# Models
from ..models import StrosekRazdelilnik, Razdelilnik
from eda5.arhiv.models import ArhivMesto, Arhiviranje
from eda5.moduli.models import Zavihek
from eda5.racunovodstvo.models import Strosek
from eda5.zaznamki.models import Zaznamek

# Forms
from ..forms.razdelilnik_forms import RazdelilnikSearchForm
from ..forms.strosekrazdelilnik_forms import StrosekRazdelilnikUpdateRazdeliForm
from eda5.arhiv.forms import ArhiviranjeZahtevekForm
from eda5.zaznamki.forms import ZaznamekForm

# Views
from eda5.core.views import FilteredListView



class StrosekRazdelilnikCreateView(UpdateView):
    model = Strosek
    template_name = "razdelilnik/strosekrazdelilnik/create/base.html"
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):
        context = super(StrosekRazdelilnikCreateView, self).get_context_data(*args, **kwargs)

        modul_zavihek = Zavihek.objects.get(oznaka="STROSEKRAZDELILNIK_CREATE")
        context['modul_zavihek'] = modul_zavihek

        # Pridobimo objekt instance = strošek
        strosek = Strosek.objects.get(id=self.get_object().id)
        context['strosek'] = strosek

        # iz request.sessions pridobimo instanco razdelilnika
        # v kateremu bomo obravnavali strošek. Glej
        # razdelilnik:razdelilnik_views:RazdelilnikDetailView
        razdelilnik_data = self.request.session.get('razdelilnik_data', None)
        razdelilnik_pk = razdelilnik_data['razdelilnik_pk']
        razdelilnik = Razdelilnik.objects.get(pk=razdelilnik_pk)
        context['razdelilnik'] = razdelilnik

        return context

    def post(self, request, *args, **kwargs):

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="STROSEKRAZDELILNIK_CREATE")

        # Pridobimo objekt instance = strošek
        strosek = Strosek.objects.get(id=self.get_object().id)

        # iz request.sessions pridobimo instanco razdelilnika
        # v kateremu bomo obravnavali strošek. Glej
        # razdelilnik:razdelilnik_views:RazdelilnikDetailView
        razdelilnik_data = request.session.get('razdelilnik_data', None)
        razdelilnik_pk = razdelilnik_data['razdelilnik_pk']
        razdelilnik = Razdelilnik.objects.get(pk=razdelilnik_pk)


        # proces vezave stroška na razdelilnik kjer se bo razdelil
        # v primeru, da se uporabnik premisli
        if "cancel" in request.POST:
            return HttpResponseRedirect(reverse('moduli:razdelilnik:razdelilnik_detail', kwargs={'pk': razdelilnik.pk}))

        # Strošek vežemo na razdelilnik kjer se bo razdelil
        else:
            StrosekRazdelilnik.objects.create_strosekrazdelilnik(
                razdelilnik=razdelilnik,
                strosek=strosek,
            )
            return HttpResponseRedirect(reverse('moduli:razdelilnik:razdelilnik_detail', kwargs={'pk': razdelilnik.pk}))

        

class StrosekRazdelilnikUpdateRazdeliView(LoginRequiredMixin, UpdateView):
    model = StrosekRazdelilnik
    form_class = StrosekRazdelilnikUpdateRazdeliForm
    template_name = "razdelilnik/strosekrazdelilnik/update/update.html"

    def get_context_data(self, *args, **kwargs):
        context = super(StrosekRazdelilnikUpdateRazdeliView, self).get_context_data(*args, **kwargs)

        modul_zavihek = Zavihek.objects.get(oznaka="STROSEKRAZDELILNIK_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context