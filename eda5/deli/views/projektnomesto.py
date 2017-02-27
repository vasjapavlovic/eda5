from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.http import JsonResponse
from django.shortcuts import render

from django.views.generic import \
    TemplateView, \
    ListView,\
    DetailView,\
    UpdateView,\
    CreateView

from django.db.models import Max


# Deli FORMS
from ..forms import \
    projektnomesto_forms

# Deli MODELS
from ..models import\
    Skupina, \
    Podskupina, \
    DelStavbe, \
    ProjektnoMesto, \
    Element

# Delovni nalogi MODELS
from eda5.delovninalogi.models import \
    Opravilo, \
    DelovniNalog

# Katalog MODELS
from eda5.katalog.models import \
    ObratovalniParameter

# Moduli MODELS
from eda5.moduli.models import \
    Zavihek

# Računovodstvo MODELS
from eda5.racunovodstvo.models import \
    Strosek



class ProjektnoMestoCreateView(CreateView):

    model = ProjektnoMesto
    form_class = projektnomesto_forms.ProjektnoMestoCreateForm
    template_name = "deli/projektno_mesto/create.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProjektnoMestoCreateView, self).get_context_data(*args, **kwargs)
        modul_zavihek = Zavihek.objects.get(oznaka="PROJEKTNO_MESTO_CREATE")
        context['modul_zavihek'] = modul_zavihek
        return context


class ProjektnoMestoDetailView(DetailView):
    template_name = "deli/projektnomesto/detail/base.html"
    model = ProjektnoMesto

    def get_context_data(self, *args, **kwargs):
        context = super(ProjektnoMestoDetailView, self).get_context_data(*args, **kwargs)

        # Servisna knjiga
        # seznam delovnih nalogov (za servisno knjigo)
        delovninalog_list = []
        # seznam opravil kjer je vsebovan element
        opravila = Opravilo.objects.filter(element=self.object.id)
        # iteriramo skozi seznam opravil, da pridobimo posamezne sezname delovnih nalogov
        for opravilo in opravila:
            delovninalog_list_x = DelovniNalog.objects.filter(opravilo=opravilo)
        # iteriramo skozi seznam delovnih nalogov in dodamo v seznam
            for dn in delovninalog_list_x:
                delovninalog_list.append(dn)
            # list(delovninalog_list)

        context['delovninalog_list'] = delovninalog_list

        # # seznam nastavitev (za obratovanje)
        # nastavitve = self.object.element_set.filter(is_active=True)[0]
        # nastavitve = nastavitve.nastavitev_set.all()
        context['nastavitev_list'] = []

        # # nastavljene vrednosti (parametri obratovanja)
        # nastavitev_max = self.object.nastavitev_set.values(
        #     "obratovalni_parameter").annotate(datum=Max("datum_nastavitve"))

        # # sestavimo ustrezen seznam za izpis
        # nastavitev_max_izpis = []
        # for nastavitev in nastavitev_max:
        #     nastavitev_max_izpis.append(self.object.nastavitev_set.filter(
        #         obratovalni_parameter=nastavitev['obratovalni_parameter'],
        #         datum_nastavitve=nastavitev['datum'])[0]
        #     )
        context['nastavitev_max'] = []

        


        # Zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="ELEMENT_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context




