# PYTHON ##############################################################


# DJANGO ##############################################################
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, UpdateView


# INTERNO ##############################################################
# Zahtevek Osnova
from ..forms import ZahtevekUpdateForm, ZahtevekIzbiraForm
from ..models import Zahtevek


# UVOŽENO ##############################################################
# Arhiv
from eda5.arhiv.forms import ArhiviranjeZahtevekForm
from eda5.arhiv.models import Arhiviranje, ArhivMesto

# Deli
from eda5.deli.forms import ElementIzbiraForm
from eda5.deli.models import Skupina, Podskupina, DelStavbe, ProjektnoMesto 

# Delovni Nalogi
from eda5.delovninalogi.forms import OpraviloCreateForm, OpraviloElementUpdateForm
from eda5.delovninalogi.models import Opravilo

# Dogodki
from eda5.dogodki.forms import DogodekCreateForm
from eda5.dogodki.forms import DogodekUpdateForm
from eda5.dogodki.models import Dogodek

# Kljuci
from eda5.kljuci.models import PredajaKljuca
from eda5.kljuci.forms import PredajaKljucaCreateForm

# Moduli
from eda5.moduli.models import Zavihek

# Partnerji
from eda5.partnerji.models import Oseba

# Zaznamki
from eda5.zaznamki.forms import ZaznamekForm
from eda5.zaznamki.models import Zaznamek


class ZahtevekListView(ListView):
    model = Zahtevek
    template_name = "zahtevki/zahtevek/list/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ZahtevekListView, self).get_context_data(*args, **kwargs)

        # content
        context['zahtevki_vresevanju_list'] = self.model.objects.zahtevki_vresevanju()
        context['zahtevki_zakljuceni_list'] = self.model.objects.zahtevki_zakljuceni()

        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_LIST")
        context['modul_zavihek'] = modul_zavihek

        return context


class ZahtevekCreateIzbiraView(TemplateView):
    model = Zahtevek
    template_name = "zahtevki/zahtevek/create_izbira.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ZahtevekCreateIzbiraView, self).get_context_data(*args, **kwargs)

        # zahtevek
        context['zahtevek_izbira_form'] = ZahtevekIzbiraForm

        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        zahtevek_izbira_form = ZahtevekIzbiraForm(request.POST or None)

        if zahtevek_izbira_form.is_valid():

            vrsta_zahtevka = zahtevek_izbira_form.cleaned_data['vrsta_zahtevka']

            if vrsta_zahtevka == '1':
                return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_create_skodni_dogodek'))
            if vrsta_zahtevka == '2':
                return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_create_sestanek'))
            if vrsta_zahtevka == '3':
                return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_create_izvedba_del'))
            if vrsta_zahtevka == '4':
                return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_create_predaja_lastnine'))
            if vrsta_zahtevka == '5':
                return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_create_analiza'))
            if vrsta_zahtevka == '6':
                return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_create_povprasevanje'))
            if vrsta_zahtevka == '7':
                return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_create_reklamacija'))


class ZahtevekUpdateView(UpdateView):
    model = Zahtevek
    form_class = ZahtevekUpdateForm
    template_name = "zahtevki/zahtevek/update_zahtevek_main.html"


class DogodekUpdateView(UpdateView):
    model = Dogodek
    form_class = DogodekUpdateForm
    template_name = "dogodki/dogodek/update_dogodek.html"


