from itertools import chain
from operator import itemgetter

# Splošno Django
from django.core.urlresolvers import reverse
from django.db.models import F, Value, CharField
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView

# Mixins
from braces.views import LoginRequiredMixin

# Models
from .models import Pomanjkljivost
from eda5.delovninalogi.models import DelovniNalog
from eda5.dogodki.models import Dogodek
from eda5.moduli.models import Zavihek
from eda5.zahtevki.models import Zahtevek
from eda5.zaznamki.models import Zaznamek

# Forms
from .forms import PomanjkljivostCreateForm, PomanjkljivostCreateFromZahtevekForm, PomanjkljivostLikvidirajPodZahtevek
from .forms import PomanjkljivostIzbiraFrom, PomanjkljivostElementUpdateForm, PomanjkljivostUpdateForm
from eda5.deli.forms import projektnomesto_forms




class PomanjkljivostiHomeView(TemplateView):
    template_name = "pomanjkljivosti/home.html"


''' Izdelava pomanjkljivosti preko vmesnika'''
class PomanjkljivostCreateView(LoginRequiredMixin, CreateView):
    model = Pomanjkljivost
    template_name = "pomanjkljivosti/pomanjkljivost/create/create.html"
    form_class = PomanjkljivostCreateForm

    def get_context_data(self, *args, **kwargs):
        context = super(PomanjkljivostCreateView, self).get_context_data(*args, **kwargs)
        # pridobimo instanco izbranega zavihka
        modul_zavihek = Zavihek.objects.get(oznaka="pomanjkljivost_create")
        context['modul_zavihek'] = modul_zavihek
        # vrnemo context
        return context


class PomanjkljivostListView(LoginRequiredMixin, ListView):

    model = Pomanjkljivost
    template_name = "pomanjkljivosti/pomanjkljivost/list/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PomanjkljivostListView, self).get_context_data(*args, **kwargs)

        # pridobimo instanco izbranega zavihka
        modul_zavihek = Zavihek.objects.get(oznaka="pomanjkljivost_list")
        context['modul_zavihek'] = modul_zavihek

        # neobdelane pomanjkljivosti, ki niso še del nobenega zahtevka
        pomanjkljivosti_nelikvidirane = Pomanjkljivost.objects.filter(zahtevek__isnull=True)
        context['pomanjkljivosti_nelikvidirane'] = pomanjkljivosti_nelikvidirane

        # seznam pomanjkljivosti, ki se že rešujejo (so del zahtevka, niso zaključene)
        pomanjkljivosti_vresevanju = Pomanjkljivost.objects.filter(zahtevek__isnull=False).exclude(status=4).exclude(status=5)
        context['pomanjkljivosti_vresevanju'] = pomanjkljivosti_vresevanju

        # rešene pomanjkljivosti
        pomanjkljivosti_zakljucene = Pomanjkljivost.objects.filter(zahtevek__isnull=False, status=4)
        context['pomanjkljivosti_zakljucene'] = pomanjkljivosti_zakljucene


        # vrnemo context
        return context

    # tega sedaj ne potrebujem !!!!!!!! podatki se uporabijo iz contexta
    def get_queryset(self):
        queryset = super(PomanjkljivostListView, self).get_queryset()
        # prikažemo samo ne-rešene pomanjkljivosti
        queryset = self.model.objects.filter(zahtevek__isnull=True)
        # vrnemo spremenjene podatke
        return queryset


