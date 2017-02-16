from django.shortcuts import render

from django.views.generic import ListView, DetailView

from .models import Obvestilo
from eda5.moduli.models import Zavihek


class ObvestiloListView(ListView):
    model = Obvestilo
    template_name = "obvestila/obvestilo/list/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ObvestiloListView, self).get_context_data(*args, **kwargs)
        modul_zavihek = Zavihek.objects.get(oznaka="OBVESTILO_LIST")
        context['modul_zavihek'] = modul_zavihek
        return context

    def get_queryset(self):
        queryset = super(ObvestiloListView, self).get_queryset()
        queryset = queryset.filter(is_active=True)
        return queryset


class ObvestiloDetailView(DetailView):
    model = Obvestilo
    template_name = "obvestila/obvestilo/detail/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ObvestiloDetailView, self).get_context_data(*args, **kwargs)
        modul_zavihek = Zavihek.objects.get(oznaka="OBVESTILO_DETAIL")
        context['modul_zavihek'] = modul_zavihek
        return context

    # dodaj create_komentar
    # dodati dodajanje dokumentov
    # dodati je zaznamke

    # dodati dodajanje komentarjev
    # dodati je zaznamke