class ZahtevekDetailView(DetailView):
    model = Zahtevek
    template_name = "zahtevki/zahtevek/detail/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ZahtevekDetailView, self).get_context_data(*args, **kwargs)

        # arhiv_mesto
        context['arhiv_mesto'] = ArhivMesto.objects.get(oznaka=self.object.oznaka)

        # dogodek
        context['dogodek_create_form'] = DogodekCreateForm

        # kljuci
        context['predajakljuca_create_form'] = PredajaKljucaCreateForm
        context['predaja_kljuca_list'] = PredajaKljuca.objects.filter(
            predaja_lastnine=self.object.predajalastnine.id)

        # opravilo
        context['opravilo_form'] = OpraviloCreateForm
        context['opravilo_list'] = Opravilo.objects.filter(zahtevek=self.object.id)

        # zaznamek
        context['zaznamek_form'] = ZaznamekForm
        context['zaznamek_list'] = Zaznamek.objects.filter(zahtevek=self.object.id)

        # zahtevek - child
        context['zahtevek_create_form'] = ZahtevekIzbiraForm
        context['zahtevek_child_list'] = Zahtevek.objects.filter(zahtevek_parent=self.object.id)

        context['arhiviranje_form'] = ArhiviranjeZahtevekForm

        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):
        # opravilo_form = OpraviloCreateForm(request.POST or None)
        arhiviranje_form = ArhiviranjeZahtevekForm(request.POST or None)
        dogodek_create_form = DogodekCreateForm(request.POST or None)
        zaznamek_form = ZaznamekForm(request.POST or None)
        zahtevek_create_form = ZahtevekIzbiraForm(request.POST or None)


        zahtevek = Zahtevek.objects.get(id=self.get_object().id)

        opravilo_list = Opravilo.objects.filter(zahtevek=zahtevek)
        zaznamek_list = Zaznamek.objects.filter(zahtevek=zahtevek)
        zahtevek_child_list = Zahtevek.objects.filter(zahtevek_parent=zahtevek)

        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_DETAIL")

        if zaznamek_form.is_valid():
            tekst = zaznamek_form.cleaned_data['tekst']
            datum = zaznamek_form.cleaned_data['datum']
            ura = zaznamek_form.cleaned_data['ura']

            Zaznamek.objects.create_zaznamek(tekst=tekst,
                                             datum=datum,
                                             ura=ura,
                                             zahtevek=zahtevek,
                                             )

            return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk}))

        if zahtevek_create_form.is_valid():

            vrsta_zahtevka = zahtevek_create_form.cleaned_data['vrsta_zahtevka']

            if vrsta_zahtevka == '1':
                return HttpResponseRedirect(reverse('moduli:zahtevki:podzahtevek_create_skodni_dogodek',
                                                    kwargs={'pk': zahtevek.pk}))
            if vrsta_zahtevka == '2':
                return HttpResponseRedirect(reverse('moduli:zahtevki:podzahtevek_create_sestanek',
                                                    kwargs={'pk': zahtevek.pk}))
            if vrsta_zahtevka == '3':
                return HttpResponseRedirect(reverse('moduli:zahtevki:podzahtevek_create_izvedba_del',
                                                    kwargs={'pk': zahtevek.pk}))
            if vrsta_zahtevka == '4':
                return HttpResponseRedirect(reverse('moduli:zahtevki:podzahtevek_create_predaja_lastnine',
                                                    kwargs={'pk': zahtevek.pk}))
            if vrsta_zahtevka == '5':
                return HttpResponseRedirect(reverse('moduli:zahtevki:podzahtevek_create_analiza',
                                                    kwargs={'pk': zahtevek.pk}))
            if vrsta_zahtevka == '6':
                return HttpResponseRedirect(reverse('moduli:zahtevki:podzahtevek_create_povprasevanje',
                                                    kwargs={'pk': zahtevek.pk}))
            if vrsta_zahtevka == '7':
                return HttpResponseRedirect(reverse('moduli:zahtevki:podzahtevek_create_reklamacija',
                                                    kwargs={'pk': zahtevek.pk}))


        # ARHIVIRANJE

        if arhiviranje_form.is_valid():

            dokument = arhiviranje_form.cleaned_data['dokument']
            elektronski = arhiviranje_form.cleaned_data['elektronski']
            fizicni = arhiviranje_form.cleaned_data['fizicni']
            lokacija_hrambe = ArhivMesto.objects.get(oznaka=zahtevek.oznaka)

            # arhiviral
            user = request.user
            oseba = Oseba.objects.get(user=user)
            arhiviral = oseba

            Arhiviranje.objects.create_arhiviranje(
                zahtevek=zahtevek,
                dokument=dokument,
                arhiviral=arhiviral,
                elektronski=elektronski,
                fizicni=fizicni,
                lokacija_hrambe=lokacija_hrambe,
            )

            return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk}))

        # IF NOT VALID
        return render(request, self.template_name, {
            'object': zahtevek,
            # 'opravilo_form': opravilo_form,
            'opravilo_list': opravilo_list,
            'zaznamek_form': zaznamek_form,
            'zaznamek_list': zaznamek_list,
            'zahtevek_create_form': zahtevek_create_form,
            'zahtevek_child_list': zahtevek_child_list,
            'arhiviranje_form': arhiviranje_form,
            'modul_zavihek': modul_zavihek,
            }
        )