class PomanjkljivostDetailView(LoginRequiredMixin, DetailView):
    model = Pomanjkljivost
    template_name = "pomanjkljivosti/pomanjkljivost/detail/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PomanjkljivostDetailView, self).get_context_data(*args, **kwargs)

        pomanjkljivost = Pomanjkljivost.objects.get(id=self.get_object().pk)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="pomanjkljivost_detail")
        context['modul_zavihek'] = modul_zavihek

        # Zaznamek
        zaznamek_list= Zaznamek.objects.filter(pomanjkljivost=self.object.id).order_by('-datum', '-ura')
        context['zaznamek_list'] = zaznamek_list

        # Procesna dejanja
        delovninalogi = DelovniNalog.objects.filter(opravilo__pomanjkljivost=pomanjkljivost)
        delovninalogi = delovninalogi.annotate(pd_datum=F('datum_stop'))
        delovninalogi = delovninalogi.annotate(pd_cas=Value('/', CharField()))
        delovninalogi = delovninalogi.annotate(pd_vrsta=Value('opravilo', CharField()))
        delovninalogi = delovninalogi.annotate(pd_vsebina=F('opravilo__naziv'))
        delovninalogi = delovninalogi.annotate(pd_oznaka=F('oznaka'))
        delovninalogi = delovninalogi.annotate(pd_dn_zaznamki=F('zaznamek'))
        delovninalogi = delovninalogi.values('pd_datum', 'pd_cas', 'pd_vrsta','pd_vsebina', 'pd_oznaka', 'pk', 'pd_dn_zaznamki')


        # Zaznamki, ki so del delovnih nalogov
        delovninalogi_pomanjkljivost = DelovniNalog.objects.filter(opravilo__pomanjkljivost=pomanjkljivost)
        zaznamki_dn_pomanjkljivost = Zaznamek.objects.filter(delovninalog__in=delovninalogi_pomanjkljivost)
        zaznamki_dn_pomanjkljivost = zaznamki_dn_pomanjkljivost.annotate(
            pd_datum=F('datum'),
            pd_cas=F('ura'),
            pd_vrsta=Value('zaznamek', CharField()),
            pd_vsebina=F('tekst'),
            pd_oznaka=F('pk'),
            pd_dn_zaznamki=Value('/', CharField()))

        # zaznamki = zaznamki.annotate(pd_vsebina=F('tekst'))
        zaznamki_dn_pomanjkljivost = zaznamki_dn_pomanjkljivost.values('pd_datum', 'pd_cas', 'pd_vrsta','pd_vsebina', 'pd_oznaka', 'pk', 'pd_dn_zaznamki')

        zaznamki = zaznamek_list
        zaznamki = zaznamki.annotate(
            pd_datum=F('datum'),
            pd_cas=F('ura'),
            pd_vrsta=Value('zaznamek', CharField()),
            pd_vsebina=F('tekst'),
            pd_oznaka=F('pk'),
            pd_dn_zaznamki=Value('/', CharField()))

        # zaznamki = zaznamki.annotate(pd_vsebina=F('tekst'))
        zaznamki = zaznamki.values('pd_datum', 'pd_cas', 'pd_vrsta','pd_vsebina', 'pd_oznaka', 'pk', 'pd_dn_zaznamki')

        dogodki = Dogodek.objects.filter(pomanjkljivost=pomanjkljivost)
        #dogodki = dogodki.annotate(pd_datum=F('datum_dogodka'))
        #dogodki = dogodki.annotate(pd_vsebina=F('opis_dogodka'))
        dogodki = dogodki.annotate(
            pd_datum=F('datum_dogodka'),
            pd_cas=Value('/', CharField()),
            pd_vrsta=Value('dogodek', CharField()),
            pd_vsebina=F('opis_dogodka'),
            pd_oznaka=F('pk'),
            pd_dn_zaznamki=Value('/', CharField()))
        dogodki = dogodki.values('pd_datum', 'pd_cas', 'pd_vrsta','pd_vsebina', 'pd_oznaka', 'pk', 'pd_dn_zaznamki')

        # https://chriskief.com/2015/01/12/combine-2-django-querysets-from-different-models/
        # https://stackoverflow.com/questions/34042961/when-i-tried-to-sort-a-list-i-got-an-error-dict-object-has-no-attribute
        procesna_dejanja = sorted(
            chain(delovninalogi, dogodki, zaznamki, zaznamki_dn_pomanjkljivost),
            key=itemgetter('pd_datum'),
            reverse=False)

        context['procesna_dejanja'] = procesna_dejanja



        return context


