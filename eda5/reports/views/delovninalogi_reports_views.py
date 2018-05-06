# Python


# Django
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.db.models import Q, F, Sum
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.db.models import Value
from django.db.models.functions import Concat

# Mixins
from braces.views import LoginRequiredMixin

# Models
from eda5.delovninalogi.models import DelovniNalog, Delo
from eda5.deli.models import DelStavbe, ProjektnoMesto
from eda5.dogodki.models import Dogodek
from eda5.moduli.models import Zavihek
from eda5.partnerji.models import Oseba
from eda5.racunovodstvo.models import Strosek, PodKonto, SkupinaVrsteStroska, VrstaStroska


# Forms
from ..forms.forms import \
    FormatForm,\
    LetnoPorociloUpravnikaStroskiIzpisIzbiraForm,\
    PlanIzbiraForm,\
    LetoIzbiraForm,\
    IzvedenaDelaIzpisIzbiraForm,\
    UporabimFilterForm,\
    ObracunIzrednaDelaForm,\
    DogodekFilterForm,\
    DogodkiIzpisIzbiraForm,\
    DelavecIzbiraForm

from eda5.racunovodstvo.forms.vrsta_stroska_forms import VrstaStroskaIzbiraForm
from eda5.narocila.forms import NarociloSelectForm

# Views
from eda5.core.views import FilteredListView

# Templated docs
from templated_docs import fill_template
from templated_docs.http import FileResponse



class EvidencaDelovnegaCasa(TemplateView):

    template_name = "reports/delovninalog/evidenca_delovnega_casa.html"

    def get_context_data(self, *args, **kwargs):
        context = super(EvidencaDelovnegaCasa, self).get_context_data(*args, **kwargs)

        modul_zavihek = Zavihek.objects.get(oznaka="REPORT_DELOVNINALOGI_EVIDENCADELOVNEGACASA")
        context['modul_zavihek'] = modul_zavihek

        return context



    def get(self, request, *args, **kwargs):

        uporabim_filter_form = UporabimFilterForm(request.GET or None)
        delavec_izbira_form = DelavecIzbiraForm(request.GET or None)
        vrsta_stroska_izbira_form = VrstaStroskaIzbiraForm(request.GET or None, davcna_klasifikacija=None)
        leto_izbira_form = LetoIzbiraForm(request.GET or None)
        narocilo_izbira_form = NarociloSelectForm(request.GET or None)

        delo_list = Delo.objects.filter().order_by('datum')


        if uporabim_filter_form.is_valid():

            if delavec_izbira_form.is_valid():
                delavec = delavec_izbira_form.cleaned_data['delavec']
                if delavec:
                    delavec = Oseba.objects.get(id=delavec.pk)
                    delo_list = delo_list.filter(delavec=delavec)

            if leto_izbira_form.is_valid():
                obdobje_leto = leto_izbira_form.cleaned_data['obdobje_leto']
                if obdobje_leto:
                    delo_list = delo_list.filter(datum__year=obdobje_leto.oznaka)

            if vrsta_stroska_izbira_form.is_valid():
                vrsta_stroska = vrsta_stroska_izbira_form.cleaned_data['vrsta_stroska']
                if vrsta_stroska:
                    delo_list = delo_list.filter(delovninalog__opravilo__vrsta_stroska=vrsta_stroska)

            if narocilo_izbira_form.is_valid():
                narocilo = narocilo_izbira_form.cleaned_data['narocilo']
                if narocilo:
                    delo_list = delo_list.filter(delovninalog__opravilo__narocilo=narocilo)


            delo_cas_sum = delo_list.aggregate(skupaj=Sum('delo_cas_rac'))

            context = self.get_context_data(
                delo_list=delo_list,
                delo_cas_sum=delo_cas_sum,
                delavec_izbira_form=delavec_izbira_form,
                uporabim_filter_form=uporabim_filter_form,
                vrsta_stroska_izbira_form=vrsta_stroska_izbira_form,
                leto_izbira_form=leto_izbira_form,
                narocilo_izbira_form=narocilo_izbira_form,
            )

        else:
            context = self.get_context_data(
                uporabim_filter_form=uporabim_filter_form,
                delavec_izbira_form=delavec_izbira_form,
                vrsta_stroska_izbira_form=vrsta_stroska_izbira_form,
                leto_izbira_form=leto_izbira_form,
                narocilo_izbira_form=narocilo_izbira_form,
            )

        return self.render_to_response(context)
