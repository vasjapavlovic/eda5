from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.views.generic import TemplateView, ListView, CreateView, DetailView

from .models import Racun
from .forms import RacunAddWidget, RacunCreateForm
from eda5.posta.models import Dokument
from eda5.users.models import User


class RacunovodstvoHomeView(TemplateView):
    template_name = "racunovodstvo/home.html"


class RacunovodstvoRacunDetail(DetailView):
    model = Racun



class RacunovodstvoRacuniLikvidacija(ListView):
    model = Dokument
    template_name = "racunovodstvo/racun_list_likvidacija.html"

    def get_queryset(self):
        queryset = super(RacunovodstvoRacuniLikvidacija, self).get_queryset()
        queryset = queryset.filter(vrsta_dokumenta=1)
        return queryset


class RacunovodstvoRacuniList(ListView):
    model = Racun
    template_name = "racunovodstvo/racun_list.html"


class RacunovodstvoLikvidacijaDetail(DetailView):
    model = Dokument
    template_name = "racunovodstvo/racun_likvidacija_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(RacunovodstvoLikvidacijaDetail, self).get_context_data(*args, **kwargs)
        context['racun_form'] = RacunCreateForm
        return context

    def post(self, request, *args, **kwargs):
        racun_form = RacunCreateForm(request.POST or None)

        dokument = Dokument.objects.get(id=self.get_object().id)

        if racun_form.is_valid():
            davcna_klasifikacija = racun_form.cleaned_data['davcna_klasifikacija']
            datum_storitve_od = racun_form.cleaned_data['datum_storitve_od']
            datum_storitve_do = racun_form.cleaned_data['datum_storitve_do']
            obdobje_obracuna_leto = racun_form.cleaned_data['obdobje_obracuna_leto']
            obdobje_obracuna_mesec = racun_form.cleaned_data['obdobje_obracuna_mesec']
            narocilo = racun_form.cleaned_data['narocilo']
            osnova_0 = racun_form.cleaned_data['osnova_0']
            osnova_1 = racun_form.cleaned_data['osnova_1']
            osnova_2 = racun_form.cleaned_data['osnova_2']

            Racun.objects.create_racun(
                dokument=dokument,
                davcna_klasifikacija=davcna_klasifikacija,
                datum_storitve_od=datum_storitve_od,
                datum_storitve_do=datum_storitve_do,
                obdobje_obracuna_leto=obdobje_obracuna_leto,
                obdobje_obracuna_mesec=obdobje_obracuna_mesec,
                narocilo=narocilo,
                osnova_0=osnova_0,
                osnova_1=osnova_1,
                osnova_2=osnova_2,
                )

        return HttpResponseRedirect('/moduli/racunovodstvo/')
