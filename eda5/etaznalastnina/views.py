from django.shortcuts import render

from django.views.generic import ListView

from .models import LastniskaEnotaInterna

from eda5.moduli.models import Zavihek


class LastniskaEnotaInternaListTehView(ListView):

    model = LastniskaEnotaInterna
    template_name = "etaznalastnina/lastniska_enota_interna/list_teh.html"

    def get_context_data(self, *args, **kwargs):
        context = super(LastniskaEnotaInternaListTehView, self).get_context_data(*args, **kwargs)

        # content
        modul_zavihek = Zavihek.objects.get(oznaka="INT_LIST_TEH")
        context['modul_zavihek'] = modul_zavihek

        return context


class LastniskaEnotaInternaListLastView(ListView):

    model = LastniskaEnotaInterna
    template_name = "etaznalastnina/lastniska_enota_interna/list_last.html"

    def get_context_data(self, *args, **kwargs):
        context = super(LastniskaEnotaInternaListLastView, self).get_context_data(*args, **kwargs)

        # content
        modul_zavihek = Zavihek.objects.get(oznaka="INT_LIST_LAST")
        context['modul_zavihek'] = modul_zavihek

        return context
