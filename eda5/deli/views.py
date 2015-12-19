from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView
from django.db.models import Max

from .forms import DelCreateForm
from .models import DelStavbe, Skupina, Element, Podskupina

from eda5.delovninalogi.models import Opravilo, DelovniNalog
from eda5.katalog.models import ObratovalniParameter
from eda5.racunovodstvo.models import Strosek

from eda5.moduli.models import Zavihek


class DelHomeView(TemplateView):
    template_name = "deli/home.html"


class DelListView(ListView):
    template_name = "deli/delstavbe/list/base.html"
    model = Skupina

    def get_context_data(self, *args, **kwargs):
        context = super(DelListView, self).get_context_data(*args, **kwargs)
        context['del_form'] = DelCreateForm

        modul_zavihek = Zavihek.objects.get(oznaka="DEL_LIST")
        context['modul_zavihek'] = modul_zavihek

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

    def get_context_data(self, *args, **kwargs):
        context = super(DelDetailView, self).get_context_data(*args, **kwargs)
        modul_zavihek = Zavihek.objects.get(oznaka="DEL_DETAIL")
        context['modul_zavihek'] = modul_zavihek
        return context


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

        # sestavim sesznam delovnih-nalogov
        delovninalog_list = []
        for opravilo in opravila:
            delovninalog_list = DelovniNalog.objects.filter(opravilo=opravilo)
            list(delovninalog_list)

        context['opravilo_list'] = opravila
        context['delovninalog_list'] = delovninalog_list


        # opravila = Opravilo.objects.filter(element=self.object.id)
        # dn = DelovniNalog.objects.filter(opravilo=opravila).exclude(strosek__isnull=True)

        # dn_strosek_skp = 0

        # for dnx in dn:
        #     dn_strosek = dnx.strosek.strosek_z_ddv
        #     dn_strosek_skp = dn_strosek_skp + dn_strosek

        # dn_strosek_skp = str(round(dn_strosek_skp)) + ',00 EUR'

        # context['celotnistrosek'] = dn_strosek_skp

        # artikel = self.object.model_artikla
        # obratovalni_parametri = ObratovalniParameter.objects.filter(artikel=artikel)
        # context['obratovalni_parmateri'] = obratovalni_parametri

        nastavitve = self.object.nastavitev_set.all()
        context['nastavitve'] = nastavitve

        # DOLOČITEV ZADNJIH NASTAVLJENIH VREDNOSTI
        nastavitev_max = self.object.nastavitev_set.values("obratovalni_parameter").annotate(datum=Max("datum_nastavitve"))

        # sestavimo ustrezen seznam za izpis
        nastavitev_max_izpis = []
        for nastavitev in nastavitev_max:
            nastavitev_max_izpis.append(self.object.nastavitev_set.filter(
                obratovalni_parameter=nastavitev['obratovalni_parameter'], datum_nastavitve=nastavitev['datum'])[0])

        context['nastavitev_max'] = nastavitev_max_izpis

        return context


class DelCreateView(CreateView):

    model = DelStavbe
    form_class = DelCreateForm
    template_name = "deli/delstavbe/create.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DelCreateView, self).get_context_data(*args, **kwargs)
        modul_zavihek = Zavihek.objects.get(oznaka="DEL_CREATE")
        context['modul_zavihek'] = modul_zavihek
        return context
