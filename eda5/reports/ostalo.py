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


class ReportDelovniNalogODnevnik(TemplateView):
    template_name = "reports/delovninalog/dnevnik/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ReportDelovniNalogODnevnik, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="DELOVNI_NALOG_DNEVNIK")
        context['modul_zavihek'] = modul_zavihek

        delovninalogi = DelovniNalog.objects.filter(status=4)
        context['delovninalogi'] = delovninalogi

        return context





def create_pdf_view(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    buffer = BytesIO()

    # Create the PDF object, using the BytesIO object as its "file."
    p = canvas.Canvas(buffer, pagesize=A4)
    p.line(10,10, 20, 20)
    p.setFont("Times-Roman", 10)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.

    delovninalogi = DelovniNalog.objects.filter()

    
    p.drawString(0, 0, 'DELOVNI NALOG')
    x = 0
    y = 0
    for dn in delovninalogi:
        y= y + 15
        p.drawString(x, y, dn.oznaka)
        p.drawString(x+100, y, dn.opravilo.oznaka)
        p.drawString(x+200, y, dn.opravilo.naziv)


    # Close the PDF object cleanly.
    p.showPage()
    p.save()

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response


