# from django.shortcuts import render

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView

from .models import Zahtevek

from eda5.delovninalogi.forms import OpraviloForm
from eda5.delovninalogi.models import Opravilo

from eda5.zaznamki.forms import ZaznamekForm
from eda5.zaznamki.models import Zaznamek


class ZahtevekHomeView(TemplateView):
    template_name = "zahtevki/home.html"


class ZahtevekListView(ListView):
    model = Zahtevek
    template_name = "zahtevki/zahtevek/list.html"


class ZahtevekDetailView(DetailView):
    model = Zahtevek
    template_name = "zahtevki/zahtevek/detail/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ZahtevekDetailView, self).get_context_data(*args, **kwargs)

        # opravilo
        context['opravilo_form'] = OpraviloForm
        context['opravilo_list'] = Opravilo.objects.filter(zahtevek=self.object.id)

        # zaznamek
        context['zaznamek_form'] = ZaznamekForm
        context['zaznamek_list'] = Zaznamek.objects.filter(zahtevek=self.object.id)

        return context

    def post(self, request, *args, **kwargs):
        opravilo_form = OpraviloForm(request.POST or None)
        zaznamek_form = ZaznamekForm(request.POST or None)

        # avtomatski podatki
        zahtevek = Zahtevek.objects.get(id=self.get_object().id)

        if opravilo_form.is_valid():
            oznaka = opravilo_form.cleaned_data['oznaka']
            naziv = opravilo_form.cleaned_data['naziv']
            rok_izvedbe = opravilo_form.cleaned_data['rok_izvedbe']
            narocilo = opravilo_form.cleaned_data['narocilo']
            nadzornik = opravilo_form.cleaned_data['nadzornik']
            # element = opravilo_form.cleaned_data['element']

            Opravilo.objects.create_opravilo(oznaka=oznaka,
                                             naziv=naziv,
                                             rok_izvedbe=rok_izvedbe,
                                             narocilo=narocilo,
                                             zahtevek=zahtevek,
                                             nadzornik=nadzornik
                                             # element=element,
                                             )

        if zaznamek_form.is_valid():
            tekst = zaznamek_form.cleaned_data['tekst']
            datum = zaznamek_form.cleaned_data['datum']
            ura = zaznamek_form.cleaned_data['ura']

            Zaznamek.objects.create_zaznamek(tekst=tekst,
                                             datum=datum,
                                             ura=ura,
                                             zahtevek=zahtevek,
                                             )

        return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk}))
