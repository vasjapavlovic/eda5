# Python
from datetime import datetime, timedelta
import os

# Django
from django import forms
from django.core.context_processors import csrf
from django.conf import settings
from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.utils import timezone
from django.utils.html import escape  # popup
from django.views.generic import TemplateView, ListView, DetailView, UpdateView

# Models
from ..models import Opravilo, VzorecOpravila
from eda5.deli.models import Skupina, Podskupina, DelStavbe, ProjektnoMesto
from eda5.moduli.models import Zavihek
from eda5.planiranje.models import SkupinaPlanov, Plan, PlaniranoOpravilo
from eda5.pomanjkljivosti.models import Pomanjkljivost
from eda5.zahtevki.models import Zahtevek

# Forms
from ..forms import OpraviloUpdateForm, VzorecOpravilaIzbiraForm, OpraviloCreateForm
from ..forms import OpraviloElementUpdateForm, OpraviloPomanjkljivostUpdateForm, OpraviloNalogaUpdateForm
from eda5.deli.forms import projektnomesto_forms

# Mixins
from ..mixins import MessagesActionMixin


# #########################################################
# OPRAVILO LIST VIEW
# #########################################################
class OpraviloListView(ListView):
    model = Opravilo
    template_name = "delovninalogi/opravilo/list.html"


# #########################################################
# OPRAVILO DETAIL VIEW
# #########################################################
class OpraviloDetailView(DetailView):
    model = Opravilo
    template_name = "delovninalogi/opravilo/detail/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(OpraviloDetailView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="OPRAVILO_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context


# #########################################################
# OPRAVILO VZOREC UPDATE VIEW
# #########################################################
class OpraviloVzorecDetailView(DetailView):
    model = VzorecOpravila
    template_name = "delovninalogi/vzorec_opravila/detail/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(OpraviloVzorecUpdateView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="VZOREC_OPRAVILA_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context



# #########################################################
# OPRAVILO UPDATE VIEW
# #########################################################
class OpraviloUpdateView(UpdateView):
    model = Opravilo
    form_class = OpraviloUpdateForm
    template_name = "delovninalogi/opravilo/update.html"


