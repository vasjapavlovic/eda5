from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.views.generic import TemplateView, ListView, DetailView
from .models import Delilnik, Odcitek
from .viewmixins import DelilnikSearchMixin
from .forms import OdcitekCreateWidget
from eda5.core.models import ObdobjeLeto, ObdobjeMesec
from eda5.partnerji.models import Oseba


class StevciHomeView(TemplateView):
    template_name = "stevci/home.html"


class DelilnikListView(DelilnikSearchMixin, ListView):
    template_name = "stevci/delilnik/list.html"
    model = Delilnik


class DelilnikDetailView(DetailView):
    template_name = "stevci/delilnik/detail.html"
    model = Delilnik

    def get_context_data(self, *args, **kwargs):
        context = super(DelilnikDetailView, self).get_context_data(*args, **kwargs)
        context['odcitek_form'] = OdcitekCreateWidget
        return context

    def post(self, request, *args, **kwargs):
        odcitek_form = OdcitekCreateWidget(request.POST or None)

        delilnik = Delilnik.objects.get(id=self.get_object().id)

        if odcitek_form.is_valid():
            obdobje_leto = odcitek_form.cleaned_data['obdobje_leto']
            obdobje_mesec = odcitek_form.cleaned_data['obdobje_mesec']
            odcital = odcitek_form.cleaned_data['odcital']
            datum_odcitka = odcitek_form.cleaned_data['datum_odcitka']
            stanje_novo = odcitek_form.cleaned_data['stanje_novo']

            obdobje_leto = ObdobjeLeto.objects.get(oznaka=obdobje_leto)
            obdobje_mesec = ObdobjeMesec.objects.get(oznaka=obdobje_mesec)
            odcital = Oseba.objects.get(id=odcital)

            odcitki_delilnika = Odcitek.objects.filter(delilnik=delilnik)
            odcitek_delilnika_zadnji = odcitki_delilnika.latest('datum_odcitka')
            stanje_staro = odcitek_delilnika_zadnji.stanje_novo

            Odcitek.objects.create_odcitek(
                delilnik=delilnik,
                obdobje_leto=obdobje_leto,
                obdobje_mesec=obdobje_mesec,
                odcital=odcital,
                datum_odcitka=datum_odcitka,
                stanje_staro=stanje_staro,
                stanje_novo=stanje_novo,
                )

        # return HttpResponseRedirect('/moduli/stevci/')
        return HttpResponseRedirect(reverse('moduli:stevci:delilnik_list'))
