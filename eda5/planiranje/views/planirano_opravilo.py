# PYTHON ##############################################################
from datetime import datetime, timedelta


# DJANGO ##############################################################
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DetailView, UpdateView


# INTERNO ##############################################################
from ..forms import PlaniranoOpraviloCreateform
from ..models import Plan, PlaniranoOpravilo, PlaniranaAktivnost


# UVOŽENO ##############################################################

# Moduli
from eda5.moduli.models import Zavihek

# Katalog
from eda5.katalog.models import ArtikelPlan

# Predpisi
from eda5.predpisi.models import Predpis


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
            perioda_predpisana_enota = \
                planirano_opravilo_create_form.cleaned_data['perioda_predpisana_enota']

            perioda_predpisana_enota_kolicina = \
                planirano_opravilo_create_form.cleaned_data['perioda_predpisana_enota_kolicina']

            perioda_predpisana_kolicina_na_enoto = \
                planirano_opravilo_create_form.cleaned_data['perioda_predpisana_kolicina_na_enoto']

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

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="PLANIRANO_OPRAVILO_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        # PlaniranaAktivnost
        planirana_aktivnost_list = PlaniranaAktivnost.objects.filter(planirano_opravilo=self.object.id)
        context['planirana_aktivnost_list'] = planirana_aktivnost_list

        # Predpis
        # PlaniranoOpravilo --> PlaniranaAktivnost
        # PlaniranaAktivnost --> artikel_plan 
        # artikel_plan --> predpis_opravilo
        # predpis_opravilo --> predpis
        # predpis_opravilo --> artikel_plan

        # TESTIRANJE

        artikel_plan_list = []

        for planirana_aktivnost in planirana_aktivnost_list:
            artikel_plan_obj = planirana_aktivnost.artikel_plan
            artikel_plan_list.append(artikel_plan_obj)

        predpis_opravilo_list = []
        for artikel_plan in artikel_plan_list:
            predpis_opravilo_obj = artikel_plan.predpis_opravilo
            predpis_opravilo_list.append(predpis_opravilo_obj)

        # predpis_list = []
        # for predpis_opravilo in predpis_opravilo_list:
        #     predpis_obj = Predpis.objects.get(predpisopravilo=predpis_opravilo)
        #     predpis_list.append(predpis_obj)

        context['predpis_opravilo_list'] = predpis_opravilo_list

        return context
