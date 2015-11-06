from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView
from .models import DelStavbe, Skupina, Element

from eda5.delovninalogi.models import Opravilo, DelovniNalog


class DelHomeView(TemplateView):
    template_name = "deli/home.html"


class DelListView(ListView):
    template_name = "deli/list.html"
    model = Skupina


class DelDetailView(DetailView):
    template_name = "deli/del_detail.html"
    model = DelStavbe


class ElementDetailView(DetailView):
    template_name = "deli/element_detail.html"
    model = Element

    def get_context_data(self, *args, **kwargs):
        context = super(ElementDetailView, self).get_context_data(*args, **kwargs)

        opravila = Opravilo.objects.filter(element=self.object.id)
        dn = DelovniNalog.objects.filter(opravilo=opravila).exclude(strosek__isnull=True)

        dn_strosek_skp = 0

        for dnx in dn:
            dn_strosek = dnx.strosek.strosek_z_ddv
            dn_strosek_skp = dn_strosek_skp + dn_strosek

        dn_strosek_skp = str(round(dn_strosek_skp)) + ',00 EUR'

        context['celotnistrosek'] = dn_strosek_skp
        return context