''' Izdelava pomanjkljivosti preko zahtevka'''
class PomanjkljivostCreateFromZahtevekView(LoginRequiredMixin, UpdateView):

    model = Zahtevek
    template_name = 'pomanjkljivosti/pomanjkljivost/create/create_from_zahtevek.html'
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):
        context = super(PomanjkljivostCreateFromZahtevekView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="pomanjkljivost_detail")
        context['modul_zavihek'] = modul_zavihek

        # deli
        context['element_izbira_form'] = projektnomesto_forms.ElementIzbiraForm

        # pomanjkljivost
        context['pomanjkljivost_create_from_zahtevek_form'] = PomanjkljivostCreateFromZahtevekForm
        context['pomanjkljivost_element_update_form'] = PomanjkljivostElementUpdateForm

        # vrnemo narejene podatke
        return context


    def post(self, request, *args, **kwargs):

        ###########################################################################
        # FORMS
        ###########################################################################

        pomanjkljivost_create_from_zahtevek_form = PomanjkljivostCreateFromZahtevekForm(request.POST or None)
        pomanjkljivost_element_update_form = PomanjkljivostElementUpdateForm(request.POST or None)

        ''' Na začetku so vsi formi napčni neustrezni-
        neizbrani'''

        pomanjkljivost_create_from_zahtevek_form_is_valid = False
        pomanjkljivost_element_update_form_is_valid = False

        ###########################################################################
        # PRIDOBIMO PODATKE
        ###########################################################################

        ''' Pridobimo instanco zahtevka kjer se pomanjkljivost dodaja '''
        zahtevek = Zahtevek.objects.get(id=self.get_object().id)

        ''' Pridobimo instanco Zavihka '''
        modul_zavihek = Zavihek.objects.get(oznaka="pomanjkljivost_detail")

        ''' Izdelamo pomanjkljivost iz zahtevka '''

        if pomanjkljivost_create_from_zahtevek_form.is_valid():
            oznaka = pomanjkljivost_create_from_zahtevek_form.cleaned_data['oznaka']
            naziv = pomanjkljivost_create_from_zahtevek_form.cleaned_data['naziv']
            opis = pomanjkljivost_create_from_zahtevek_form.cleaned_data['opis']
            prijavil_text = pomanjkljivost_create_from_zahtevek_form.cleaned_data['prijavil_text']
            ugotovljeno_dne = pomanjkljivost_create_from_zahtevek_form.cleaned_data['ugotovljeno_dne']
            prioriteta = pomanjkljivost_create_from_zahtevek_form.cleaned_data['prioriteta']
            pomanjkljivost_create_from_zahtevek_form_is_valid = True


        ''' Pridobimo še elemente, ki so predmet pomanjkljivosti '''

        if pomanjkljivost_element_update_form.is_valid():
            element = pomanjkljivost_element_update_form.cleaned_data['element']
            pomanjkljivost_element_update_form_is_valid = True


        # če so vsi podatki pravilno izpolnjeni izvrši spodaj navedene ukaze
        if pomanjkljivost_create_from_zahtevek_form_is_valid == True and pomanjkljivost_element_update_form_is_valid == True:

            ###########################################################################
            # UKAZI
            ###########################################################################

            # izdelamo pomanjkljivost

            pomanjkljivost_data = Pomanjkljivost.objects.create_pomanjkljivost(
                oznaka=oznaka,
                naziv=naziv,
                opis=opis,
                prijavil_text=prijavil_text,
                ugotovljeno_dne=ugotovljeno_dne,
                prioriteta=prioriteta,
                # element=element, element se doda kasnje
                zahtevek=zahtevek,
            )

            # pridobimo instanco pomanjkljivosti za nadaljno spreminjanje
            pomanjkljivost_object = Pomanjkljivost.objects.get(id=pomanjkljivost_data.pk)

            # pomanjkljivosti dodamo izbrane elemente
            pomanjkljivost_object.element = element
            pomanjkljivost_object.save()

            # po končanem vnosu se izvede preusmeritev

            return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk}))

        else:
            return render(request, self.template_name, {
                'pomanjkljivost_create_from_zahtevek_form': pomanjkljivost_create_from_zahtevek_form,
                'pomanjkljivost_element_update_form': pomanjkljivost_element_update_form,
                'modul_zavihek': modul_zavihek,
                }
            )







