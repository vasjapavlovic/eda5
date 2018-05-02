from datetime import timedelta, datetime


# DJANGO ##############################################################
from django.db.models import Max
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.db.models import F


# INTERNO ##############################################################
from ..forms import PlanCreateform
from ..models import Plan, PlaniranoOpravilo, PlanKontrolaSpecifikacija, PlanAktivnost, PlanKontrolaSkupina


# UVOŽENO ##############################################################

# Delovni Nalogi
from eda5.delovninalogi.models import Opravilo

# Moduli
from eda5.moduli.models import Zavihek


# Mixins
from braces.views import LoginRequiredMixin

# templated docs
from templated_docs import fill_template
from templated_docs.http import FileResponse
from eda5.reports.forms import FormatForm


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
        opravila_potrjena_planirana = opravila_vsa
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
        planirano_opravilo_zapadlo_list_pk = []
        planirano_opravilo_nezapadlo_list_pk = []

        for opravilo in max_opravila_potrjena_planirana:

            # pridobimo instanco zadnjega izvedenega opravila
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


            # ==================================================
            # Določitev datuma izvedenega opravila in naslednjega opravila
            # ===========================================================

            # pridobimo planirani datum izvedbe dela po odprtem opravilu
            opravilo = obj
            delovninalog_prvi = opravilo.delovninalog_set.first()
            delovninalog_prvi_planirano_dne = delovninalog_prvi.datum_plan
            datum_izvedeno_dne = delovninalog_prvi_planirano_dne

            if datum_izvedeno_dne:
                # glede na periodo posameznega opravila določimo še datum naslednjega opravila
                datum_naslednjega_opravila = datum_izvedeno_dne + leto + mesec + teden + dan

                # podatke o datumu izvedena pregleda in datumu naslednjega
                # pregleda zabeležimo v bazo planiranih opravil

                # pridobimo instanco planiranega opravila
                planirano_opravilo = PlaniranoOpravilo.objects.get(opravilo=opravilo)

                # datum izvedenega opravila
                planirano_opravilo.datum_izvedeno_dne = datum_izvedeno_dne


                # datum naslednje ponovitve opravila
                planirano_opravilo.datum_naslednjega_opravila = datum_naslednjega_opravila



                # shranimo spremembe v bazo
                planirano_opravilo.save()

                if datum_naslednjega_opravila < timezone.now().date():
                    planirano_opravilo_zapadlo_list_pk.append(obj.pk)
                else:
                    planirano_opravilo_nezapadlo_list_pk.append(obj.pk)

            else:
                # če je slučajno dodan delovninalog v čakanju ga izpustimo ker
                # trenutna nastavitev za osvežitev planiranih opravil
                # je glede na planirani datum prvega delovnega naloga
                opravilo = obj
                planirano_opravilo = PlaniranoOpravilo.objects.get(opravilo=opravilo)
                print(opravilo)
                print(planirano_opravilo)
                datum_naslednjega_opravila = planirano_opravilo.datum_naslednjega_opravila
                print(datum_naslednjega_opravila)
                if datum_naslednjega_opravila < timezone.now().date():
                    planirano_opravilo_zapadlo_list_pk.append(obj.pk)
                else:
                    planirano_opravilo_nezapadlo_list_pk.append(obj.pk)



        zapadla_opravila = Opravilo.objects.filter(pk__in=planirano_opravilo_zapadlo_list_pk).order_by('planirano_opravilo__datum_naslednjega_opravila')

        nezapadla_opravila = Opravilo.objects.filter(pk__in=planirano_opravilo_nezapadlo_list_pk).order_by('planirano_opravilo__datum_naslednjega_opravila')

        context['zapadla_opravila'] = zapadla_opravila
        context['nezapadla_opravila'] = nezapadla_opravila



        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="PLAN_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context


class PlanUpdateView(LoginRequiredMixin, UpdateView):
    model = Plan
    template_name = 'planiranje/plan/update.html'
    fields = ('id',)

    def get_context_data(self, *args, **kwargs):
        context = super(PlanUpdateView, self).get_context_data(*args, **kwargs)
        # tukaj prikažem formset za vnos

        plan = Plan.objects.get(id=self.get_object().pk)

        plan_aktivnost_list = PlanAktivnost.objects.filter(plan=plan)
        plan_aktivnost_list = plan_aktivnost_list.order_by('oznaka')

        context['plan_aktivnost_list'] = plan_aktivnost_list

        return context



class PlanPrintView(LoginRequiredMixin, UpdateView):

    model = Plan
    template_name = 'planiranje/plan/plan_print.html'
    fields = ('id', )


    def get_context_data(self, *args, **kwargs):
        context = super(PlanPrintView, self).get_context_data(*args, **kwargs)

        form = FormatForm()
        context['form'] = form

        plan = Plan.objects.get(id=self.object.id)
        planirano_opravilo_list = PlaniranoOpravilo.objects.filter(plan=plan)
        planirano_opravilo_list = planirano_opravilo_list.filter(is_active=True)
        planirano_opravilo_list = planirano_opravilo_list.order_by(
            'osnova__zap_st',
            'oznaka',
        )

        print_data = {
            'plan': plan,
            'planirano_opravilo_list': planirano_opravilo_list,

        }

        context['print_data'] = print_data
        return context



    def post(self, request, *args, **kwargs):

        plan = Plan.objects.get(id=self.get_object().pk)

        planirano_opravilo_list = PlaniranoOpravilo.objects.filter(plan=plan)
        planirano_opravilo_list = planirano_opravilo_list.filter(is_active=True)
        planirano_opravilo_list = planirano_opravilo_list.order_by(
            'osnova__zap_st',
            'oznaka',
        )

        print_data = {
            'plan': plan,
            'planirano_opravilo_list': planirano_opravilo_list,

        }

        form = FormatForm(request.POST or None)
        form_is_valid = False

        if form.is_valid():
            doctypex = form.cleaned_data['format_field']
            form_is_valid = True

        if form_is_valid == True:
            ###########################################################################
            # UKAZI
            ###########################################################################

            # pridobimo današnji datum za izpis na izpisu

            datum_danes = timezone.now().date()


            # prenos podatkov za aplikacijo templated_docs

            filename = fill_template(
                'obrazci/planiranje/plan/plan.ods', {'print_data': print_data, 'datum_danes': datum_danes}, output_format=doctypex)
            visible_filename = 'Plan {}.{}'.format(plan.oznaka, doctypex)

            return FileResponse(filename, visible_filename)


        # v primeru, da so zgornji Form-i NISO ustrezno izpolnjeni
        # izvrši spodnje ukaze

        else:
            return render(request, self.template_name, {
                'form': form,
                # 'deli_seznam_filter_form': deli_seznam_filter_form,
                }
            )
