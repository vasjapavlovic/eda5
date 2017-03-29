# Python
import os
from datetime import timedelta, datetime
import pandas as pd
import time

# Django
from django.conf import settings
from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models import F, Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import TemplateView, ListView, DetailView, UpdateView

# Templated docs
from templated_docs import fill_template
from templated_docs.http import FileResponse

# Models
from ..models import Opravilo, DelovniNalog, Delo, VzorecOpravila, DeloVrsta
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
        context['format_form'] = FormatForm 

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

        
        ###########################################################################
        # FORMS
        ###########################################################################
        format_form = FormatForm(request.POST or None)
        format_form_is_valid = True

        ###########################################################################
        # PRIDOBIMO PODATKE
        ###########################################################################
        

        # instanca
        # Delovni nalog s katerim imamo opravka (instanca)
        delovninalog = DelovniNalog.objects.get(id=self.get_object().id)

        cas_skupaj = Delo.objects.filter(delovninalog=delovninalog).aggregate(cas_skupaj=Sum(F('time_stop')-F('time_start')))

        cas_skupaj = cas_skupaj['cas_skupaj']

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="DN_DETAIL")

        # dokumenti
        dokumenti = Arhiviranje.objects.filter(delovninalog=delovninalog)

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


        # dela
        zmin = delovninalog.opravilo.zmin

        zaokrozitev_min = timedelta(minutes=zmin)  # čas v minutah
        dela_list = Delo.objects.filter(delovninalog=delovninalog)

        dela = []
        dela_vrste = []
        porabljen_cas_po_vrsti_dela = []
        skupaj_ur_rac = 0
        skupaj_ur_dej = 0
        for delo in dela_list:
            delo_datum = delo.datum
            delo_delavec = delo.delavec
            vrsta_dela = delo.vrsta_dela
            delo_naziv = delo.naziv
            porabljen_cas_rac = zaokrozen_zmin(delo.porabljen_cas, zmin, '+')
            porabljen_cas_rac_ur = pretvori_v_ure(porabljen_cas_rac)
            porabljen_cas_dej = delo.porabljen_cas
            porabljen_cas_dej_ur = pretvori_v_ure(porabljen_cas_dej)

            skupaj_ur_rac = skupaj_ur_rac + porabljen_cas_rac_ur
            skupaj_ur_dej = skupaj_ur_dej + porabljen_cas_dej_ur

            instanca = {
                'datum': delo_datum,
                'vrsta_dela': vrsta_dela,
                'delavec': delo_delavec,
                'naziv': delo_naziv,
                'porabljen_cas_rac_ur': porabljen_cas_rac_ur,
                'porabljen_cas_dej_ur': porabljen_cas_dej_ur,
            }


            # delovnih nalogovo, ki imajo manj kot eno minuto naj jih ne doda
            # na seznam
            if not porabljen_cas_rac_ur == 0:
                dela.append(instanca)
                dela_vrste.append(vrsta_dela.oznaka)
                porabljen_cas_po_vrsti_dela.append(porabljen_cas_dej_ur)



        df = pd.DataFrame({'vrsta_dela': dela_vrste, 'porabljen_cas_dej_ur': porabljen_cas_po_vrsti_dela})
        result = df.groupby('vrsta_dela').sum()
        result.sort_index(inplace=True)

        # ##########################################################

        delo_list = Delo.objects.filter(delovninalog=delovninalog).annotate(delo_cas=F('time_stop')-F('time_start'))


        '''
        Izdelamo porabljen čas za izvedbo dela
        v enoti UR in ga shranimo v bazo pod delo_cas_rac
        '''
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


        '''
        Glede na izračunane čase za izvedbo del 
        izračunamo skupne porabljene čase po VRSTA_DELA.
        '''
        delo_cas_vrstadela = Delo.objects.filter(delovninalog=delovninalog)
        vrstadel_cas_list = delo_cas_vrstadela.values('vrsta_dela__oznaka', 'vrsta_dela__naziv').order_by('vrsta_dela').annotate(vrstadela_cas_rac_sum=Sum('delo_cas_rac'))
  

        # material
        dnevnik = Dnevnik.objects.filter(delovninalog=delovninalog)






        if format_form_is_valid == True:
            ###########################################################################
            # UKAZI
            ###########################################################################
        
            # iz instance pridobimo željene podatke
            # ki jih bomo uporabili v izpisu
            vrsta_dokumenta = "DELOVNI NALOG"
            naslovnik = delovninalog.opravilo.narocilo.narocnik
            za_izvajalca = delovninalog.nosilec
            za_narocnika = delovninalog.opravilo.narocilo.narocnik.kratko_ime
            opravilo = delovninalog.opravilo
            narocilo = delovninalog.opravilo.narocilo
            datum = timezone.localtime(timezone.now()).date()

            izpis_data = {
                'vrsta_dokumenta': vrsta_dokumenta,
                'delovninalog': delovninalog,
                'naslovnik': naslovnik,
                'za_izvajalca': za_izvajalca,
                'za_narocnika': za_narocnika,
                'opravilo': opravilo,
                'narocilo': narocilo,
                'dokumenti': dokumenti,
                'dela': dela,
                'dnevnik': dnevnik,
                'skupaj_ur_rac': skupaj_ur_rac,
                'skupaj_ur_dej': skupaj_ur_dej,
                'vrstadel_cas_list': vrstadel_cas_list,
                'datum': datum,
            }

            # izdelamo izpis
            filename = fill_template(
                # oblikovna datoteka v formatu .odb, ki jo želimo uporabiti
                'obrazci/delovninalogi/delovninalog_20170327.odt', 
                # podatki za uporabo v oblikovni datoteki   
                izpis_data,                     
                output_format="pdf"
            )

            visible_filename = '{}.{}'.format(delovninalog.oznaka ,"pdf")

            return FileResponse(filename, visible_filename)

        # v primeru, da so zgornji Form-i NISO ustrezno izpolnjeni
        # izvrši spodnje ukaze

        else:
            return render(request, self.template_name, {
                'format_form': format_form,
                'modul_zavihek': modul_zavihek,
                }
            )





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



