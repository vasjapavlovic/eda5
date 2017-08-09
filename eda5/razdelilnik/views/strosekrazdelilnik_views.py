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
from ..forms.strosekrazdelilnik_forms import StrosekRazdelilnikCreateForm, StrosekRazdelilnikUpdateForm
from eda5.arhiv.forms import ArhiviranjeZahtevekForm
from eda5.zaznamki.forms import ZaznamekForm

# Views
from eda5.core.views import FilteredListView



class StrosekRazdelilnikCreateRazdelilnikView(UpdateView):
    model = Razdelilnik
    template_name = "razdelilnik/strosekrazdelilnik/create/base.html"
    fields = ('id', )


    def post(self, request, *args, **kwargs):

        razdelilnik = Razdelilnik.objects.get(id=self.get_object().id)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="STROSEKRAZDELILNIK_CREATE")


        StrosekRazdelilnik.objects.create_strosekrazdelilnik(
            razdelilnik=razdelilnik,
            strosek=strosek,
        )



        return HttpResponseRedirect(reverse('moduli:razdelilnik:razdelilnik_detail', kwargs={'pk': razdelilnik.pk}))




class StrosekRazdelilnikCreateView(UpdateView):
    model = Strosek
    template_name = "razdelilnik/strosekrazdelilnik/create/base.html"
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):
        context = super(StrosekRazdelilnikCreateView, self).get_context_data(*args, **kwargs)

        modul_zavihek = Zavihek.objects.get(oznaka="STROSEKRAZDELILNIK_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        # object
        strosek = Strosek.objects.get(id=self.get_object().id)
        print(strosek)
        razdelilnik_data = request.session.get('razdelilnik_data', None)
        razdelilnik_pk = razdelilnik_data['razdelilnik_pk']
        razdelilnik = Razdelilnik.objects.get(pk=razdelilnik_pk)
        print(razdelilnik)
        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="STROSEKRAZDELILNIK_CREATE")


        StrosekRazdelilnik.objects.create_strosekrazdelilnik(
            razdelilnik=razdelilnik,
            strosek=strosek,
        )



        return HttpResponseRedirect(reverse('moduli:razdelilnik:razdelilnik_detail', kwargs={'pk': razdelilnik.pk}))




class StrosekRazdelilnikUpdateView(LoginRequiredMixin, UpdateView):
    model = StrosekRazdelilnik
    form_class = StrosekRazdelilnikUpdateForm
    template_name = "razdelilnik/strosekrazdelilnik/update/update.html"

    def get_context_data(self, *args, **kwargs):
        context = super(StrosekRazdelilnikUpdateView, self).get_context_data(*args, **kwargs)

        modul_zavihek = Zavihek.objects.get(oznaka="RACUNRAZDELILNIK_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context