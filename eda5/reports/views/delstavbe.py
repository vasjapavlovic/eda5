# Django
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.db.models import Max
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView

# Mixins
from braces.views import LoginRequiredMixin

# Models
from eda5.deli.models import Skupina, Podskupina, DelStavbe, ProjektnoMesto, Element
from eda5.delovninalogi.models import Opravilo, DelovniNalog
from eda5.katalog.models import ObratovalniParameter
from eda5.moduli.models import Zavihek
from eda5.racunovodstvo.models import Strosek

# Forms



class ReportDelStavbeView(DetailView):
    template_name = "reports/delstavbe/detail/base.html"
    model = DelStavbe

    def get_context_data(self, *args, **kwargs):
        context = super(ReportDelStavbeView, self).get_context_data(*args, **kwargs)
        modul_zavihek = Zavihek.objects.get(oznaka="DEL_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        # Servisna knjiga
        delstavbe_instance = DelStavbe.objects.get(id=self.object.id)
        
        # seznam delovnih nalogov (za servisno knjigo)
        servisna_knjiga = []
        # seznam opravil kjer je vsebovan element
        opravila = Opravilo.objects.filter(element__del_stavbe=self.object.id)
        # iteriramo skozi seznam opravil, da pridobimo posamezne sezname delovnih nalogov
        for opravilo in opravila:
            delovninalog_list_x = DelovniNalog.objects.filter(opravilo=opravilo)
        # iteriramo skozi seznam delovnih nalogov in dodamo v seznam
            for dn in delovninalog_list_x:
                servisna_knjiga.append(dn)
            # list(delovninalog_list)
        context['servisna_knjiga'] = servisna_knjiga


        return context