class OpraviloCreateView(UpdateView):
    model = Zahtevek
    template_name = "delovninalogi/opravilo/create_from_zahtevek.html"
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):
        context = super(OpraviloCreateView, self).get_context_data(*args, **kwargs)

        # opravilo
        context['opravilo_create_form'] = OpraviloCreateForm
        context['opravilo_element_update_form'] = OpraviloElementUpdateForm
        context['element_izbira_form'] = ElementIzbiraForm

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="OPRAVILO_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        # object
        zahtevek = Zahtevek.objects.get(id=self.get_object().id)

        # forms
        opravilo_create_form = OpraviloCreateForm(request.POST or None)
        opravilo_element_update_form = OpraviloElementUpdateForm(request.POST or None)
        element_izbira_form = ElementIzbiraForm(request.POST or None)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="OPRAVILO_CREATE")

        # izdelamo opravilo (!!!elemente opravilu dodamo kasneje)
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
                'opravilo_element_update_form': opravilo_element_update_form,
                'element_izbira_form': element_izbira_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        if opravilo_element_update_form.is_valid():
            element = opravilo_element_update_form.cleaned_data['element']

            opravilo_object.element = element
            opravilo_object.save()

        else:
            return render(request, self.template_name, {
                'opravilo_create_form': opravilo_create_form,
                'opravilo_element_update_form': opravilo_element_update_form,
                'element_izbira_form': element_izbira_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk}))


# view called with ajax to reload the month drop down list
def reload_controls_element_podskupina_view(request):

    c = {}
    c.update(csrf(request))

    context = {}
    # get the object
    skupina = request.POST['skupina']
    skupina = Skupina.objects.get(id=skupina)

    # podskupine glede na izbrano skupino
    podskupina_list = []
    for podskupina in skupina.podskupina_set.all():
        podskupina_list.append(podskupina.id)

    # OUTPUT FILTER
    # Podskupine
    context['podskupine_to_display'] = podskupina_list

    return JsonResponse(context)


# view called with ajax to reload the month drop down list
def reload_controls_element_del_stavbe_view(request):

    c = {}
    c.update(csrf(request))

    context = {}
    # get the object
    podskupina = request.POST['podskupina']
    podskupina = Podskupina.objects.get(id=podskupina)

    # deli stavbe glede na izbrano podskupino
    del_stavbe_list = []
    for del_stavbe in podskupina.delstavbe_set.all():
        del_stavbe_list.append(del_stavbe.id)

    # OUTPUT FILTER

    # DelStavbe
    context['del_stavbe_to_display'] = del_stavbe_list

    return JsonResponse(context)


# view called with ajax to reload the month drop down list
def reload_controls_element_element_view(request):

    c = {}
    c.update(csrf(request))

    context = {}
    # get the object
    del_stavbe = request.POST['del_stavbe']
    del_stavbe = DelStavbe.objects.get(id=del_stavbe)
    projektno_mesto_list = ProjektnoMesto.objects.filter(del_stavbe=del_stavbe)

    # deli stavbe glede na izbrano podskupino
    element_list = []
    for projektno_mesto in projektno_mesto_list:
        # obstaja samo en element v projektnem mestu. ostali niso aktivni
        element = projektno_mesto.element_set.all()[0]
        element_list.append(element.id)

    # OUTPUT FILTER

    # DelStavbe
    context['element_to_display'] = element_list

    return JsonResponse(context)
