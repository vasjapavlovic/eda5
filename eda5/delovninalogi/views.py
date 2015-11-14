from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.utils import timezone
from django.views.generic import TemplateView, ListView, DetailView, UpdateView


from .mixins import MessagesActionMixin
from .forms import OpraviloModelForm, DelovniNalogVcakanjuModelForm, DelovniNalogVplanuModelForm,\
                   DelovniNalogVresevanjuModelForm, DeloForm, DeloZacetoUpdateModelForm

from .forms import DelovniNalogAddDokumentForm
from .models import Opravilo, DelovniNalog, Delo

from eda5.zaznamki.forms import ZaznamekForm
from eda5.zaznamki.models import Zaznamek


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
    template_name = "delovninalogi/opravilo/detail.html"


# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
class OpraviloUpdateView(UpdateView):
    model = Opravilo
    form_class = OpraviloModelForm
    template_name = "delovninalogi/opravilo/update.html"


# DELOVNI NALOG*******************************************************************************************
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
class DelovniNalogList(ListView):
    model = DelovniNalog
    template_name = "delovninalogi/delovninalog/list/extended.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DelovniNalogList, self).get_context_data(*args, **kwargs)

        # content
        context['dn_vcakanju_list'] = self.model.objects.dn_vcakanju()
        context['dn_vplanu_list'] = self.model.objects.dn_vplanu()
        context['dn_vresevanju_list'] = self.model.objects.dn_vresevanju()
        context['dn_zakljuceni_list'] = self.model.objects.dn_zakljuceni()

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

        # zaznamek
        context['zaznamek_form'] = ZaznamekForm
        context['zaznamek_list'] = Zaznamek.objects.filter(delovninalog=self.object.id)

        # delo
        context['delo_form'] = DeloForm
        context['delo_list'] = Delo.objects.filter(delovninalog=self.object.id)
        context['delo_delavec_distinct_list'] = Delo.objects.filter(delovninalog=self.object.id).distinct('delavec')

        return context

    def post(self, request, *args, **kwargs):

        # DELOVNI-NALOG s katerim imamo opravka
        # =================================================================================================
        delovninalog = DelovniNalog.objects.get(id=self.get_object().id)

        # VNOS ZAZNAMKA
        # =================================================================================================
        zaznamek_form = ZaznamekForm(request.POST or None)

        if zaznamek_form.is_valid():

            # PODATKI ZA VNOS
            # ---------------------------------------------------------------------------------------------
            tekst = zaznamek_form.cleaned_data['tekst']
            datum = zaznamek_form.cleaned_data['datum']
            ura = zaznamek_form.cleaned_data['ura']

            # DODATNE VALIDACIJE
            # ---------------------------------------------------------------------------------------------
            # validacija_zaznamek_add_01
            '''če je delovni-nalog že zaključen novih zaznamkov ni mogoče vnašati. V templates je gumb za nove vnose
            odstranjen.Ta validacija je samo za slučaj če bi se link do gumba ročno vnesel'''

            if delovninalog.status == 4:
                messages.error(request, "Delovni nalog je že zaključen! Novih zaznamkov ni mogoče vnašati.")
                return HttpResponseRedirect(reverse('moduli:delovninalogi:dn_detail', kwargs={'pk': delovninalog.pk}))

            # VNOS V BAZO
            # ---------------------------------------------------------------------------------------------
            Zaznamek.objects.create_zaznamek(tekst=tekst,
                                             datum=datum,
                                             ura=ura,
                                             delovninalog=delovninalog,
                                             )

            # POGOJI PREUSMERJANJA
            # ---------------------------------------------------------------------------------------------

        # VNOS NOVEGA DELA
        # =================================================================================================
        delo_form = DeloForm(request.POST or None)

        if delo_form.is_valid():

            # PODATKI ZA VNOS
            # ---------------------------------------------------------------------------------------------

            delavec = delo_form.cleaned_data['delavec']
            datum = timezone.now().date()
            time_start = timezone.now().time().strftime("%H:%M:%S")

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
                    messages.error(request, "Končati je potrebno predhodno delo z oznako '%s'"
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


            Delo.objects.create_delo(delavec=delavec,
                                     datum=datum,
                                     time_start=time_start,
                                     delovninalog=delovninalog,
                                     )

            messages.success(request, 'Novo delo je vneseno')
            # sporočilo uporabniku

            # POGOJI PREUSMERJANJA
            # ---------------------------------------------------------------------------------------------




            '''Ko je status delovnega-naloga "V PLANU" izvedi preusmeritev na UPDATE-STATUS --> dn_update_vplanu'''
            if delovninalog.status == 2:
                return HttpResponseRedirect(reverse('moduli:delovninalogi:dn_update_vplanu',
                                                    kwargs={'pk': delovninalog.pk}))

        return HttpResponseRedirect(reverse('moduli:delovninalogi:dn_detail', kwargs={'pk': delovninalog.pk}))


# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
class DelovniNalogUpdateVcakanjuView(MessagesActionMixin, UpdateView):
    model = DelovniNalog
    form_class = DelovniNalogVcakanjuModelForm
    template_name = "delovninalogi/delovninalog/update_vcakanju.html"
    success_url = reverse_lazy('moduli:delovninalogi:dn_list')

    success_msg = "Status zahtevka je spremenjen na 'V PLANU'"


# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
class DelovniNalogUpdateVplanuView(MessagesActionMixin, UpdateView):
    model = DelovniNalog
    form_class = DelovniNalogVplanuModelForm
    template_name = "delovninalogi/delovninalog/update_vplanu.html"

    success_msg = "Status zahtevka je spremenjen na 'V REŠEVANJU'"


# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
class DelovniNalogUpdateVresevanjuView(MessagesActionMixin, UpdateView):
    model = DelovniNalog
    form_class = DelovniNalogVresevanjuModelForm
    template_name = "delovninalogi/delovninalog/update_vresevanju.html"

    success_msg = "Status zahtevka je spremenjen na 'ZAKLJUČENO'. Potrjeni delovni nalogi\
                  iz strani nadzornika bodo obarvani v zeleno."


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
class DelovniNalogUpdateDokumentFormView(MessagesActionMixin, UpdateView):
    model = DelovniNalog
    form_class = DelovniNalogAddDokumentForm
    template_name = "delovninalogi/delovninalog/update_dokument.html"

    success_msg = "Dokumentacija je bila uspešno spremenjena."


# DELO****************************************************************************************************
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
class DeloZacetoUpdateView(MessagesActionMixin, UpdateView):
    model = Delo
    form_class = DeloZacetoUpdateModelForm
    template_name = "delovninalogi/delo/update_zaceto.html"

    success_msg = "Delo je uspešno končano."
