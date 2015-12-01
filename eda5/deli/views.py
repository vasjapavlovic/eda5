from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView, UpdateView

from .forms import DelCreateForm
from .models import DelStavbe, Skupina, Element, Podskupina

from eda5.delovninalogi.models import Opravilo, DelovniNalog


class DelHomeView(TemplateView):
    template_name = "deli/home.html"


class DelListView(ListView):
    template_name = "deli/delstavbe/list/extended.html"
    model = Skupina

    def get_context_data(self, *args, **kwargs):
        context = super(DelListView, self).get_context_data(*args, **kwargs)
        context['del_form'] = DelCreateForm
        return context

    def post(self, request, *args, **kwargs):
        del_form = DelCreateForm(request.POST or None)

        # avtomatska oznaka Dela stavbe

        if del_form.is_valid():

            # vnešeni podatki
            podskupina = del_form.cleaned_data['podskupina']
            naziv = del_form.cleaned_data['naziv']
            shema = del_form.cleaned_data['shema']
            lastniska_skupina = del_form.cleaned_data['lastniska_skupina']

            # avtomatska oznaka
            st_delov = DelStavbe.objects.filter(podskupina=podskupina).count()
            if st_delov > 9:
                oznaka = str(podskupina.oznaka) + str(st_delov + 1)
            else:
                oznaka = str(podskupina.oznaka) + '0' + str(st_delov + 1)

            DelStavbe.objects.create_del(
                                         podskupina=podskupina,
                                         oznaka=oznaka,
                                         naziv=naziv,
                                         shema=shema,
                                         lastniska_skupina=lastniska_skupina,
                                         )

        return HttpResponseRedirect(reverse('moduli:deli:del_list'))


class DelDetailView(DetailView):
    template_name = "deli/delstavbe/detail/base.html"
    model = DelStavbe


class DelUpdateView(UpdateView):
    model = DelStavbe
    template_name = "deli/delstavbe/detail/update.html"
    fields = [
              'podskupina',
              'oznaka',
              'naziv',
              'lastniska_skupina',
              ]




class ElementDetailView(DetailView):
    template_name = "deli/element/detail/base.html"
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
