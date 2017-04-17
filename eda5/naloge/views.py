# Splošno Django
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView

# Mixins
from braces.views import LoginRequiredMixin

# Models
from .models import Naloga
from eda5.moduli.models import Zavihek
from eda5.sestanki.models import Sestanek, Sklep
from eda5.zahtevki.models import Zahtevek

# Forms
from . import forms
from eda5.deli.forms import projektnomesto_forms



''' Izdelava naloge'''
class NalogaCreateView(LoginRequiredMixin, CreateView):
    model = Naloga
    template_name = "naloge/naloga/create/create.html"
    form_class = forms.NalogaCreateForm

    def get_context_data(self, *args, **kwargs):
        context = super(NalogaCreateView, self).get_context_data(*args, **kwargs)
        # pridobimo instanco izbranega zavihka
        modul_zavihek = Zavihek.objects.get(oznaka="naloga_create")
        context['modul_zavihek'] = modul_zavihek
        # vrnemo context
        return context


class NalogaListView(LoginRequiredMixin, ListView):

    model = Naloga
    template_name = "naloge/naloga/list/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NalogaListView, self).get_context_data(*args, **kwargs)

        # pridobimo instanco izbranega zavihka
        modul_zavihek = Zavihek.objects.get(oznaka="naloga_list")
        context['modul_zavihek'] = modul_zavihek

        # neobdelane pomanjkljivosti, ki niso še del nobenega zahtevka
        naloge_nelikvidirane = Naloga.objects.filter(zahtevek__isnull=True)
        context['naloge_nelikvidirane'] = naloge_nelikvidirane

        # seznam pomanjkljivosti, ki se že rešujejo (so del zahtevka, niso zaključene)
        naloge_vresevanju = Naloga.objects.filter(zahtevek__isnull=False).exclude(status=4).exclude(status=5)
        context['naloge_vresevanju'] = naloge_vresevanju

        # rešene pomanjkljivosti
        naloge_zakljucene = Naloga.objects.filter(zahtevek__isnull=False, status=4)
        context['naloge_zakljucene'] = naloge_zakljucene


        # vrnemo context
        return context


class NalogaDetailView(LoginRequiredMixin, DetailView):
    model = Naloga
    template_name = "naloge/naloga/detail/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NalogaDetailView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="naloga_detail")
        context['modul_zavihek'] = modul_zavihek

        return context


