# PYTHON ##############################################################


# DJANGO ##############################################################
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView
from django.utils import timezone


# INTERNO ##############################################################
# Zahtevek Osnova
from ..forms import ZahtevekCreateForm
from ..models import Zahtevek

# Zahtevek Izvedba Del
from ..forms import ZahtevekIzvedbaDelCreateForm, ZahtevekIzvedbaDelUpdateForm
from ..models import ZahtevekIzvedbaDela


# UVOŽENO ##############################################################

# Moduli
from eda5.moduli.models import Zavihek

# Delovni Nalogi
from eda5.delovninalogi.forms import VzorecOpravilaIzbiraForm
from eda5.delovninalogi.models import Opravilo, VzorecOpravila

# Planiranje
from eda5.planiranje.models import SkupinaPlanov, Plan, PlaniranoOpravilo


class ZahtevekIzvedbaDelCreateView(TemplateView):
    template_name = "zahtevki/zahtevek/create_izvedba_del.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ZahtevekIzvedbaDelCreateView, self).get_context_data(*args, **kwargs)
        context['zahtevek_splosno_form'] = ZahtevekCreateForm
        context['zahtevek_izvedba_del_form'] = ZahtevekIzvedbaDelCreateForm

        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_IZVEDBA_DEL_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *Args, **kwargs):

        zahtevek_splosno_form = ZahtevekCreateForm(request.POST or None)
        zahtevek_izvedba_del_form = ZahtevekIzvedbaDelCreateForm(request.POST or None)
        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_IZVEDBA_DEL_CREATE")

        if zahtevek_splosno_form.is_valid():
            oznaka = zahtevek_splosno_form.cleaned_data['oznaka']
            naziv = zahtevek_splosno_form.cleaned_data['naziv']
            rok_izvedbe = zahtevek_splosno_form.cleaned_data['rok_izvedbe']
            nosilec = zahtevek_splosno_form.cleaned_data['nosilec']

            zahtevek_splosno_data = Zahtevek.objects.create_zahtevek(
                oznaka=oznaka,
                vrsta=3,
                naziv=naziv,
                rok_izvedbe=rok_izvedbe,
                nosilec=nosilec,
                status=3,
            )
            zahtevek = Zahtevek.objects.get(id=zahtevek_splosno_data.pk)

        else:
            return render(request, self.template_name, {
                'zahtevek_splosno_form': zahtevek_splosno_form,
                'zahtevek_izvedba_del_form': zahtevek_izvedba_del_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        if zahtevek_izvedba_del_form.is_valid():

            is_zakonska_obveza = zahtevek_izvedba_del_form.cleaned_data['is_zakonska_obveza']

            ZahtevekIzvedbaDela.objects.create_zahtevek_sestanek(
                zahtevek=zahtevek,
                is_zakonska_obveza=is_zakonska_obveza,
            )
        else:
            return render(request, self.template_name, {
                'zahtevek_splosno_form': zahtevek_splosno_form,
                'zahtevek_izvedba_del_form': zahtevek_izvedba_del_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk}))


class PodzahtevekIzvedbaDelCreateView(UpdateView):
    model = Zahtevek
    fields = ('id', )
    template_name = "zahtevki/zahtevek/create_izvedba_del.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PodzahtevekIzvedbaDelCreateView, self).get_context_data(*args, **kwargs)
        context['zahtevek_splosno_form'] = ZahtevekCreateForm
        context['zahtevek_izvedba_del_form'] = ZahtevekIzvedbaDelCreateForm

        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_IZVEDBA_DEL_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *Args, **kwargs):

        zahtevek_parent = Zahtevek.objects.get(id=self.get_object().id)

        zahtevek_splosno_form = ZahtevekCreateForm(request.POST or None)
        zahtevek_izvedba_del_form = ZahtevekIzvedbaDelCreateForm(request.POST or None)
        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_IZVEDBA_DEL_CREATE")

        if zahtevek_splosno_form.is_valid():
            oznaka = zahtevek_splosno_form.cleaned_data['oznaka']
            naziv = zahtevek_splosno_form.cleaned_data['naziv']
            rok_izvedbe = zahtevek_splosno_form.cleaned_data['rok_izvedbe']
            nosilec = zahtevek_splosno_form.cleaned_data['nosilec']

            zahtevek_splosno_data = Zahtevek.objects.create_zahtevek(
                oznaka=oznaka,
                vrsta=3,
                naziv=naziv,
                rok_izvedbe=rok_izvedbe,
                nosilec=nosilec,
                status=3,
                zahtevek_parent=zahtevek_parent
            )
            zahtevek = Zahtevek.objects.get(id=zahtevek_splosno_data.pk)

        else:
            return render(request, self.template_name, {
                'zahtevek_splosno_form': zahtevek_splosno_form,
                'zahtevek_izvedba_del_form': zahtevek_izvedba_del_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        if zahtevek_izvedba_del_form.is_valid():

            is_zakonska_obveza = zahtevek_izvedba_del_form.cleaned_data['is_zakonska_obveza']

            ZahtevekIzvedbaDela.objects.create_zahtevek_sestanek(
                zahtevek=zahtevek,
                is_zakonska_obveza=is_zakonska_obveza,
            )
        else:
            return render(request, self.template_name, {
                'zahtevek_splosno_form': zahtevek_splosno_form,
                'zahtevek_izvedba_del_form': zahtevek_izvedba_del_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk}))


class ZahtevekUpdateIzvedbaView(UpdateView):
    model = ZahtevekIzvedbaDela
    form_class = ZahtevekIzvedbaDelUpdateForm
    template_name = "zahtevki/zahtevek/update_zahtevek_izvedba.html"


class OpraviloCreateFromVzorecView(UpdateView):
    model = Zahtevek
    template_name = "delovninalogi/opravilo/create_from_vzorec_opravila.html"
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):
        context = super(OpraviloCreateFromVzorecView, self).get_context_data(*args, **kwargs)

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