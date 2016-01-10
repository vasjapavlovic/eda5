# DJANGO #####################################
from django.shortcuts import render
from django.views.generic import ListView, DetailView

# RELATIVE IMPORTS
from .models import LastniskaEnotaInterna

# ABSOLUTE IMPORTS
# Moduli
from eda5.moduli.models import Zavihek


class LastniskaEnotaInternaListTehView(ListView):

    model = LastniskaEnotaInterna
    template_name = "etaznalastnina/lastniska_enota_interna/list/tehnicna.html"

    def get_context_data(self, *args, **kwargs):
        context = super(LastniskaEnotaInternaListTehView, self).get_context_data(*args, **kwargs)

        # content
        modul_zavihek = Zavihek.objects.get(oznaka="INT_LIST_TEH")
        context['modul_zavihek'] = modul_zavihek

        return context

    def get_queryset(self):
        queryset = super(LastniskaEnotaInternaListTehView, self).get_queryset()

        return queryset.select_related('elaborat', 'internadodatno')


class LastniskaEnotaInternaListLastView(ListView):

    model = LastniskaEnotaInterna
    template_name = "etaznalastnina/lastniska_enota_interna/list/lastniska.html"

    def get_context_data(self, *args, **kwargs):
        context = super(LastniskaEnotaInternaListLastView, self).get_context_data(*args, **kwargs)

        # content
        modul_zavihek = Zavihek.objects.get(oznaka="INT_LIST_LAST")
        context['modul_zavihek'] = modul_zavihek

        return context

    def get_queryset(self):
        queryset = super(LastniskaEnotaInternaListLastView, self).get_queryset()

        return queryset.select_related('elaborat', 'internadodatno')


class LastniskaEnotaInternaDetailView(DetailView):

    model = LastniskaEnotaInterna
    template_name = "etaznalastnina/lastniska_enota_interna/detail/base.html"
