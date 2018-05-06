from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.db.models import Q

from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A3, A4



from ..forms import ReportForm



from eda5.racunovodstvo.models import Strosek, VrstaStroska, SkupinaVrsteStroska, PodKonto, Konto
from eda5.moduli.models import Zavihek

from eda5.delovninalogi.models import Delo, DelovniNalog


class ReportStrosek(TemplateView):
    template_name = "reports/strosek/report_1/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ReportStrosek, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="REPORT_STROSEK")
        context['modul_zavihek'] = modul_zavihek

        context['report_form'] = ReportForm
        # strosek po vrsta_stroska
        strosek_list = Strosek.objects.filter(racun__davcna_klasifikacija=1)
        context['strosek_list'] = strosek_list

        q = self.request.GET.getlist("q")

        if q:

            vrsta_stroska_list = VrstaStroska.objects.filter(skupina__skupina__skupina__oznaka="O", skupina__in=q)
        else:
            vrsta_stroska_list = VrstaStroska.objects.filter(skupina__skupina__skupina__oznaka="O")
        context['vrsta_stroska_list'] = vrsta_stroska_list

        skupina_vrste_stroska_list = SkupinaVrsteStroska.objects.filter(skupina__skupina__oznaka="O")
        context['skupina_vrste_stroska_list'] = skupina_vrste_stroska_list

        podkonto = PodKonto.objects.filter(skupina__oznaka="O")
        context['podkonto_list'] = podkonto

        konto = Konto.objects.exclude(oznaka="E")
        context['konto_list'] = konto

        return context


class ReportDelavciVDelu(TemplateView):
    template_name = "reports/delovninalog/delavcivdelu/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ReportDelavciVDelu, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="DELAVCI_V_DELU")
        context['modul_zavihek'] = modul_zavihek

        delavdelu = Delo.objects.filter(time_stop__isnull=True)
        context['delavdelu'] = delavdelu

        return context
