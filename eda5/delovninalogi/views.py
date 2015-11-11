from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView, UpdateView

from .forms import OpraviloModelForm
from .models import Opravilo, DelovniNalog, Delo


class AppHomeView(TemplateView):
    template_name = "delovninalogi/home.html"


class OpraviloListView(ListView):
    model = Opravilo
    template_name = "delovninalogi/opravilo/list.html"


class OpraviloDetailView(DetailView):
    model = Opravilo
    template_name = "delovninalogi/opravilo/detail.html"


class OpraviloUpdateView(UpdateView):
    model = Opravilo
    form_class = OpraviloModelForm
    template_name = "delovninalogi/opravilo/update.html"


class DelovniNalogList(ListView):
    model = DelovniNalog
    template_name = "delovninalogi/delovninalog/list/extended.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DelovniNalogList, self).get_context_data(*args, **kwargs)

        # content
        context['dn_vcakanju_list'] = self.model.objects.dn_vcakanju()
        context['dn_vplanu_list'] = self.model.objects.dn_vplanu()
        context['dn_vresevanju_list'] = self.model.objects.dn_vresevanju()
        context['dn_zakljuceni_list'] = self.model.objects.dn_zakljuceni()

        return context


class DelovniNalogDetailView(DetailView):
    model = DelovniNalog
    template_name = "delovninalogi/delovninalog/detail/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DelovniNalogDetailView, self).get_context_data(*args, **kwargs)

        # content
        context['odprta_dela'] = Delo.objects.odprta_dela()
        context['koncana_dela'] = Delo.objects.koncana_dela()

        return context