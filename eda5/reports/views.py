from django.shortcuts import render
from django.views.generic import TemplateView


from eda5.racunovodstvo.models import Strosek, VrstaStroska
from eda5.moduli.models import Zavihek


class ReportStrosek(TemplateView):
    template_name = "reports/strosek/report_1/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ReportStrosek, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="REPORT_STROSEK")
        context['modul_zavihek'] = modul_zavihek

        # strosek po vrsta_stroska
        strosek_list = Strosek.objects.filter(racun__davcna_klasifikacija=1)
        context['strosek_list'] = strosek_list

        vrsta_stroska_list = VrstaStroska.objects.filter(skupina__skupina__skupina__oznaka="O")
        context['vrsta_stroska_list'] = vrsta_stroska_list

        return context
