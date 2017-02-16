# PYTHON ##############################################################
from datetime import datetime, timedelta
import os


# DJANGO ##############################################################
from django.conf import settings
from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
# from django.shortcuts import render
from django.utils import timezone
from django.views.generic import TemplateView, ListView, DetailView, UpdateView


from .mixins import MessagesActionMixin
from .forms import OpraviloUpdateForm, DelovniNalogVcakanjuModelForm, DelovniNalogVplanuModelForm,\
                   DelovniNalogVresevanjuModelForm, DeloCreateForm, DeloZacetoUpdateModelForm
from .models import Opravilo, DelovniNalog, Delo, VzorecOpravila

from eda5.arhiv.forms import ArhiviranjeDelovniNalogForm
from eda5.arhiv.models import Arhiviranje, ArhivMesto
from eda5.partnerji.models import Oseba
from eda5.skladisce.models import Dnevnik
from eda5.skladisce.forms import DnevnikDelovniNalogCreateForm
from eda5.zaznamki.forms import ZaznamekForm
from eda5.zaznamki.models import Zaznamek

from eda5.moduli.models import Zavihek


# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
class AppHomeView(TemplateView):
    template_name = "delovninalogi/home.html"


# OPRAVILO************************************************************************************************
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
class OpraviloListView(ListView):
    model = Opravilo
    template_name = "delovninalogi/opravilo/list.html"


# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
class OpraviloDetailView(DetailView):
    model = Opravilo
    template_name = "delovninalogi/opravilo/detail/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(OpraviloDetailView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="OPRAVILO_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context


class VzorecOpravilaDetailView(DetailView):
    model = VzorecOpravila
    template_name = "delovninalogi/vzorec_opravila/detail/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(VzorecOpravilaDetailView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="VZOREC_OPRAVILA_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context


# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
class OpraviloUpdateView(UpdateView):
    model = Opravilo
    form_class = OpraviloUpdateForm
    template_name = "delovninalogi/opravilo/update.html"


# DELOVNI NALOG*******************************************************************************************
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
class DelovniNalogList(ListView):
    model = DelovniNalog
    template_name = "delovninalogi/delovninalog/list/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DelovniNalogList, self).get_context_data(*args, **kwargs)

        # content
        context['dn_vcakanju_list'] = self.model.objects.dn_vcakanju()
        context['dn_vplanu_list'] = self.model.objects.dn_vplanu()
        context['dn_vresevanju_list'] = self.model.objects.dn_vresevanju()
        context['dn_zakljuceni_list'] = self.model.objects.dn_zakljuceni()

        modul_zavihek = Zavihek.objects.get(oznaka="DN_LIST")
        context['modul_zavihek'] = modul_zavihek

        return context


# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
class DelovniNalogDetailView(MessagesActionMixin, DetailView):
    model = DelovniNalog
    template_name = "delovninalogi/delovninalog/detail/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DelovniNalogDetailView, self).get_context_data(*args, **kwargs)

        # content
        context['odprta_dela'] = Delo.objects.odprta_dela()
        context['koncana_dela'] = Delo.objects.koncana_dela()

        # arhiv
        context['arhiviranje_form'] = ArhiviranjeDelovniNalogForm

        # delo
        context['delo_create_form'] = DeloCreateForm
        context['delo_update_form'] = DeloZacetoUpdateModelForm
        context['delo_list'] = Delo.objects.filter(delovninalog=self.object.id)
        context['delo_delavec_distinct_list'] = Delo.objects.filter(delovninalog=self.object.id).distinct('delavec')

        # skladisce
        context['material_form'] = DnevnikDelovniNalogCreateForm
        context['material_list'] = Dnevnik.objects.filter(delovninalog=self.object.id)

        # zaznamek
        context['zaznamek_form'] = ZaznamekForm
        context['zaznamek_list'] = Zaznamek.objects.filter(delovninalog=self.object.id)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="DN_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        # DELOVNI-NALOG s katerim imamo opravka
        # =================================================================================================
        delovninalog = DelovniNalog.objects.get(id=self.get_object().id)
        arhiviranje_form = ArhiviranjeDelovniNalogForm(request.POST or None)
        zaznamek_form = ZaznamekForm(request.POST or None)
        delo_create_form = DeloCreateForm(request.POST or None)
        delo_update_form = DeloZacetoUpdateModelForm(request.POST or None)
        dnevnik_delovninalog_form = DnevnikDelovniNalogCreateForm(request.POST or None)

        
        ''' Vnašanje zaznamkov v delovni nalog preko
        okna, ki se odpre nad obstoječim oknom (MODAL)'''

        if zaznamek_form.is_valid():

            # PODATKI ZA VNOS
            # ---------------------------------------------------------------------------------------------
            tekst = zaznamek_form.cleaned_data['tekst']
            datum = zaznamek_form.cleaned_data['datum']
            ura = zaznamek_form.cleaned_data['ura']

            # DODATNE VALIDACIJE
            # ---------------------------------------------------------------------------------------------
            

            ''' validacija_zaznamek_add_01
            če je delovni-nalog že zaključen novih zaznamkov ni 
            mogoče vnašati '''

            if delovninalog.status == 4:
                messages.error(request, "Delovni nalog je že zaključen! Novih zaznamkov ni mogoče vnašati.")
                return HttpResponseRedirect(reverse('moduli:delovninalogi:dn_detail', kwargs={'pk': delovninalog.pk}))

            else:

            # VNOS V BAZO
            # ---------------------------------------------------------------------------------------------
                Zaznamek.objects.create_zaznamek(tekst=tekst,
                                                 datum=datum,
                                                 ura=ura,
                                                 delovninalog=delovninalog,
                                                 )

                return HttpResponseRedirect(reverse('moduli:delovninalogi:dn_detail', kwargs={'pk': delovninalog.pk}))

            # POGOJI PREUSMERJANJA
            # ---------------------------------------------------------------------------------------------

        # VNOS NOVEGA DELA
        # =================================================================================================
        if delo_create_form.is_valid():

            # PODATKI ZA VNOS
            # ---------------------------------------------------------------------------------------------

            oznaka = delo_create_form.cleaned_data['oznaka']
            naziv = delo_create_form.cleaned_data['naziv']
            vrsta_dela = delo_create_form.cleaned_data['vrsta_dela']
            delavec = delo_create_form.cleaned_data['delavec']
            datum = delo_create_form.cleaned_data['datum']
            time_start = delo_create_form.cleaned_data['time_start']


            # DODATNE VALIDACIJE
            # ---------------------------------------------------------------------------------------------

            # validacija_01
            '''Delovnim nalogom "V ČAKANJU" ni mogoče dodajati del'''

            if delovninalog.status == 1:
                messages.error(request, 'Delovnim nalogom "V ČAKANJU" ni mogoče dodajati del. Poterbno je planirati \
                                 na povezavi DASHBOARD : Planiraj.')  # sporočilo uporabniku
                return HttpResponseRedirect(reverse('moduli:delovninalogi:dn_detail', kwargs={'pk': delovninalog.pk}))

            # validacija_02
            '''pred vnosom novega dela NOSILEC ali DELAVEC ne sme imeti odprtih del. Istočasno ni mogoče
            opravljati več del'''
            for delo in Delo.objects.filter(time_stop__isnull=True):
                if delo.delavec.id == delavec.id:
                    messages.error(request, "Končati je potrebno predhodno delo v delovnem nalogu z oznako '%s'"
                                   % (delo.delovninalog.oznaka))
                    return HttpResponseRedirect(reverse('moduli:delovninalogi:dn_detail', kwargs={'pk': delovninalog.pk}))

            # validacija_03
            '''če je delovni-nalog že zaključen novih del ni mogoče vnašati. V templates je gumb za nove vnose
            odstranjen.Ta validacija je samo za slučaj če bi se link do gumba ročno vnesel'''

            if delovninalog.status == 4:
                messages.error(request, "Delovni nalog je že zaključen! Novih del ni mogoče vnašati.")
                return HttpResponseRedirect(reverse('moduli:delovninalogi:dn_detail', kwargs={'pk': delovninalog.pk}))

            # VNOS V BAZO
            # ---------------------------------------------------------------------------------------------

            Delo.objects.create_delo(
                oznaka=oznaka,
                naziv=naziv,
                delavec=delavec,
                datum=datum,
                vrsta_dela=vrsta_dela,
                time_start=time_start,
                delovninalog=delovninalog,
            )

            messages.success(request, 'Novo delo je vneseno')

            return HttpResponseRedirect(reverse('moduli:delovninalogi:dn_detail', kwargs={'pk': delovninalog.pk}))


        if delo_update_form.is_valid():

            oznaka = delo_update_form.cleaned_data['time_stop']


        if arhiviranje_form.is_valid():

            dokument = arhiviranje_form.cleaned_data['dokument']
            elektronski = arhiviranje_form.cleaned_data['elektronski']
            fizicni = arhiviranje_form.cleaned_data['fizicni']
            lokacija_hrambe = ArhivMesto.objects.get(oznaka=delovninalog.opravilo.zahtevek.oznaka)

            # arhiviral
            user = request.user
            oseba = Oseba.objects.get(user=user)
            arhiviral = oseba

            Arhiviranje.objects.create_arhiviranje(
                delovninalog=delovninalog,
                dokument=dokument,
                arhiviral=arhiviral,
                elektronski=elektronski,
                fizicni=fizicni,
                lokacija_hrambe=lokacija_hrambe,
            )

            return HttpResponseRedirect(reverse('moduli:delovninalogi:dn_detail', kwargs={'pk': delovninalog.pk}))

        if dnevnik_delovninalog_form.is_valid():

            artikel = dnevnik_delovninalog_form.cleaned_data['artikel']
            likvidiral = dnevnik_delovninalog_form.cleaned_data['likvidiral']
            kom = dnevnik_delovninalog_form.cleaned_data['kom']

            Dnevnik.objects.create_dnevnik(
                delovninalog=delovninalog,
                artikel=artikel,
                likvidiral=likvidiral,
                kom=kom,
            )

            return HttpResponseRedirect(reverse('moduli:delovninalogi:dn_detail', kwargs={'pk': delovninalog.pk}))

        return HttpResponseRedirect(reverse('moduli:delovninalogi:dn_detail', kwargs={'pk': delovninalog.pk}))


# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
class DelovniNalogUpdateVcakanjuView(MessagesActionMixin, UpdateView):
    model = DelovniNalog
    form_class = DelovniNalogVcakanjuModelForm
    template_name = "delovninalogi/delovninalog/update_vcakanju.html"
    success_url = reverse_lazy('moduli:delovninalogi:dn_list')  # redirect na seznam delovnih nalogov

    success_msg = "Status Delovnega Naloga je spremenjen na 'V PLANU'"

    def get_context_data(self, *args, **kwargs):
        context = super(DelovniNalogUpdateVcakanjuView, self).get_context_data(*args, **kwargs)

        # Zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="DN_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context


# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
class DelovniNalogUpdateVplanuView(MessagesActionMixin, UpdateView):
    model = DelovniNalog
    form_class = DelovniNalogVplanuModelForm
    template_name = "delovninalogi/delovninalog/update_vplanu.html"

    success_msg = "Status Delovnega Naloga je spremenjen na 'V REŠEVANJU'"

    def get_context_data(self, *args, **kwargs):
        context = super(DelovniNalogUpdateVplanuView, self).get_context_data(*args, **kwargs)

        # Zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="DN_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context


# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
class DelovniNalogUpdateVresevanjuView(MessagesActionMixin, UpdateView):
    model = DelovniNalog
    form_class = DelovniNalogVresevanjuModelForm
    template_name = "delovninalogi/delovninalog/update_vresevanju.html"

    success_msg = "Status Delovnega Naloga je spremenjen na 'ZAKLJUČENO'. Potrjeni delovni nalogi\
                  iz strani nosilca bodo obarvani v zeleno."

    def get_context_data(self, *args, **kwargs):
        context = super(DelovniNalogUpdateVresevanjuView, self).get_context_data(*args, **kwargs)

        # Zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="DN_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context


    # DODATNE VALIDACIJE
    # ---------------------------------------------------------------------------------------------
    def form_valid(self, form):

        # validacija_01
        '''Delovnih nalogov z odprtimi deli ni mogoče zaključiti!'''

        delovninalog_id = self.kwargs['pk']

        dela = Delo.objects.filter(delovninalog=delovninalog_id, time_stop__isnull=True)
        if dela:
            messages.error(self.request, "Delovnega naloga z odprtimi deli ni mogoče zaključiti!")
            return HttpResponseRedirect(reverse('moduli:delovninalogi:dn_detail', kwargs={'pk': delovninalog_id}))

        return super(DelovniNalogUpdateVresevanjuView, self).form_valid(form)


# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# class DelovniNalogUpdateDokumentFormView(MessagesActionMixin, UpdateView):
#     model = DelovniNalog
#     form_class = DelovniNalogAddDokumentForm
#     template_name = "delovninalogi/delovninalog/update_dokument.html"

#     success_msg = "Dokumentacija je bila uspešno spremenjena."


# DELO****************************************************************************************************
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
class DeloZacetoUpdateView(MessagesActionMixin, UpdateView):
    model = Delo
    form_class = DeloZacetoUpdateModelForm
    template_name = "delovninalogi/delo/update_zaceto.html"

    success_msg = "Delo je uspešno končano."

    def get_context_data(self, *args, **kwargs):
        context = super(DeloZacetoUpdateView, self).get_context_data(*args, **kwargs)

        # Zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="DN_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context