#################################################################################
# LIKVIDACIJA POMANJKLJIVOSTI POD ZAHTEVKE
#################################################################################

"""
Likvidacija se izvrši preko dveh VIEWs. V privem izberemo pomanjkljivosti
in ji dodelimo zahevek. V drugem pa pomanjkljivosti dodamo še ostale
vrednosti

Relacija:
- PomanjkljivostIzbiraFromZahtevek
- PomanjkljivostLikvidirajPodZahtevekView

"""

class PomanjkljivostIzbiraFromZahtevek(LoginRequiredMixin, UpdateView):
    model = Zahtevek
    template_name = "pomanjkljivosti/pomanjkljivost/update/pomanjkljivost_izbira_from_zahtevek.html"
    fields = ('id', )
    # additional parameters
    zahtevek_id = None


    def get_context_data(self, *args, **kwargs):
        context = super(PomanjkljivostIzbiraFromZahtevek, self).get_context_data(*args, **kwargs)

        # zahtevek
        context['pomanjkljivost_izbira_form'] = PomanjkljivostIzbiraFrom

        modul_zavihek = Zavihek.objects.get(oznaka="pomanjkljivost_detail")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):


        ###########################################################################
        # FORMS
        ###########################################################################

        pomanjkljivost_izbira_form = PomanjkljivostIzbiraFrom(request.POST or None)

        pomanjkljivost_izbira_form_is_valid = False


        ###########################################################################
        # PRIDOBIMO PODATKE
        ###########################################################################

        ''' Pridobimo instanco zahtevka kjer se bo pomanjkljivost
        nahajala '''

        zahtevek = Zahtevek.objects.get(id=self.get_object().id)

        ''' Pridobimo instanco pomanjkljivosti, ki jo želimo
        dodati pod zahtevek '''

        # ko je pomanjkljivost izbrana
        if pomanjkljivost_izbira_form.is_valid():
            # pridobimo instanco izbrane pomanjkljivosti
            pomanjkljivost = pomanjkljivost_izbira_form.cleaned_data['pomanjkljivost']
            pomanjkljivost_izbira_form_is_valid = True

        # če so vsi podatki pravilno izpolnjeni izvrši spodaj navedene ukaze
        if pomanjkljivost_izbira_form_is_valid == True:

            ###########################################################################
            # UKAZI
            ###########################################################################

            # pomanjkljivosti dodelimo relacijo na izbrani zahtevek
            pomanjkljivost.zahtevek = zahtevek
            pomanjkljivost.save()

            return HttpResponseRedirect(reverse(
                'moduli:pomanjkljivosti:pomanjkljivost_likvidiraj_pod_zahtevek',
                kwargs={
                    'pk': pomanjkljivost.pk,
                }))


