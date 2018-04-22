from django.views.generic import TemplateView, DetailView

from eda5.delovninalogi.models import DelovniNalog
from eda5.racunovodstvo.models import Strosek


class DP01_02(TemplateView):
    template_name = "reports/iso9001/iso9001_kazalnik_DP01-02.html"


    def get_context_data(self, *args, **kwargs):
        context = super(DP01_02, self).get_context_data(*args, **kwargs)


        # Seznam delovnih nalogov pri katerih se izvaja planirano opravilo
        delovninalog_planirani_list = DelovniNalog.objects.filter(opravilo__planirano_opravilo__isnull=False)
        # samo plan PLAN-OV
        delovninalog_planirani_list = delovninalog_planirani_list.filter(opravilo__planirano_opravilo__plan__oznaka="PLAN-OV-2018")
        # brez dnevnih opravil
        delovninalog_planirani_list = delovninalog_planirani_list.exclude(opravilo__planirano_opravilo__perioda_predpisana_enota="dan")
        # brez tedenskih opravil
        delovninalog_planirani_list = delovninalog_planirani_list.exclude(opravilo__planirano_opravilo__perioda_predpisana_enota="teden")


        # ZAKLJUČENI V LETU 2017
        #delovninalog_planirani_list = delovninalog_planirani_list.filter(datum_stop__gte=)

        # ZAPADLI




        # ORDER
        delovninalog_planirani_list = delovninalog_planirani_list.order_by('opravilo__planirano_opravilo__oznaka', '-id')
        context['delovninalog_planirani_list'] = delovninalog_planirani_list


        return context



class DP01_03(TemplateView):
    template_name = "reports/iso9001/iso9001_kazalnik_DP01-03.html"


    def get_context_data(self, *args, **kwargs):
        context = super(DP01_03, self).get_context_data(*args, **kwargs)


        # seznam stroškov
        strosek_seznam = Strosek.objects.filter()
        # kriterij - vrsta stroška skupina - O-TVZ-02
        strosek_seznam = strosek_seznam.filter(vrsta_stroska__skupina__oznaka="O-TVZ-02")
        # ObdobjeLeto
        strosek_seznam = strosek_seznam.filter(datum_storitve_od__year="2017")
        # order by vrsta_stroška (O-TVZ-02A, O-TVZ-02B)
        strosek_seznam = strosek_seznam.order_by('vrsta_stroska__oznaka', 'datum_storitve_od')
        # v templates pripraviš tabelo, ki je primerna za izdelavo pouizvedbe v excelu


        context['strosek_seznam'] = strosek_seznam

        return context
