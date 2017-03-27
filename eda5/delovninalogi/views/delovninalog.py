# Python
from datetime import datetime, timedelta
import os


# Django
from django.conf import settings
from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.views.generic import TemplateView, ListView, DetailView, UpdateView


# Templated docs
from templated_docs import fill_template
from templated_docs.http import FileResponse


# Models
from ..models import Opravilo, DelovniNalog, Delo, VzorecOpravila
from eda5.arhiv.models import Arhiviranje, ArhivMesto
from eda5.moduli.models import Zavihek
from eda5.partnerji.models import Oseba
from eda5.skladisce.models import Dnevnik
from eda5.zaznamki.models import Zaznamek


# Forms
from ..forms import OpraviloUpdateForm, DelovniNalogVcakanjuModelForm, DelovniNalogVplanuModelForm
from ..forms import DelovniNalogVresevanjuModelForm, DeloCreateForm, DeloKoncajUpdateForm
from eda5.arhiv.forms import ArhiviranjeDelovniNalogForm
from eda5.reports.forms import FormatForm
from eda5.zaznamki.forms import ZaznamekForm


# Mixins
from ..mixins import MessagesActionMixin



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


class DelovniNalogDetailView(MessagesActionMixin, DetailView):
    model = DelovniNalog
    template_name = "delovninalogi/delovninalog/detail/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DelovniNalogDetailView, self).get_context_data(*args, **kwargs)

        # arhiv
        context['arhiviranje_form'] = ArhiviranjeDelovniNalogForm

        # delo
        context['odprta_dela'] = Delo.objects.odprta_dela()
        context['koncana_dela'] = Delo.objects.koncana_dela()
        context['delo_create_form'] = DeloCreateForm
        context['delo_update_form'] = DeloKoncajUpdateForm
        context['delo_list'] = Delo.objects.filter(delovninalog=self.object.id)
        context['delo_delavec_distinct_list'] = Delo.objects.filter(delovninalog=self.object.id).distinct('delavec')

        # from za izbiro formata izvoza
        context['form'] = FormatForm 

        # skladisce
        context['material_list'] = Dnevnik.objects.filter(delovninalog=self.object.id)

        # zaznamek
        context['zaznamek_form'] = ZaznamekForm
        context['zaznamek_list'] = Zaznamek.objects.filter(delovninalog=self.object.id)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="DN_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context


    def post(self, request, *args, **kwargs):

        # Delovni nalog s katerim imamo opravka (instanca)
        delovninalog = DelovniNalog.objects.get(id=self.get_object().id)

        # FORMS
        arhiviranje_form = ArhiviranjeDelovniNalogForm(request.POST or None)
        zaznamek_form = ZaznamekForm(request.POST or None)
        delo_create_form = DeloCreateForm(request.POST or None)
        delo_update_form = DeloKoncajUpdateForm(request.POST or None)


        
        # ZAZNAMKI
        # =================================================================================================
        ''' Vnašanje zaznamkov v delovni nalog preko
        okna, ki se odpre nad obstoječim oknom (MODAL)'''

        if zaznamek_form.is_valid():

            # pridobimo podatke iz forma
            tekst = zaznamek_form.cleaned_data['tekst']
            datum = zaznamek_form.cleaned_data['datum']
            ura = zaznamek_form.cleaned_data['ura']


            # izdelamo zaznamek znotraj delovnega naloga
            Zaznamek.objects.create_zaznamek(
                tekst=tekst,
                datum=datum,
                ura=ura,
                delovninalog=delovninalog,
            )

            # redirectamo na obstoječi delovni nalog
            return HttpResponseRedirect(reverse('moduli:delovninalogi:dn_detail', kwargs={'pk': delovninalog.pk}))

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
                zahtevek=delovninalog.opravilo.zahtevek,
                dokument=dokument,
                arhiviral=arhiviral,
                elektronski=elektronski,
                fizicni=fizicni,
                lokacija_hrambe=lokacija_hrambe,
            )

            return HttpResponseRedirect(reverse('moduli:delovninalogi:dn_detail', kwargs={'pk': delovninalog.pk}))

        return HttpResponseRedirect(reverse('moduli:delovninalogi:dn_detail', kwargs={'pk': delovninalog.pk}))


# Planiranje delovnih nalogov s statusom "V Čakanju"
class DelovniNalogUpdateVcakanjuView(MessagesActionMixin, UpdateView):
    model = DelovniNalog
    form_class = DelovniNalogVcakanjuModelForm
    template_name = "delovninalogi/delovninalog/update_vcakanju.html"
    # Preusmerimo na seznam delovnih nalogov
    success_url = reverse_lazy('moduli:delovninalogi:dn_list')
    # Sporočilo uporabniku
    success_msg = "Delovninalog je bil uspešno dodan v plan."

    def get_context_data(self, *args, **kwargs):
        context = super(DelovniNalogUpdateVcakanjuView, self).get_context_data(*args, **kwargs)

        # Zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="DN_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context


class DelovniNalogUpdateVresevanjuView(MessagesActionMixin, UpdateView):
    model = DelovniNalog
    form_class = DelovniNalogVresevanjuModelForm
    template_name = "delovninalogi/delovninalog/update_vresevanju.html"

    success_msg = "Delovni nalog je bil zaključen. Potrjeni delovni nalogi\
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
        # Delovnih nalogov z odprtimi deli ni mogoče zaključiti!
        # pridobimo instanco delovnega naloga
        delovninalog_id = self.kwargs['pk']
        delovninalog = DelovniNalog.objects.get(id=delovninalog_id)

        # pridobimo seznam nedokončanih del
        dela = Delo.objects.filter(delovninalog=delovninalog, time_stop__isnull=True)
        # če nedokončana dela obstajajo opozori in preusmeri
        if dela:
            # opozorilo
            messages.error(self.request, "Delovnega naloga z odprtimi deli ni mogoče zaključiti!")
            #preusmeritev
            return HttpResponseRedirect(reverse('moduli:delovninalogi:dn_detail', kwargs={'pk': delovninalog.pk }))
        return super(DelovniNalogUpdateVresevanjuView, self).form_valid(form)