''' Izdelava pomanjkljivosti preko zahtevka'''
class NalogaCreateFromZahtevekView(LoginRequiredMixin, UpdateView):

    model = Zahtevek
    template_name = 'naloge/naloga/create/create_from_zahtevek.html'
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):
        context = super(NalogaCreateFromZahtevekView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="naloga_detail")
        context['modul_zavihek'] = modul_zavihek

        # pomanjkljivost
        context['naloga_create_from_zahtevek_form'] = forms.NalogaCreateFromZahtevekForm

        # vrnemo narejene podatke
        return context


    def post(self, request, *args, **kwargs):

        ###########################################################################
        # FORMS
        ###########################################################################

        naloga_create_from_zahtevek_form = forms.NalogaCreateFromZahtevekForm(request.POST or None)

        ''' Na začetku so vsi formi napčni neustrezni-
        neizbrani'''

        naloga_create_from_zahtevek_form_is_valid = False

        ###########################################################################
        # PRIDOBIMO PODATKE
        ###########################################################################

        ''' Pridobimo instanco zahtevka kjer se pomanjkljivost dodaja '''
        zahtevek = Zahtevek.objects.get(id=self.get_object().id)

        ''' Pridobimo instanco Zavihka '''
        modul_zavihek = Zavihek.objects.get(oznaka="pomanjkljivost_detail")

        ''' Izdelamo pomanjkljivost iz zahtevka '''

        if naloga_create_from_zahtevek_form.is_valid():
            oznaka = naloga_create_from_zahtevek_form.cleaned_data['oznaka']
            naziv = naloga_create_from_zahtevek_form.cleaned_data['naziv']
            opis = naloga_create_from_zahtevek_form.cleaned_data['opis']
            rok_izvedbe = naloga_create_from_zahtevek_form.cleaned_data['rok_izvedbe']
            prioriteta = naloga_create_from_zahtevek_form.cleaned_data['prioriteta']
            nosilec = naloga_create_from_zahtevek_form.cleaned_data['nosilec']
            naloga_create_from_zahtevek_form_is_valid = True

        # če so vsi podatki pravilno izpolnjeni izvrši spodaj navedene ukaze
        if naloga_create_from_zahtevek_form_is_valid == True:

            ###########################################################################
            # UKAZI
            ###########################################################################

            # izdelamo

            naloga = Naloga.objects.create_naloga(
                oznaka=oznaka,
                naziv=naziv,
                opis=opis,
                rok_izvedbe=rok_izvedbe,
                prioriteta=prioriteta,
                nosilec=nosilec,
                zahtevek=zahtevek,
            )

            # po končanem vnosu se izvede preusmeritev

            return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk}))

        else:
            return render(request, self.template_name, {
                'naloga_create_from_zahtevek_form': naloga_create_from_zahtevek_form,
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

class NalogaIzbiraFromZahtevek(LoginRequiredMixin, UpdateView):
    model = Zahtevek
    template_name = "naloge/naloga/update/naloga_izbira_from_zahtevek.html"
    fields = ('id', )
    # additional parameters
    zahtevek_id = None


    def get_context_data(self, *args, **kwargs):
        context = super(NalogaIzbiraFromZahtevek, self).get_context_data(*args, **kwargs)

        # zahtevek
        context['naloga_izbira_form'] = forms.NalogaIzbiraFrom

        modul_zavihek = Zavihek.objects.get(oznaka="naloga_detail")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):


        ###########################################################################
        # FORMS
        ###########################################################################

        naloga_izbira_form = forms.NalogaIzbiraFrom(request.POST or None)

        naloga_izbira_form_is_valid = False


        ###########################################################################
        # PRIDOBIMO PODATKE
        ###########################################################################

        ''' Pridobimo instanco zahtevka kjer se bo pomanjkljivost 
        nahajala '''

        zahtevek = Zahtevek.objects.get(id=self.get_object().id)

        ''' Pridobimo instanco pomanjkljivosti, ki jo želimo 
        dodati pod zahtevek '''

        # ko je pomanjkljivost izbrana
        if naloga_izbira_form.is_valid():
            # pridobimo instanco izbrane pomanjkljivosti
            naloga = naloga_izbira_form.cleaned_data['naloga']
            naloga_izbira_form_is_valid = True

        # če so vsi podatki pravilno izpolnjeni izvrši spodaj navedene ukaze
        if naloga_izbira_form_is_valid == True:

            ###########################################################################
            # UKAZI
            ###########################################################################

            # pomanjkljivosti dodelimo relacijo na izbrani zahtevek
            naloga.zahtevek = zahtevek
            naloga.save()

            return HttpResponseRedirect(reverse(
                'moduli:zahtevki:zahtevek_detail', 
                kwargs={
                    'pk': zahtevek.pk, 
                }))


''' Izdelava pomanjkljivosti preko zahtevka'''
class NalogaCreateFromSestanekView(LoginRequiredMixin, UpdateView):

    model = Sklep
    template_name = 'naloge/naloga/create/create_from_zahtevek.html'
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):
        context = super(NalogaCreateFromSestanekView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="naloga_detail")
        context['modul_zavihek'] = modul_zavihek

        # pomanjkljivost
        context['naloga_create_from_zahtevek_form'] = forms.NalogaCreateFromZahtevekForm

        # vrnemo narejene podatke
        return context


    def post(self, request, *args, **kwargs):

        ###########################################################################
        # FORMS
        ###########################################################################

        naloga_create_from_zahtevek_form = forms.NalogaCreateFromZahtevekForm(request.POST or None)

        ''' Na začetku so vsi formi napčni neustrezni-
        neizbrani'''

        naloga_create_from_zahtevek_form_is_valid = False

        ###########################################################################
        # PRIDOBIMO PODATKE
        ###########################################################################

        ''' Pridobimo instanco zahtevka kjer se pomanjkljivost dodaja '''
        sestanek = Sestanek.objects.get(id=self.get_object().id)

        ''' Pridobimo instanco Zavihka '''
        modul_zavihek = Zavihek.objects.get(oznaka="pomanjkljivost_detail")

        ''' Izdelamo pomanjkljivost iz zahtevka '''

        if naloga_create_from_zahtevek_form.is_valid():
            oznaka = naloga_create_from_zahtevek_form.cleaned_data['oznaka']
            naziv = naloga_create_from_zahtevek_form.cleaned_data['naziv']
            opis = naloga_create_from_zahtevek_form.cleaned_data['opis']
            rok_izvedbe = naloga_create_from_zahtevek_form.cleaned_data['rok_izvedbe']
            prioriteta = naloga_create_from_zahtevek_form.cleaned_data['prioriteta']
            nosilec = naloga_create_from_zahtevek_form.cleaned_data['nosilec']
            sklep_sestanka = naloga_create_from_zahtevek_form.cleaned_data['sklep_sestanka']
            naloga_create_from_zahtevek_form_is_valid = True

        # če so vsi podatki pravilno izpolnjeni izvrši spodaj navedene ukaze
        if naloga_create_from_zahtevek_form_is_valid == True:

            ###########################################################################
            # UKAZI
            ###########################################################################

            # izdelamo

            naloga = Naloga.objects.create_naloga(
                oznaka=oznaka,
                naziv=naziv,
                opis=opis,
                rok_izvedbe=rok_izvedbe,
                prioriteta=prioriteta,
                nosilec=nosilec,
                sklep_sestanka=sklep_sestanka,
                zahtevek=sestanek.zahtevek,
            )

            # po končanem vnosu se izvede preusmeritev

            return HttpResponseRedirect(reverse('moduli:sestanki:sestanek_detail', kwargs={'pk': sestanek.pk}))

        else:
            return render(request, self.template_name, {
                'naloga_create_from_zahtevek_form': naloga_create_from_zahtevek_form,
                'modul_zavihek': modul_zavihek,
                }
            )



class NalogaUpdateView(UpdateView):
    model = Naloga
    form_class = forms.NalogaUpdateForm
    template_name = "naloge/naloga/update/update.html"


    def get_context_data(self, *args, **kwargs):
        context = super(NalogaUpdateView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="naloga_detail")
        context['modul_zavihek'] = modul_zavihek

        return context