# #########################################################
# OPRAVILO SPLOŠNO CREATE VIEW
# #########################################################
class OpraviloCreateFromZahtevekView(UpdateView):
    model = Zahtevek
    template_name = "delovninalogi/opravilo/create_from_zahtevek.html"
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):
        context = super(OpraviloCreateFromZahtevekView, self).get_context_data(*args, **kwargs)

        # opravilo
        context['opravilo_create_form'] = OpraviloCreateForm
        context['opravilo_element_update_form'] = OpraviloElementUpdateForm
        context['opravilo_naloga_update_form'] = OpraviloNalogaUpdateForm

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="OPRAVILO_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        # ====================================
        # FORMS
        # ====================================

        opravilo_create_form = OpraviloCreateForm(request.POST or None)
        opravilo_element_update_form = OpraviloElementUpdateForm(request.POST or None)
        opravilo_naloga_update_form = OpraviloNalogaUpdateForm(request.POST or None)

        ''' Vsi forms za vnose so nazačetku neustrezno izpolnjeni.
        Pomembno zaradi načina struktura View-ja '''

        opravilo_create_form_is_valid = False
        opravilo_element_update_form_is_valid = False
        opravilo_naloga_update_form_is_valid = False

        ###########################################################################
        # PRIDOBIMO PODATKE
        ###########################################################################

        # zahtevek
        zahtevek = Zahtevek.objects.get(id=self.get_object().id)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="OPRAVILO_CREATE")

        # podatki o opravilu
        if opravilo_create_form.is_valid():
            oznaka = opravilo_create_form.cleaned_data['oznaka']
            naziv = opravilo_create_form.cleaned_data['naziv']
            rok_izvedbe = opravilo_create_form.cleaned_data['rok_izvedbe']
            narocilo = opravilo_create_form.cleaned_data['narocilo']
            nosilec = opravilo_create_form.cleaned_data['nosilec']
            planirano_opravilo = opravilo_create_form.cleaned_data['planirano_opravilo']
            opravilo_create_form_is_valid = True

        # podatki o izbranih elementih, ki se dodajo opravilu
        if opravilo_element_update_form.is_valid():
            element = opravilo_element_update_form.cleaned_data['element']
            opravilo_element_update_form_is_valid = True

        ''' Pridobimo podatek o izbranih nalogah, ki se
        bodo v opravilu odpravljale '''

        if opravilo_naloga_update_form.is_valid():
            # seznam pomanjkljivosti
            naloga_list = opravilo_naloga_update_form.cleaned_data['naloga']
            # ukaz, da je form ustrezno izpolnjen
            opravilo_naloga_update_form_is_valid = True

        ''' v primeru, da so zgornji Form-i ustrezno izpolnjeni
        izvrši spodnje ukaze '''

        if opravilo_create_form_is_valid == True and \
            opravilo_element_update_form_is_valid == True and \
            opravilo_naloga_update_form_is_valid == True:
            ###########################################################################
            # UKAZI
            ###########################################################################

            # Izdelamo novo opravilo kjer se kasneje dodatno dopolni
            # na katerih elementih se opravilo opravlja ter katere
            # pomanjkljivosti se odpravljajo v tem opravilu.

            opravilo_data = Opravilo.objects.create_opravilo(
                oznaka=oznaka,
                naziv=naziv,
                rok_izvedbe=rok_izvedbe,
                narocilo=narocilo,
                zahtevek=zahtevek,
                nosilec=nosilec,
                planirano_opravilo=planirano_opravilo,
            )

            # instanco izdelanega opravila shranimo za nadaljno uporabo

            opravilo_object = Opravilo.objects.get(id=opravilo_data.pk)

            ''' opravilu dodelimo izbrane naloge '''

            opravilo_object.naloga = naloga_list

            # Posodobitev opravila tako, da se pove na katerih elementih
            # stavbe se opravilo izvaja. Pomembno za elektronsko servisno
            # knjigo.

            opravilo_object.element = element
            opravilo_object.save()

            # če je izbrano planirano_opravilo pridobi podatek "zmin - zaokroževanje"
            # iz planiranega opravila

            if planirano_opravilo:
                zmin = planirano_opravilo.zmin
                opravilo_object.zmin = zmin
                opravilo_object.save()

            # izvedemo preusmeritev

            return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk}))

        # če zgornji formi niso ustrezno izpolnjeni

        else:
            return render(request, self.template_name, {
                'opravilo_create_form': opravilo_create_form,
                'opravilo_element_update_form': opravilo_element_update_form,
                'opravilo_naloga_update_form': opravilo_naloga_update_form,
                'modul_zavihek': modul_zavihek,
                }
            )


