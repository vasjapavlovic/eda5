# from django.shortcuts import render

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView

from .models import Zahtevek

from eda5.delovninalogi.forms import OpraviloForm
from eda5.delovninalogi.models import DelovniNalog, Opravilo


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

        # opravilo form
        context['opravilo_form'] = OpraviloForm
        # opravilo list
        context['opravilo_list'] = Opravilo.objects.filter(zahtevek=self.object.id)

        return context

    def post(self, request, *args, **kwargs):
        opravilo_form = OpraviloForm(request.POST or None)

        # avtomatski podatki
        zahtevek = Zahtevek.objects.get(id=self.get_object().id)

        if opravilo_form.is_valid():
            oznaka = opravilo_form.cleaned_data['oznaka']
            naziv = opravilo_form.cleaned_data['naziv']
            rok_izvedbe = opravilo_form.cleaned_data['rok_izvedbe']
            narocilo = opravilo_form.cleaned_data['narocilo']
            vrsta_stroska = opravilo_form.cleaned_data['vrsta_stroska']
            # element = opravilo_form.cleaned_data['element']

            Opravilo.objects.create_opravilo(oznaka=oznaka,
                                             naziv=naziv,
                                             rok_izvedbe=rok_izvedbe,
                                             narocilo=narocilo,
                                             vrsta_stroska=vrsta_stroska,
                                             zahtevek=zahtevek,
                                             # element=element,
                                             )

        return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk}))
