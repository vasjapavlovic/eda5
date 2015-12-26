from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.db.models import Max
from datetime import datetime, timedelta
from django.utils import timezone

from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

from .forms import PlanCreateform, PlaniranoOpraviloCreateform
from .models import Plan, PlaniranoOpravilo, PlaniranaAktivnost

from eda5.moduli.models import Zavihek
from eda5.delovninalogi.models import Opravilo


class PlanCreateView(CreateView):

    model = Plan
    template_name = "planiranje/plan/create.html"
    form_class = PlanCreateform

    def get_context_data(self, *args, **kwargs):
        context = super(PlanCreateView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="PLAN_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context


class PlanListView(ListView):

    model = Plan
    template_name = "planiranje/plan/list/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PlanListView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="PLAN_LIST")
        context['modul_zavihek'] = modul_zavihek

        return context


class PlanDetailView(DetailView):

    model = Plan
    template_name = "planiranje/plan/detail/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PlanDetailView, self).get_context_data(*args, **kwargs)

        # PlanOpravilo
        planirano_opravilo_list = PlaniranoOpravilo.objects.filter(plan=self.object.id)
        context['planirano_opravilo_list'] = planirano_opravilo_list

        #########################################################################################
        # SLDENJE PLANU: ZAPADLA OPRAVILA; OPRAVILA V PLANU; FAZA PLANIRANJA; IZVEDENA OPRAVILA #
        #########################################################################################
        opravila_potrjena = Opravilo.objects.filter(is_potrjen=True)
        opravila_potrjena_planirana = opravila_potrjena.filter(planirano_opravilo__isnull=False)
        max_opravila_potrjena_planirana = opravila_potrjena_planirana.values(
            "planirano_opravilo").annotate(datum_izvedbe=Max("created"))

        # Zadnje izvedena Planirana Opravila
        # ==================================
        opravilo_planirano_zadnje_list = []

        for opravilo in max_opravila_potrjena_planirana:

            obj = Opravilo.objects.filter(
                planirano_opravilo=opravilo['planirano_opravilo'],
                created=opravilo['datum_izvedbe'])[0]

            opravilo_planirano_zadnje_list.append(obj)

        context['opravilo_planirano_zadnje_list'] = opravilo_planirano_zadnje_list

        # Zapadla Planirana Opravila
        # ==========================
        planirano_opravilo_zapadlo_list = []
        planirano_opravilo_nezapadlo_list = []

        for opravilo in max_opravila_potrjena_planirana:

            obj = Opravilo.objects.filter(
                planirano_opravilo=opravilo['planirano_opravilo'],
                created=opravilo['datum_izvedbe'])[0]

            # datum planirane izvedbe
            perioda_oznaka = obj.planirano_opravilo.perioda_predpisana_enota
            perioda_kolicina = obj.planirano_opravilo.perioda_predpisana_enota_kolicina

            if perioda_oznaka == "leto":
                leto = timedelta(days=perioda_kolicina*365)
            else:
                leto = timedelta(days=0)

            if perioda_oznaka == "mesec":
                mesec = timedelta(days=perioda_kolicina*31)
            else:
                mesec = timedelta(days=0)

            if perioda_oznaka == "teden":
                teden = timedelta(weeks=perioda_kolicina)
            else:
                teden = timedelta(weeks=0)

            if perioda_oznaka == "dan":
                dan = timedelta(days=perioda_kolicina)
            else:
                dan = timedelta(days=0)

            datum_naslednjega_opravila = obj.created + leto + mesec + teden + dan

            if datum_naslednjega_opravila < timezone.now():
                planirano_opravilo_zapadlo_list.append(obj)
            else:
                planirano_opravilo_nezapadlo_list.append(obj)

        context['planirano_opravilo_zapadlo_list'] = planirano_opravilo_zapadlo_list
        context['planirano_opravilo_nezapadlo_list'] = planirano_opravilo_nezapadlo_list

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="PLAN_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context


class PlaniranoOpraviloCreateView(UpdateView):
    model = Plan
    template_name = "planiranje/planirano_opravilo/create_from_plan.html"
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):
        context = super(PlaniranoOpraviloCreateView, self).get_context_data(*args, **kwargs)

        # opravilo
        context['planirano_opravilo_create_form'] = PlaniranoOpraviloCreateform

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="PLANIRANO_OPRAVILO_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        # object
        plan = Plan.objects.get(id=self.get_object().id)

        # forms
        planirano_opravilo_create_form = PlaniranoOpraviloCreateform(request.POST or None)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="PLANIRANO_OPRAVILO_CREATE")

        # izdelamo opravilo (!!!elemente opravilu dodamo kasneje)
        if planirano_opravilo_create_form.is_valid():
            oznaka = planirano_opravilo_create_form.cleaned_data['oznaka']
            naziv = planirano_opravilo_create_form.cleaned_data['naziv']
            namen = planirano_opravilo_create_form.cleaned_data['namen']
            obseg = planirano_opravilo_create_form.cleaned_data['obseg']
            perioda_predpisana_enota = planirano_opravilo_create_form.cleaned_data['perioda_predpisana_enota']
            perioda_predpisana_enota_kolicina = planirano_opravilo_create_form.cleaned_data['perioda_predpisana_enota_kolicina']
            perioda_predpisana_kolicina_na_enoto = planirano_opravilo_create_form.cleaned_data['perioda_predpisana_kolicina_na_enoto']
            opomba = planirano_opravilo_create_form.cleaned_data['opomba']

            PlaniranoOpravilo.objects.create_planirano_opravilo(
                oznaka=oznaka,
                naziv=naziv,
                namen=namen,
                obseg=obseg,
                perioda_predpisana_enota=perioda_predpisana_enota,
                perioda_predpisana_enota_kolicina=perioda_predpisana_enota_kolicina,
                perioda_predpisana_kolicina_na_enoto=perioda_predpisana_kolicina_na_enoto,
                opomba=opomba,
                plan=plan,
            )

        else:
            return render(request, self.template_name, {
                'planirano_opravilo_create_form': planirano_opravilo_create_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        return HttpResponseRedirect(reverse('moduli:planiranje:plan_detail', kwargs={'pk': plan.pk}))


class PlaniranoOpraviloDetailView(DetailView):

    model = PlaniranoOpravilo
    template_name = "planiranje/planirano_opravilo/detail/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PlaniranoOpraviloDetailView, self).get_context_data(*args, **kwargs)

        # PlaniranaAktivnost
        planirana_aktivnost_list = PlaniranaAktivnost.objects.filter(planirano_opravilo=self.object.id)
        context['planirana_aktivnost_list'] = planirana_aktivnost_list

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="PLANIRANO_OPRAVILO_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context
