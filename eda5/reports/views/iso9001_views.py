from django.views.generic import TemplateView, DetailView

from eda5.delovninalogi.models import DelovniNalog


class Porocanje(TemplateView):
    template_name = "reports/iso9001/planiranaopravila_nepravocasno_izvedena.html"


    def get_context_data(self, *args, **kwargs):
        context = super(Porocanje, self).get_context_data(*args, **kwargs)


        # Seznam delovnih nalogov pri katerih se izvaja planirano opravilo
        delovninalog_planirani_list = DelovniNalog.objects.filter(opravilo__planirano_opravilo__isnull=False)
        # samo plan PLAN-OV
        delovninalog_planirani_list = delovninalog_planirani_list.filter(opravilo__planirano_opravilo__plan__oznaka="PLAN-OV-2018")
        # brez dnevnih opravil
        delovninalog_planirani_list = delovninalog_planirani_list.exclude(opravilo__planirano_opravilo__perioda_predpisana_enota="dan")
        # brez tedenskih opravil
        delovninalog_planirani_list = delovninalog_planirani_list.exclude(opravilo__planirano_opravilo__perioda_predpisana_enota="teden")


        # ZAKLJUČENI V LETU 2017
        # ZAPADLI



        
        # ORDER
        delovninalog_planirani_list = delovninalog_planirani_list.order_by('opravilo__planirano_opravilo__oznaka', '-id')
        context['delovninalog_planirani_list'] = delovninalog_planirani_list


        return context
