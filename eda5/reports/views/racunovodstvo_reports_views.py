# Python

# Django
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.db.models import \
    Q,\
    F,\
    Sum
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.generic import \
    TemplateView,\
    ListView,\
    DetailView,\
    UpdateView
from django.db.models import Value
from django.db.models.functions import Concat

# Templated docs
from templated_docs import fill_template
from templated_docs.http import FileResponse

# Braces
from braces.views import LoginRequiredMixin

# Models
from eda5.delovninalogi.models import DelovniNalog
from eda5.deli.models import DelStavbe, ProjektnoMesto
from eda5.dogodki.models import Dogodek
from eda5.moduli.models import Zavihek
from eda5.racunovodstvo.models import \
    Strosek,\
    PodKonto,\
    SkupinaVrsteStroska,\
    VrstaStroska

# Views
from eda5.core.views import FilteredListView

# Forms
from ..forms import \
    FormatForm,\
    LetoIzbiraForm,\
    IzvedenaDelaIzpisIzbiraForm,\
    UporabimFilterForm,\
    NarociloSelectForm
from eda5.racunovodstvo.forms.vrsta_stroska_forms import VrstaStroskaIzbiraForm


class ReportStroskiVrstaStroskaNarocilo(TemplateView):
    template_name = "reports/report_stroski/report_stroski_vrstastroska_narocilo.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ReportStroskiVrstaStroskaNarocilo, self).get_context_data(*args, **kwargs)

        modul_zavihek = Zavihek.objects.get(oznaka="REPORT_STROSKI_VRSTASTROSKA_NAROCILO")
        context['modul_zavihek'] = modul_zavihek

        return context

    def get(self, request, *args, **kwargs):

        vrsta_stroska_izbira_form = VrstaStroskaIzbiraForm(request.GET or None, davcna_klasifikacija=None)
        leto_izbira_form = LetoIzbiraForm(request.GET or None)
        narocilo_izbira_form = NarociloSelectForm(request.GET or None)
        uporabim_filter_form = UporabimFilterForm(request.GET or None)


        strosek_list = Strosek.objects.filter().order_by('datum_storitve_od')

        if uporabim_filter_form.is_valid():

            if leto_izbira_form.is_valid():
                obdobje_leto = leto_izbira_form.cleaned_data['obdobje_leto']
                if obdobje_leto:
                    strosek_list = strosek_list.filter(datum_storitve_od__year=obdobje_leto.oznaka)

            if vrsta_stroska_izbira_form.is_valid():
                vrsta_stroska = vrsta_stroska_izbira_form.cleaned_data['vrsta_stroska']
                if vrsta_stroska:
                    strosek_list = strosek_list.filter(vrsta_stroska=vrsta_stroska)

            if narocilo_izbira_form.is_valid():
                narocilo = narocilo_izbira_form.cleaned_data['narocilo']
                if narocilo:
                    strosek_list = strosek_list.filter(narocilo=narocilo)


            strosek_sum_brezddv = strosek_list.aggregate(skupaj=Sum('osnova'))

            context = self.get_context_data(
                strosek_list=strosek_list,
                strosek_sum_brezddv=strosek_sum_brezddv,
                uporabim_filter_form=uporabim_filter_form,
                vrsta_stroska_izbira_form=vrsta_stroska_izbira_form,
                leto_izbira_form=leto_izbira_form,
                narocilo_izbira_form=narocilo_izbira_form,
                )

        else:
            context = self.get_context_data(
                uporabim_filter_form=uporabim_filter_form,
                vrsta_stroska_izbira_form=vrsta_stroska_izbira_form,
                leto_izbira_form=leto_izbira_form,
                narocilo_izbira_form=narocilo_izbira_form,
            )

        return self.render_to_response(context)
