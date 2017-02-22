# PYTHON ##############################################################
from datetime import timedelta


# DJANGO ##############################################################
from django.db.models import Max
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView


# INTERNO ##############################################################
from ..forms import PlanCreateform
from ..models import Plan, PlaniranoOpravilo


# UVOŽENO ##############################################################

# Delovni Nalogi
from eda5.delovninalogi.models import Opravilo

# Moduli
from eda5.moduli.models import Zavihek


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
        planirano_opravilo_list = PlaniranoOpravilo.objects.filter(
            plan=self.object.id,  # opravila ki so del plana
            is_active=True,  # samo aktivna opravila želimo, da se prikažejo na seznamu
            )
        context['planirano_opravilo_list'] = planirano_opravilo_list

        #########################################################################################
        # SLDENJE PLANU: ZAPADLA OPRAVILA; OPRAVILA V PLANU; FAZA PLANIRANJA; IZVEDENA OPRAVILA #
        #########################################################################################

        opravila_vsa = Opravilo.objects.filter(
            planirano_opravilo__plan=self.object.id,  # opravila ki so del plana
            planirano_opravilo__is_active=True,  # samo aktivna opravila želimo, da se prikažejo na seznamu
            )

        # zaenkrat tudi nepotrjena opravila iz strani nadzornika
        opravila_potrjena_planirana = opravila_vsa.filter(planirano_opravilo__isnull=False)
        max_opravila_potrjena_planirana = opravila_potrjena_planirana.values(
            "planirano_opravilo").annotate(datum_izvedbe=Max("created"))

        # Dnevnik izvedenih opravil oziroma delovnih nalogov
        # ==================================
        context['opravila_potrjena_planirana'] = opravila_potrjena_planirana

        delovni_nalog_zakljucen_list = []
        for opravilo in opravila_potrjena_planirana:
            for dn in opravilo.delovninalog_set.filter(status=4):
                delovni_nalog_zakljucen_list.append(dn)

        context['delovni_nalog_zakljucen_list'] = delovni_nalog_zakljucen_list


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

        dn_planirano_opravilo_zapadlo_list = []
        for opravilo in planirano_opravilo_zapadlo_list:
            for dn in opravilo.delovninalog_set.all():
                dn_planirano_opravilo_zapadlo_list.append(dn)

        context['dn_planirano_opravilo_zapadlo_list'] = dn_planirano_opravilo_zapadlo_list

        dn_planirano_opravilo_nezapadlo_list = []
        for opravilo in planirano_opravilo_nezapadlo_list:
            for dn in opravilo.delovninalog_set.all():
                dn_planirano_opravilo_nezapadlo_list.append(dn)

        context['dn_planirano_opravilo_nezapadlo_list'] = dn_planirano_opravilo_nezapadlo_list





        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="PLAN_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context
