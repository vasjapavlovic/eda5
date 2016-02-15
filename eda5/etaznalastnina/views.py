# DJANGO #####################################
from django.shortcuts import render
from django.views.generic import ListView, DetailView

# RELATIVE IMPORTS
from .models import LastniskaEnotaInterna, LastniskaEnotaElaborat

# ABSOLUTE IMPORTS
# Moduli
from eda5.moduli.models import Zavihek


from eda5.stevcnostanje.models import Stevec, Delilnik

from eda5.etaznalastnina.models import LastniskaSkupina
from eda5.deli.models import ProjektnoMesto, DelStavbe


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

    def get_context_data(self, *args, **kwargs):
        context = super(LastniskaEnotaInternaDetailView, self).get_context_data(*args, **kwargs)

        # content
        modul_zavihek = Zavihek.objects.get(oznaka="INT_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        # stevci vezani na enoto
        # opravila = Opravilo.objects.filter(element=self.object.id)
        interna_enota = self.object
        enota_elaborat = interna_enota.elaborat

        # seznam delilnikov posamezne enote
        projektno_mesto_list = ProjektnoMesto.objects.filter(del_stavbe__lastniska_skupina__lastniska_enota=enota_elaborat)
        delilnik_enota_list = []
        for projektno_mesto in projektno_mesto_list:
            delilnik_list = Delilnik.objects.filter(stevec__projektno_mesto=projektno_mesto)
            for delilnik in delilnik_list:
                delilnik_enota_list.append(delilnik)
        context['delilnik_enota_list'] = delilnik_enota_list


        # skupni deli v solasti
        del_list = DelStavbe.objects.filter(lastniska_skupina__lastniska_enota=enota_elaborat)
        context['del_list'] = del_list

        return context