class PomanjkljivostLikvidirajPodZahtevekView(LoginRequiredMixin, UpdateView):

    model = Pomanjkljivost
    template_name = 'pomanjkljivosti/pomanjkljivost/update/likvidiraj_pod_zahtevek.html'
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):
        context = super(PomanjkljivostLikvidirajPodZahtevekView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="pomanjkljivost_detail")
        context['modul_zavihek'] = modul_zavihek

        # deli
        context['element_izbira_form'] = projektnomesto_forms.ElementIzbiraForm

        # pomanjkljivost
        context['pomanjkljivost_likvidiraj_pod_zahtevek_form'] = PomanjkljivostLikvidirajPodZahtevek
        context['pomanjkljivost_element_update_form'] = PomanjkljivostElementUpdateForm

        # vrnemo narejene podatke
        return context


    def post(self, request, *args, **kwargs):


        ###########################################################################
        # FORMS
        ###########################################################################

        pomanjkljivost_likvidiraj_pod_zahtevek_form = PomanjkljivostLikvidirajPodZahtevek(request.POST or None)
        pomanjkljivost_element_update_form = PomanjkljivostElementUpdateForm(request.POST or None)


        ###########################################################################
        # PRIDOBIMO PODATKE
        ###########################################################################


        ''' Pridobimo instanco pomanjkljivosti, ki jo likvidiramo '''

        pomanjkljivost_id = self.kwargs.get('pk', None)
        pomanjkljivost = Pomanjkljivost.objects.get(id=pomanjkljivost_id)

        ''' Pridobimo instanco Zavihka '''

        modul_zavihek = Zavihek.objects.get(oznaka="pomanjkljivost_detail")

        ''' Na začetku so vsi formi napčni neustrezni-
        neizbrani'''

        pomanjkljivost_likvidiraj_pod_zahtevek_form_is_valid = False
        pomanjkljivost_element_update_form_is_valid = False


        if pomanjkljivost_likvidiraj_pod_zahtevek_form.is_valid():
            # pridobimo izpolnjene podatke
            naziv = pomanjkljivost_likvidiraj_pod_zahtevek_form.cleaned_data['naziv']
            opis = pomanjkljivost_likvidiraj_pod_zahtevek_form.cleaned_data['opis']
            prioriteta = pomanjkljivost_likvidiraj_pod_zahtevek_form.cleaned_data['prioriteta']
            pomanjkljivost_likvidiraj_pod_zahtevek_form_is_valid = True

        ''' Pridobimo še elemente, ki so predmet pomanjkljivosti '''

        if pomanjkljivost_element_update_form.is_valid():
            element = pomanjkljivost_element_update_form.cleaned_data['element']
            pomanjkljivost_element_update_form_is_valid = True


        # če so vsi podatki pravilno izpolnjeni izvrši spodaj navedene ukaze
        if pomanjkljivost_likvidiraj_pod_zahtevek_form_is_valid == True and pomanjkljivost_element_update_form_is_valid == True:

            ###########################################################################
            # UKAZI
            ###########################################################################

            ''' relacijo z zahtevkom smo pomanjkljivosti dodelili že v
            PomanjkljivostIzbiraFromZahtevek '''

            # pomanjkljivosti dodelimo še ostale podatke
            pomanjkljivost.naziv = naziv
            pomanjkljivost.opis = opis
            pomanjkljivost.prioriteta = prioriteta

            # dodamo še izbrane elemente
            pomanjkljivost.element = element

            # spremembe prepišemo
            pomanjkljivost.save()

        # če podatki niso pravilno izpolnjeni izvrši naslednji ukaz
        else:
            return render(request, self.template_name, {
                'pomanjkljivost_likvidiraj_pod_zahtevek_form': pomanjkljivost_likvidiraj_pod_zahtevek_form,
                'pomanjkljivost_element_update_form': pomanjkljivost_element_update_form,
                'element_izbira_form': element_izbira_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        ''' po končanem vnosu se izvede preusmeritev '''

        return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': pomanjkljivost.zahtevek.pk}))



class PomanjkljivostUpdateView(UpdateView):
    model = Pomanjkljivost
    form_class = PomanjkljivostUpdateForm
    template_name = "pomanjkljivosti/pomanjkljivost/update/update.html"


    def get_context_data(self, *args, **kwargs):
        context = super(PomanjkljivostUpdateView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="pomanjkljivost_detail")
        context['modul_zavihek'] = modul_zavihek

        return context
