from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView, UpdateView

from .forms import OpraviloModelForm, DelovniNalogVcakanjuModelForm, DelovniNalogVresevanjuModelForm
from .models import Opravilo, DelovniNalog, Delo

from eda5.zaznamki.forms import ZaznamekForm
from eda5.zaznamki.models import Zaznamek

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

        # zaznamek
        context['zaznamek_form'] = ZaznamekForm
        context['zaznamek_list'] = Zaznamek.objects.filter(delovninalog=self.object.id)

        return context


    def post(self, request, *args, **kwargs):
        zaznamek_form = ZaznamekForm(request.POST or None)

        # avtomatski podatki
        delovninalog = DelovniNalog.objects.get(id=self.get_object().id)

        if zaznamek_form.is_valid():
            tekst = zaznamek_form.cleaned_data['tekst']
            datum = zaznamek_form.cleaned_data['datum']
            ura = zaznamek_form.cleaned_data['ura']

            Zaznamek.objects.create_zaznamek(tekst=tekst,
                                             datum=datum,
                                             ura=ura,
                                             delovninalog=delovninalog,
                                             )

        return HttpResponseRedirect(reverse('moduli:delovninalogi:dn_detail', kwargs={'pk': delovninalog.pk}))


class DelovniNalogUpdateVcakanjuView(UpdateView):
    
    model = DelovniNalog
    form_class = DelovniNalogVcakanjuModelForm
    template_name = "delovninalogi/delovninalog/update_vcakanju.html"
    success_url = reverse_lazy('moduli:delovninalogi:dn_list')

class DelovniNalogUpdateVresevanjuView(UpdateView):
    model = DelovniNalog
    form_class = DelovniNalogVresevanjuModelForm
    template_name = "delovninalogi/delovninalog/update_vresevanju.html"