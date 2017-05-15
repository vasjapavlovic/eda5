# Python
import datetime as dt
import os
from datetime import timedelta, datetime
import pandas as pd
import time
# Django
from django.db.models import Q, F, Sum
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import TemplateView, DetailView

# Templated Docs
from templated_docs import fill_template
from templated_docs.http import FileResponse

#Models
from eda5.deli.models import Podskupina, DelStavbe
from eda5.delovninalogi.models import DelovniNalog, Delo
from eda5.etaznalastnina.models import LastniskaSkupina, Program
from eda5.moduli.models import Zavihek
from eda5.narocila.models import Narocilo
from eda5.skladisce.models import Dnevnik

# Forms
from eda5.reports.forms import FormatForm, DeliSeznamFilterForm, ObracunFilterForm




###########################################################
# SEZNAM DELOV STAVBE PO PROGRAMIH - PRINT
###########################################################
class ObracunZbirniDelovniNalogView(TemplateView):

    template_name = "reports/obracuni/obracuni_zbirni_delovni_nalog.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ObracunZbirniDelovniNalogView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        context['form'] = FormatForm
        context['obracun_filter_form'] = ObracunFilterForm


        # fiksniramo izpis na naročilo --> Pogodba o izvajanju upravniških storitev
        narocilo = Narocilo.objects.get(oznaka="NRC-2016-7")

        # obdobje
        obdobje_od = dt.date(2017, 4, 1)
        obdobje_do = dt.date(2017, 4, 30)
        

        # seznam delovnih nalogov ki so del osnovnega filtra
        delovninalog_filtered_list = DelovniNalog.objects.filter(
            opravilo__narocilo=narocilo, # delovni nalogi ki so del naročila
            datum_stop__isnull=False).filter(
            Q(datum_stop__gte=obdobje_od) & Q(datum_stop__lte=obdobje_do)
            )

        ''' izpolnemo podakte o računskem času delovnega naloga '''


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

        for delovninalog in delovninalog_filtered_list:


            # enota za zaokroževanje
            zmin = delovninalog.opravilo.zmin
            # seznam del pod delovnim nalogom
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
        dn_list = []
        for dn in delovninalog_filtered_list:

            # skupni porabljen čas za izvedbo glede na vrsto del
            delo_cas_vrstadela = Delo.objects.filter(delovninalog=dn)
            vrstadel_cas_list = delo_cas_vrstadela.values('vrsta_dela__oznaka', 'vrsta_dela__naziv').order_by('vrsta_dela').annotate(vrstadela_cas_rac_sum=Sum('delo_cas_rac'))
            dela = vrstadel_cas_list

            # dnevnik porabljenega materiala
            material = Dnevnik.objects.filter(delovninalog=dn)

            dn_list.append((dn, dela, material))

        '''
        Skupni čas porabljen za izvedbo vseh del
        po delovnem nalogu
        '''
        # izračunamo skupni porabljen čas
        # skupaj_ur_rac = Delo.objects.filter(delovninalog=dn).aggregate(skupaj_ur_rac=Sum(F('delo_cas_rac')))

        # skupaj_ur_rac = skupaj_ur_rac['skupaj_ur_rac']

        ##################################################################
        '''
        Izpis materiala v delovnem nalogu
        '''
        ##################################################################
        


        naslov_data = {
                'st_dokumenta': "DN-ZBIRNI-EDA20121-201704",
                'tip_dokumenta': "ZBIRNI DELOVNI NALOG",
                'narocnik': narocilo.narocnik.kratko_ime + " (" + narocilo.narocnik.davcna_st + ")",
                'narocilo': narocilo.oznaka + "|" + narocilo.predmet,
                'delovninalog_filtered_list': delovninalog_filtered_list,
        }

        context['dn_list'] = dn_list
        context['naslov_data'] = naslov_data

        return context


    def post(self, request, *args, **kwargs):

        ###########################################################################
        # FORMS
        ###########################################################################

        form = FormatForm(request.POST or None)
        obracun_filter_form = ObracunFilterForm(request.POST or None)

        form_is_valid = False
        obracun_filter_form_is_valid = False

        ###########################################################################
        # PRIDOBIMO PODATKE
        ###########################################################################

        if form.is_valid():
            doctypex = form.cleaned_data['format_field']
            form_is_valid = True

        if obracun_filter_form_is_valid.is_valid():
            obdobje_leto = obracun_filter_form_is_valid.cleaned_data['obdobje_leto']
            obdobje_mesec = obracun_filter_form_is_valid.cleaned_data['obdobje_mesec']
            obracun_filter_form_is_valid = True

        #Če so formi pravilno izpolnjeni

        if form_is_valid == True and obracun_filter_form_is_valid == True:
            ###########################################################################
            # UKAZI
            ###########################################################################

            # pridobimo današnji datum za izpis na izpisu

            datum_danes = timezone.now().date()

            # izdelamo seznam delovnih nalogov glede na izbrane filtre (Mesečni obračun)
            delovninalog_filtered_list = DelovniNalog.objects.filter(
                opravilo__narocilo__izvajalec__davcna_st="97041823",  # prikažemo samo delovne naloge za izvajalca EDAFM
                # filter glede na izbrano leto,
                # filter glede na izbran mesec,
            )

            return HttpResponseRedirect(reverse('moduli:reports:zahtevek_detail', kwargs={'pk': zahtevek.pk}))




            return FileResponse(filename, visible_filename)

        # v primeru, da so zgornji Form-i NISO ustrezno izpolnjeni
        # izvrši spodnje ukaze

        else:
            return render(request, self.template_name, {
                'form': form,
                'deli_seznam_filter_form': deli_seznam_filter_form,
                }
            )