# #########################################################
# OPRAVILO ODPRAVA POMANJKLJIVOSTI CREATE VIEW
# #########################################################
class OpraviloCreatePomanjkljivosti(UpdateView):
    model = Zahtevek
    template_name = "delovninalogi/opravilo/create_pomanjkljivosti.html"
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):
        context = super(OpraviloCreatePomanjkljivosti, self).get_context_data(*args, **kwargs)

        # opravilo
        context['opravilo_create_form'] = OpraviloCreateForm
        context['opravilo_naloga_update_form'] = OpraviloNalogaUpdateForm
        context['opravilo_pomanjkljivost_update_form'] = OpraviloPomanjkljivostUpdateForm

        # seznam pomanjkljivosti, ki se že rešujejo
        pomanjkljivosti_likvidirane_pod_zahtevek = Pomanjkljivost.objects.filter(zahtevek=self.get_object(), opravilo__isnull=True)
        context['pomanjkljivosti_likvidirane_pod_zahtevek'] = pomanjkljivosti_likvidirane_pod_zahtevek

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="OPRAVILO_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        ###########################################################################
        # FORMS
        ###########################################################################

        opravilo_create_form = OpraviloCreateForm(request.POST or None)
        opravilo_naloga_update_form = OpraviloNalogaUpdateForm(request.POST or None)
        opravilo_pomanjkljivost_update_form = OpraviloPomanjkljivostUpdateForm(request.POST or None)

        ''' Vsi forms za vnose so nazačetku neustrezno izpolnjeni.
        Pomembno zaradi načina struktura View-ja '''

        opravilo_create_form_is_valid = False
        opravilo_naloga_update_form_is_valid = False
        opravilo_pomanjkljivost_update_form_is_valid = False

        ###########################################################################
        # PRIDOBIMO PODATKE
        ###########################################################################

        ''' Pridobimo instanco zahtevka kjer se bo pomanjkljivost 
        nahajala '''

        zahtevek = Zahtevek.objects.get(id=self.get_object().id)

        ''' Pridobimo instanco zahtevka kjer se bo pomanjkljivost 
        nahajala '''

        modul_zavihek = Zavihek.objects.get(oznaka="OPRAVILO_CREATE")

        ''' Pridobimo podatke o opravilu '''

        if opravilo_create_form.is_valid():
            oznaka = opravilo_create_form.cleaned_data['oznaka']
            naziv = opravilo_create_form.cleaned_data['naziv']
            rok_izvedbe = opravilo_create_form.cleaned_data['rok_izvedbe']
            narocilo = opravilo_create_form.cleaned_data['narocilo']
            nosilec = opravilo_create_form.cleaned_data['nosilec']
            planirano_opravilo = opravilo_create_form.cleaned_data['planirano_opravilo']
            # ukaz, da je form ustrezno izpolnjen
            opravilo_create_form_is_valid = True

        ''' Pridobimo podatek o izbranih nalogah, ki se
        bodo v opravilu odpravljale '''

        if opravilo_naloga_update_form.is_valid():
            # seznam pomanjkljivosti
            naloga_list = opravilo_naloga_update_form.cleaned_data['naloga']
            # ukaz, da je form ustrezno izpolnjen
            opravilo_naloga_update_form_is_valid = True

        ''' Pridobimo podatek o izbranih pomanjkljivostih, ki se
        bodo v opravilu odpravljale '''

        if opravilo_pomanjkljivost_update_form.is_valid():
            # seznam pomanjkljivosti
            pomanjkljivost_list = opravilo_pomanjkljivost_update_form.cleaned_data['pomanjkljivost']
            # ukaz, da je form ustrezno izpolnjen
            opravilo_pomanjkljivost_update_form_is_valid = True

        ''' v primeru, da so zgornji Form-i ustrezno izpolnjeni
        izvrši spodnje ukaze '''

        if opravilo_create_form_is_valid == True and \
            opravilo_pomanjkljivost_update_form_is_valid == True and \
            opravilo_naloga_update_form_is_valid == True:
            ###########################################################################
            # UKAZI
            ###########################################################################

            ''' Izdelamo novo opravilo kjer se kasneje dodatno dopolni
            na katerih elementih se opravilo opravlja ter katere
            pomanjkljivosti se odpravljajo v tem opravilu. '''

            opravilo_data = Opravilo.objects.create_opravilo(
                oznaka=oznaka,
                naziv=naziv,
                rok_izvedbe=rok_izvedbe,
                narocilo=narocilo,
                zahtevek=zahtevek,
                nosilec=nosilec,
                planirano_opravilo=planirano_opravilo,
            )

            ''' Instanco izdelanega opravila spravimo za nadaljno
            uporabo '''

            opravilo_object = Opravilo.objects.get(id=opravilo_data.pk)

            ''' opravilu dodelimo izbrane naloge '''

            opravilo_object.naloga = naloga_list
        
            ''' opravilu dodelimo izbrane pomanjkljivosti '''

            opravilo_object.pomanjkljivost = pomanjkljivost_list

            ''' opravilu dodelimo elemente, ki so vezani na pomanjkljivost '''
            
            element_list = []
            for pomanjkljivost in pomanjkljivost_list:
                for element in pomanjkljivost.element.all():
                    element_list.append(element)

            opravilo_object.element = element_list

            ''' spravimo zgoraj navedene ukaze v bazi '''

            opravilo_object.save()

            ''' izvedemo preusmeritev '''

            return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk}))


        # v primeru, da so zgornji Form-i NISO ustrezno izpolnjeni
        # izvrši spodnje ukaze

        else:
            return render(request, self.template_name, {
                'opravilo_create_form': opravilo_create_form,
                'opravilo_naloga_update_form': opravilo_naloga_update_form,
                'opravilo_pomanjkljivost_update_form': opravilo_pomanjkljivost_update_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        


# #########################################################
# OPRAVILO CREATE FROM VZOREC VIEW
# #########################################################
class OpraviloCreateFromVzorecFromZahtevekView(UpdateView):
    model = Zahtevek
    template_name = "delovninalogi/opravilo/create_from_vzorec_opravila.html"
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):
        context = super(OpraviloCreateFromVzorecFromZahtevekView, self).get_context_data(*args, **kwargs)

        # vzorec opravila
        context['vzorec_opravila_izbira_form'] = VzorecOpravilaIzbiraForm

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="OPRAVILO_FROM_VZOREC_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        # object
        zahtevek = Zahtevek.objects.get(id=self.get_object().id)

        # forms
        vzorec_opravila_izbira_form = VzorecOpravilaIzbiraForm(request.POST or None)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="OPRAVILO_FROM_VZOREC_CREATE")

        # izdelamo opravilo (!!!elemente opravilu dodamo kasneje)
        if vzorec_opravila_izbira_form.is_valid():
            vzorec_opravila = vzorec_opravila_izbira_form.cleaned_data['vzorec_opravila']

            # nova oznaka opravila
            try:
                leto = timezone.now().date().year
                zap_st = Opravilo.objects.all().count()
                zap_st = zap_st + 1
            except:
                zap_st = 1

            nova_oznaka = "OPR-%s-%s" % (leto, zap_st)  #

            # iz VzorecOpravila poberemo podatke
            oznaka = nova_oznaka
            naziv = vzorec_opravila.naziv
            rok_izvedbe = timezone.now().date()  # rok izvedbe izhaja iz zadnjega dodanega + perioda
            narocilo = vzorec_opravila.narocilo
            nosilec = vzorec_opravila.nosilec
            planirano_opravilo = vzorec_opravila.planirano_opravilo
            element_list = vzorec_opravila.element.all()

            opravilo_data = Opravilo.objects.create_opravilo(
                oznaka=oznaka,
                naziv=naziv,
                rok_izvedbe=rok_izvedbe,
                narocilo=narocilo,
                zahtevek=zahtevek,
                nosilec=nosilec,
                planirano_opravilo=planirano_opravilo,
            )

            opravilo_object = Opravilo.objects.get(id=opravilo_data.pk)

            # shranimo še elemente, ki so v ManyToMany relaciji z opravilom
            opravilo_object.element = element_list
            opravilo_object.save()

            return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk}))

        else:
            return render(request, self.template_name, {
                'vzorec_opravila_izbira_form': vzorec_opravila_izbira_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        


# view called with ajax to reload the month drop down list
def reload_controls_planiranje_skupina_planov_view(request):

    c = {}
    c.update(csrf(request))

    context = {}
    # get the object
    skupina_planov = request.POST['skupina_planov']
    skupina_planov = SkupinaPlanov.objects.get(id=skupina_planov)
    # podskupine glede na izbrano skupino
    plan_list = []
    for plan in skupina_planov.plan_set.all():
        plan_list.append(plan.id)

    # OUTPUT FILTER
    # Podskupine
    context['plan_to_display'] = plan_list

    return JsonResponse(context)


# view called with ajax to reload the month drop down list
def reload_controls_planiranje_plan_view(request):

    c = {}
    c.update(csrf(request))

    context = {}
    # get the object
    plan = request.POST['plan']
    plan = Plan.objects.get(id=plan)

    planirano_opravilo_list = []
    for planirano_opravilo in plan.planiranoopravilo_set.filter(is_active=True):
        planirano_opravilo_list.append(planirano_opravilo.id)

    # OUTPUT FILTER

    context['planirano_opravilo_to_display'] = planirano_opravilo_list

    return JsonResponse(context)


# view called with ajax to reload the month drop down list
def reload_controls_delovninalogi_planirano_opravilo_view(request):

    c = {}
    c.update(csrf(request))

    context = {}
    # get the object
    planirano_opravilo = request.POST['planirano_opravilo']
    planirano_opravilo = PlaniranoOpravilo.objects.get(id=planirano_opravilo)

    vzorec_opravila_list = []
    for vzorec_opravila in planirano_opravilo.vzorecopravila_set.all():
        vzorec_opravila_list.append(vzorec_opravila.id)

    # OUTPUT FILTER

    # DelStavbe
    context['vzorec_opravila_to_display'] = vzorec_opravila_list

    return JsonResponse(context)






###########################################################
# OPRAVILO ODPRAVA POMANJKLJIVOSTI CREATE VIEW
###########################################################

        ###########################################################################
        # FORMS
        ###########################################################################

        ###########################################################################
        # PRIDOBIMO PODATKE
        ###########################################################################

            ###########################################################################
            # UKAZI
            ###########################################################################






