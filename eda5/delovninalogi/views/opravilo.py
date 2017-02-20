# PYTHON ##############################################################
from datetime import datetime, timedelta
import os


# DJANGO ##############################################################
from django.core.context_processors import csrf
from django.conf import settings
from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import TemplateView, ListView, DetailView, UpdateView





# UVOZI ZNOTRAJ APLIKACIJE ############################################
from ..forms import \
    OpraviloUpdateForm, \
    VzorecOpravilaIzbiraForm, \
    OpraviloCreateForm, \
    OpraviloElementUpdateForm, \
    OpraviloPomanjkljivostUpdateForm

from ..models import \
    Opravilo, \
    VzorecOpravila

from ..mixins import MessagesActionMixin


# UVOZI ZUNANJIH APLIKAIJ ############################################

# Deli
from eda5.deli.forms import ElementIzbiraForm
from eda5.deli.models import Skupina, Podskupina, DelStavbe, ProjektnoMesto 

# Moduli
from eda5.moduli.models import Zavihek

# Planiranje
from eda5.planiranje.models import SkupinaPlanov, Plan, PlaniranoOpravilo

# Zahtevki
from eda5.zahtevki.models import Zahtevek


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
# OPRAVILO CREATE VIEW
# #########################################################
class OpraviloCreateFromZahtevekView(UpdateView):
    model = Zahtevek
    template_name = "delovninalogi/opravilo/create_from_zahtevek.html"
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):
        context = super(OpraviloCreateFromZahtevekView, self).get_context_data(*args, **kwargs)

        # opravilo
        context['opravilo_create_form'] = OpraviloCreateForm
        context['element_izbira_form'] = ElementIzbiraForm
        context['opravilo_element_update_form'] = OpraviloElementUpdateForm
        context['opravilo_pomanjkljivost_update_form'] = OpraviloPomanjkljivostUpdateForm

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="OPRAVILO_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        # object
        zahtevek = Zahtevek.objects.get(id=self.get_object().id)

        # forms
        opravilo_create_form = OpraviloCreateForm(request.POST or None)
        element_izbira_form = ElementIzbiraForm(request.POST or None)
        opravilo_element_update_form = OpraviloElementUpdateForm(request.POST or None)
        opravilo_pomanjkljivost_update_form = OpraviloPomanjkljivostUpdateForm(request.POST or None)
        

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="OPRAVILO_CREATE")


        ''' Izdelamo novo opravilo kjer se kasneje dodatno dopolni
        na katerih elementih se opravilo opravlja ter katere
        pomanjkljivosti se odpravljajo v tem opravilu. '''

        if opravilo_create_form.is_valid():
            oznaka = opravilo_create_form.cleaned_data['oznaka']
            naziv = opravilo_create_form.cleaned_data['naziv']
            rok_izvedbe = opravilo_create_form.cleaned_data['rok_izvedbe']
            narocilo = opravilo_create_form.cleaned_data['narocilo']
            nosilec = opravilo_create_form.cleaned_data['nosilec']
            planirano_opravilo = opravilo_create_form.cleaned_data['planirano_opravilo']

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

        else:
            return render(request, self.template_name, {
                'opravilo_create_form': opravilo_create_form,
                'element_izbira_form': element_izbira_form,
                'opravilo_element_update_form': opravilo_element_update_form,
                'opravilo_pomanjkljivost_update_form': opravilo_pomanjkljivost_update_form,
                'modul_zavihek': modul_zavihek,
                }
            )


        ''' Posodobitev opravila tako, da se pove na katerih elementih
        stavbe se opravilo izvaja. Pomembno za elektronsko servisno
        knjigo. '''

        if opravilo_element_update_form.is_valid():
            element = opravilo_element_update_form.cleaned_data['element']

            opravilo_object.element = element
            opravilo_object.save()

        else:
            return render(request, self.template_name, {
                'opravilo_create_form': opravilo_create_form,
                'element_izbira_form': element_izbira_form,
                'opravilo_element_update_form': opravilo_element_update_form,
                'opravilo_pomanjkljivost_update_form': opravilo_pomanjkljivost_update_form,
                'modul_zavihek': modul_zavihek,
                }
            )


        ''' Posodobitev opravila tako, da mu dodeli pomanjkljivosti, 
        ki se odpravljajo v tem opravilu'''

        if opravilo_pomanjkljivost_update_form.is_valid():
            pomanjkljivost = opravilo_pomanjkljivost_update_form.cleaned_data['pomanjkljivost']

            opravilo_object.pomanjkljivost = pomanjkljivost
            opravilo_object.save()

        else:
            return render(request, self.template_name, {
                'opravilo_create_form': opravilo_create_form,
                'element_izbira_form': element_izbira_form,
                'opravilo_element_update_form': opravilo_element_update_form,
                'opravilo_pomanjkljivost_update_form': opravilo_pomanjkljivost_update_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk}))





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
            print(element_list)

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

        else:
            return render(request, self.template_name, {
                'vzorec_opravila_izbira_form': vzorec_opravila_izbira_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk}))


# view called with ajax to reload the month drop down list
def reload_controls_planiranje_skupina_planov_view(request):

    c = {}
    c.update(csrf(request))

    context = {}
    # get the object
    skupina_planov = request.POST['skupina_planov']
    print(skupina_planov)
    skupina_planov = SkupinaPlanov.objects.get(id=skupina_planov)
    print(skupina_planov)
    print(skupina_planov.plan_set.all())
    # podskupine glede na izbrano skupino
    plan_list = []
    for plan in skupina_planov.plan_set.all():
        plan_list.append(plan.id)

    # OUTPUT FILTER
    # Podskupine
    context['plan_to_display'] = plan_list
    print(plan_list)

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
    for planirano_opravilo in plan.planiranoopravilo_set.all():
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