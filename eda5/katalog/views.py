from django.shortcuts import render

from django.views.generic import ListView

from .models import Proizvajalec, ModelArtikla, TipArtikla

from eda5.moduli.models import Zavihek


class ProizvajalecListView(ListView):

    model = Proizvajalec
    template_name = "katalog/proizvajalec/list/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProizvajalecListView, self).get_context_data(*args, **kwargs)

        modul_zavihek = Zavihek.objects.get(oznaka="PROIZVAJALEC_LIST")
        context['modul_zavihek'] = modul_zavihek

        return context


class TipArtiklaListView(ListView):

    model = TipArtikla
    template_name = "katalog/tip_artikla/list/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(TipArtiklaListView, self).get_context_data(*args, **kwargs)

        modul_zavihek = Zavihek.objects.get(oznaka="TIP_ARTIKLA_LIST")
        context['modul_zavihek'] = modul_zavihek

        return context


class ModelArtiklaListView(ListView):

    model = ModelArtikla
    template_name = "katalog/model_artikla/list/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ModelArtiklaListView, self).get_context_data(*args, **kwargs)

        modul_zavihek = Zavihek.objects.get(oznaka="MODEL_ARTIKLA_LIST")
        context['modul_zavihek'] = modul_zavihek

        return context
