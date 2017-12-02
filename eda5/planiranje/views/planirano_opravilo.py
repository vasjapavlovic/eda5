# PYTHON ##############################################################
from datetime import datetime, timedelta

# DJANGO ##############################################################
from django.core.urlresolvers import reverse
from django.db.models import F, Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DetailView, UpdateView

# Models
from ..models import Plan
from ..models import PlaniranoOpravilo
from ..models import PlaniranaAktivnost
from eda5.delovninalogi.models import DelovniNalog
from eda5.delovninalogi.models import Delo
from eda5.delovninalogi.models import Opravilo
from eda5.delovninalogi.models import VzorecOpravila
from eda5.katalog.models import ArtikelPlan
from eda5.moduli.models import Zavihek
from eda5.predpisi.models import Predpis

# Forms
from ..forms import PlaniranoOpraviloCreateform
from eda5.deli.forms import projektnomesto_forms
from eda5.delovninalogi.forms import OpraviloElementUpdateForm
from eda5.delovninalogi.forms import VzorecOpravilaCreateForm





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

            zmin = planirano_opravilo_create_form.cleaned_data['zmin']

            PlaniranoOpravilo.objects.create_planirano_opravilo(
                oznaka=oznaka,
                naziv=naziv,
                namen=namen,
                obseg=obseg,
                perioda_predpisana_enota=perioda_predpisana_enota,
                perioda_predpisana_enota_kolicina=perioda_predpisana_enota_kolicina,
                perioda_predpisana_kolicina_na_enoto=perioda_predpisana_kolicina_na_enoto,
                opomba=opomba,
                zmin=zmin,
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

        # instanca
        planirano_opravilo = self.object.id

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
            if artikel_plan:
                predpis_opravilo_obj = artikel_plan.predpis_opravilo
                predpis_opravilo_list.append(predpis_opravilo_obj)

        # predpis_list = []
        # for predpis_opravilo in predpis_opravilo_list:
        #     predpis_obj = Predpis.objects.get(predpisopravilo=predpis_opravilo)
        #     predpis_list.append(predpis_obj)

        context['predpis_opravilo_list'] = predpis_opravilo_list



        # DNEVNIK IZVEDENIH DEL (delovni nalogi)

        # Seznam delovnih nalogov glede na izbrano planirano opravilo
        opravila_izvedena_list = DelovniNalog.objects.filter(opravilo__planirano_opravilo=planirano_opravilo)
        # Prikaži samo zaključene delovne naloge
        opravila_izvedena_list = opravila_izvedena_list.filter(status=4).annotate(porabljen_cas=Sum('delo__delo_cas_rac'))
        # Razvrsti delovne naloge od zadnjega proti prvemu glede na datum izvedbe
        opravila_izvedena_list = opravila_izvedena_list.order_by('-datum_stop')
        # izpišemo vsebino v context
        context['opravila_izvedena_list'] = opravila_izvedena_list


        # POROČANJE O PORABLJENEM ČASU ZA POSAMEZNO OPRAVILO

        def zaokrozen_zmin(time_input, zmin, operator):
            '''
            zaokroži čas glede na zmin podan v minutah
            Author: Vasja Pavlovič 2017
            '''
            hours, reminder = divmod(time_input.seconds, 3600)
            minutes, seconds = divmod(reminder, 60)
            # koliko je celih
            x, ostanek = divmod(minutes, zmin)
            if ostanek > 0:
                if operator == "+":
                    x = x + 1
                if operator == "-":
                    x
            # če je x=6 je potrebno tudi uro povečati +1
            if x == 6:
                hours = hours + 1
            hours = hours
            minutes = zmin * x
            seconds = 0
            zaokrozen_zmin = timedelta(hours=hours, minutes=minutes, seconds=seconds)
            return zaokrozen_zmin

        def pretvori_v_ure(time_input):
            '''
            timedelta object pretvori v ure npr. timedelta(hours=x)
            '''
            seconds = time_input.seconds
            skupaj_ur = seconds/3600
            return skupaj_ur


        ##################################################################
        '''
        Izpis del v delovnem nalogu
        '''
        ##################################################################

        for delovninalog in opravila_izvedena_list:

            # enota za zaokroževanje
            zmin = delovninalog.opravilo.zmin
            # seznam del pod delovnim nalogom
            delo_list = Delo.objects.filter(delovninalog=delovninalog).annotate(delo_cas=F('time_stop')-F('time_start'))


            for delo in delo_list:
                # osnovni delo_cas
                delo_cas = delo.delo_cas
                # zaokrožen delo_cas
                delo_cas_rac = zaokrozen_zmin(delo_cas, zmin, '+')
                # pretvorjen v decimalno številko delo_cas
                delo_cas_rac = pretvori_v_ure(delo_cas_rac)
                # shranimo v bazo
                delo.delo_cas_rac = delo_cas_rac
                delo.save()



        return context


class VzorecOpravilaCreateView(UpdateView):
    model = PlaniranoOpravilo
    template_name = "delovninalogi/vzorec_opravila/create_from_planirano_opravilo.html"
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):
        context = super(VzorecOpravilaCreateView, self).get_context_data(*args, **kwargs)

        # opravilo
        context['vzorec_opravila_create_form'] = VzorecOpravilaCreateForm
        context['opravilo_element_update_form'] = OpraviloElementUpdateForm
        context['element_izbira_form'] = projektnomesto_forms.ElementIzbiraForm

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="VZOREC_OPRAVILA_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        # object
        planirano_opravilo = PlaniranoOpravilo.objects.get(id=self.get_object().id)

        # forms
        vzorec_opravila_create_form = VzorecOpravilaCreateForm(request.POST or None)
        opravilo_element_update_form = OpraviloElementUpdateForm(request.POST or None)
        element_izbira_form = projektnomesto_forms.ElementIzbiraForm(request.POST or None)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="VZOREC_OPRAVILA_CREATE")

        # izdelamo opravilo (!!!elemente opravilu dodamo kasneje)
        if vzorec_opravila_create_form.is_valid():
            oznaka = vzorec_opravila_create_form.cleaned_data['oznaka']
            naziv = vzorec_opravila_create_form.cleaned_data['naziv']
            rok_izvedbe = vzorec_opravila_create_form.cleaned_data['rok_izvedbe']
            narocilo = vzorec_opravila_create_form.cleaned_data['narocilo']
            nosilec = vzorec_opravila_create_form.cleaned_data['nosilec']
            vrsta_stroska = vzorec_opravila_create_form.cleaned_data['vrsta_stroska']

            vzorec_opravila_data = VzorecOpravila.objects.create_vzorec_opravila(
                oznaka=oznaka,
                naziv=naziv,
                rok_izvedbe=rok_izvedbe,
                narocilo=narocilo,
                nosilec=nosilec,
                vrsta_stroska=vrsta_stroska,
                planirano_opravilo=planirano_opravilo,
            )

            vzorec_opravila_object = VzorecOpravila.objects.get(id=vzorec_opravila_data.pk)

        else:
            return render(request, self.template_name, {
                'vzorec_opravila_create_form': vzorec_opravila_create_form,
                'opravilo_element_update_form': opravilo_element_update_form,
                'element_izbira_form': element_izbira_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        if opravilo_element_update_form.is_valid():
            element = opravilo_element_update_form.cleaned_data['element']

            vzorec_opravila_object.element = element
            vzorec_opravila_object.save()

        else:
            return render(request, self.template_name, {
                'vzorec_opravila_create_form': vzorec_opravila_create_form,
                'opravilo_element_update_form': opravilo_element_update_form,
                'element_izbira_form': element_izbira_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        return HttpResponseRedirect(reverse(
                    'moduli:planiranje:planirano_opravilo_detail',
                    kwargs={'pk': planirano_opravilo.pk})
                    )
