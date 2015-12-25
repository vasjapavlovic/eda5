from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from django.views.generic import TemplateView, FormView, ListView, DetailView

from .forms import NarociloCreateIzbiraForm, NarociloSplosnoCreateForm, NarociloTelefonCreateForm
from .models import NarociloTelefon, NarociloPogodba, Narocilo

from eda5.moduli.models import Zavihek


class NarocilaHomeView(TemplateView):
    template_name = "narocila/home.html"


class NarociloListView(ListView):

    model = Narocilo
    template_name = "narocila/narocilo/list/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NarociloListView, self).get_context_data(*args, **kwargs)

        modul_zavihek = Zavihek.objects.get(oznaka="NAROCILO_LIST")
        context['modul_zavihek'] = modul_zavihek

        return context



class NarociloCreateIzbiraView(TemplateView):
    model = Narocilo
    template_name = "narocila/narocilo/create_izbira.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NarociloCreateIzbiraView, self).get_context_data(*args, **kwargs)

        # zahtevek
        context['narocilo_izbira_create_form'] = NarociloCreateIzbiraForm

        modul_zavihek = Zavihek.objects.get(oznaka="NAROCILO_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        narocilo_izbira_create_form = NarociloCreateIzbiraForm(request.POST or None)

        if narocilo_izbira_create_form.is_valid():

            vrsta_narocila = narocilo_izbira_create_form.cleaned_data['vrsta_narocila']

            if vrsta_narocila == '1':
                return HttpResponseRedirect(reverse('moduli:narocila:narocilo_create_telefon'))


class NarociloTelefonCreateView(TemplateView):
    template_name = "narocila/narocilo/create_telefon.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NarociloTelefonCreateView, self).get_context_data(*args, **kwargs)
        context['narocilo_splosno_form'] = NarociloSplosnoCreateForm
        context['narocilo_telefon_form'] = NarociloTelefonCreateForm

        modul_zavihek = Zavihek.objects.get(oznaka="NAROCILO_CREATE_TEL")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):
        narocilo_splosno_form = NarociloSplosnoCreateForm(request.POST or None)
        narocilo_telefon_form = NarociloTelefonCreateForm(request.POST or None)
        modul_zavihek = Zavihek.objects.get(oznaka="NAROCILO_CREATE_TEL")

        if narocilo_telefon_form.is_valid():
            oseba = narocilo_telefon_form.cleaned_data['oseba']
            telefonska_stevilka = narocilo_telefon_form.cleaned_data['telefonska_stevilka']
            datum_klica = narocilo_telefon_form.cleaned_data['datum_klica']
            cas_klica = narocilo_telefon_form.cleaned_data['cas_klica']
            telefonsko_sporocilo = narocilo_telefon_form.cleaned_data['telefonsko_sporocilo']

            narocilo_telefon_data = NarociloTelefon.objects.create_narocilo_telefon(
                oseba=oseba,
                telefonska_stevilka=telefonska_stevilka,
                datum_klica=datum_klica,
                cas_klica=cas_klica,
                telefonsko_sporocilo=telefonsko_sporocilo,
            )
            narocilo_telefon = NarociloTelefon.objects.get(id=narocilo_telefon_data.pk)

        else:
            return render(request, self.template_name, {
                'narocilo_splosno_form': narocilo_splosno_form,
                'narocilo_telefon_form': narocilo_telefon_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        if narocilo_splosno_form.is_valid():
            narocnik = narocilo_splosno_form.cleaned_data['narocnik']
            izvajalec = narocilo_splosno_form.cleaned_data['izvajalec']
            oznaka = narocilo_splosno_form.cleaned_data['oznaka']
            predmet = narocilo_splosno_form.cleaned_data['predmet']
            datum_narocila = narocilo_splosno_form.cleaned_data['datum_narocila']
            datum_veljavnosti = narocilo_splosno_form.cleaned_data['datum_veljavnosti']
            vrednost = narocilo_splosno_form.cleaned_data['vrednost']

            Narocilo.objects.create_narocilo(
                narocilo_telefon=narocilo_telefon,
                narocnik=narocnik,
                izvajalec=izvajalec,
                oznaka=oznaka,
                predmet=predmet,
                datum_narocila=datum_narocila,
                datum_veljavnosti=datum_veljavnosti,
                vrednost=vrednost,
            )

        else:
            return render(request, self.template_name, {
                'narocilo_splosno_form': narocilo_splosno_form,
                'narocilo_telefon_form': narocilo_telefon_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        return HttpResponseRedirect(reverse('moduli:narocila:home'))


class NarociloPogodbaCreateView(TemplateView):
    template_name = "narocila/narocilo/create_pogodba.html"


class NarociloDetailView(DetailView):
    model = Narocilo
    template_name = 'narocila/narocilo/detail/base.html'

    def get_context_data(self, *args, **kwargs):
        context = super(NarociloDetailView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="NAROCILO_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context

