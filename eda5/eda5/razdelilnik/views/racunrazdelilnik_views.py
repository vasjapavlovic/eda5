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
from ..models import RacunRazdelilnik, Razdelilnik
from eda5.arhiv.models import ArhivMesto, Arhiviranje
from eda5.moduli.models import Zavihek
from eda5.zaznamki.models import Zaznamek

# Forms
from ..forms.razdelilnik_forms import RacunRazdelilnikCreateForm, RacunRazdelilnikUpdateForm, RazdelilnikSearchForm
from eda5.arhiv.forms import ArhiviranjeZahtevekForm
from eda5.zaznamki.forms import ZaznamekForm

# Views
from eda5.core.views import FilteredListView



class RacunRazdelilnikCreateView(UpdateView):
    model = Razdelilnik
    template_name = "razdelilnik/racunrazdelilnik/create/base.html"
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):
        context = super(RacunRazdelilnikCreateView, self).get_context_data(*args, **kwargs)

        # opravilo
        context['racun_razdelilnik_create_form'] = RacunRazdelilnikCreateForm

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="RACUNRAZDELILNIK_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        # object
        razdelilnik = Razdelilnik.objects.get(id=self.get_object().id)

        # forms
        racun_razdelilnik_create_form = RacunRazdelilnikCreateForm(request.POST or None)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="RACUNRAZDELILNIK_CREATE")

        # izdelamo opravilo (!!!elemente opravilu dodamo kasneje)
        if racun_razdelilnik_create_form.is_valid():
            razdelilnik = racun_razdelilnik_create_form.cleaned_data['razdelilnik']
            racun = racun_razdelilnik_create_form.cleaned_data['racun']

            RacunRazdelilnik.objects.create_racunrazdelilnik(
                razdelilnik=razdelilnik,
                racun=racun,
            )

        else:
            return render(request, self.template_name, {
                'racun_razdelilnik_create_form': racun_razdelilnik_create_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        return HttpResponseRedirect(reverse('moduli:razdelilnik:razdelilnik_detail', kwargs={'pk': razdelilnik.pk}))


class RacunRazdelilnikUpdateView(LoginRequiredMixin, UpdateView):
    model = RacunRazdelilnik
    form_class = RacunRazdelilnikUpdateForm
    template_name = "razdelilnik/racunrazdelilnik/update/update.html"

    def get_context_data(self, *args, **kwargs):
        context = super(RacunRazdelilnikUpdateView, self).get_context_data(*args, **kwargs)

        modul_zavihek = Zavihek.objects.get(oznaka="RACUNRAZDELILNIK_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context