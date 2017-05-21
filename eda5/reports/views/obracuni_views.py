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

# Utils
from eda5.core.utils import zaokrozen_zmin, pretvori_v_ure

#Models
from eda5.deli.models import Podskupina, DelStavbe
from eda5.delovninalogi.models import DelovniNalog, Delo, DeloVrsta
from eda5.etaznalastnina.models import LastniskaSkupina, Program
from eda5.moduli.models import Zavihek
from eda5.narocila.models import Narocilo
from eda5.planiranje.models import PlaniranoOpravilo
from eda5.racunovodstvo.models import VrstaStroska
from eda5.skladisce.models import Dnevnik, Artikel

# Forms
from ..forms import ObracunIzrednaDelaForm
from eda5.reports.forms import DeliSeznamFilterForm, ObracunFilterForm, ObracunIzpisVrstaForm



class ObracunZbirniDelovniNalogView(TemplateView):

    form_class= ObracunIzrednaDelaForm
    template_name = "reports/obracuni/obracuni_zbirni_delovni_nalog.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ObracunZbirniDelovniNalogView, self).get_context_data(*args, **kwargs)

    #     # zavihek
    #     modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_DETAIL")
    #     context['modul_zavihek'] = modul_zavihek


        context['obracun_izpis_vrsta_form'] = ObracunIzpisVrstaForm
    #     context['obracun_filter_form'] = ObracunFilterForm




    #     context['dn_list'] = dn_list
    #     context['naslov_data'] = naslov_data

        return context


    def get_form_kwargs(self):
        return {
          'initial': self.get_initial(),
          'prefix': self.get_prefix(),
          'data': self.request.GET or None
        }

    def get(self, request, *args, **kwargs):

        #form = self.get_form(self.get_form_class())
        obracun_izredna_dela_form = ObracunIzrednaDelaForm(request.GET or None)

        if obracun_izredna_dela_form.is_valid():
            obdobje_od = obracun_izredna_dela_form.cleaned_data['datum_od']
            obdobje_do = obracun_izredna_dela_form.cleaned_data['datum_do']
            vrsta_stroska = obracun_izredna_dela_form.cleaned_data['vrsta_stroska']
            narocilo = obracun_izredna_dela_form.cleaned_data['narocilo']

            ''' izpolnemo podakte o računskem času delovnega naloga '''

            stroskovnomesto = vrsta_stroska

            # seznam delovnih nalogov ki so del osnovnega filtra
            delovninalog_filtered_list = DelovniNalog.objects.filter(
                opravilo__narocilo=narocilo, # delovni nalogi ki so del naročila
                # opravilo__planirano_opravilo__isnull=True,  # samo neplanirana opravila
                opravilo__vrsta_stroska=vrsta_stroska,
                datum_stop__isnull=False)
                #.filter(
                #Q(datum_stop__gte=obdobje_od) & Q(datum_stop__lte=obdobje_do)
                #)

            delovninalog_filtered_list = delovninalog_filtered_list.filter(
                Q(datum_stop__gte=obdobje_od) & Q(datum_stop__lte=obdobje_do)
                )

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

                # skupni porabljen čas za izvedbo glede na vrsto del (ZUN damo ben ker se ne obračunajo)
                dela_filtered_list = Delo.objects.filter(delovninalog=dn).exclude(vrsta_dela__oznaka="ZUN").order_by('datum', 'time_start')
                vrstadel_cas_list = dela_filtered_list.values('vrsta_dela__oznaka', 'vrsta_dela__naziv').order_by('vrsta_dela').annotate(vrstadela_cas_rac_sum=Sum('delo_cas_rac'))

                # dnevnik porabljenega materiala
                material = Dnevnik.objects.filter(delovninalog=dn)

                # če v delovnemu nalogu ni del, ki se obračunajo, ga ne prikažem
                if dela_filtered_list or material:
                    dn_list.append((dn, dela_filtered_list, vrstadel_cas_list, material))

            


            naslov_data = {
                    'st_dokumenta': "DN-ZBIRNI-EDA20121-201704",
                    'tip_dokumenta': "ZBIRNI DELOVNI NALOG",
                    'obdobje': "Od " + str(obdobje_od) + " Do " + str(obdobje_do),
                    'stroskovnomesto': stroskovnomesto,
                    'narocnik': narocilo.narocnik.kratko_ime + " (" + narocilo.narocnik.davcna_st + ")",
                    'narocilo': narocilo.oznaka + "|" + narocilo.predmet,
                    'delovninalog_filtered_list': delovninalog_filtered_list,
            }



            context = self.get_context_data(
                obracun_izredna_dela_form=obracun_izredna_dela_form, 
                naslov_data=naslov_data,
                dn_list=dn_list,
            )
        else:
            context = self.get_context_data(
                obracun_izredna_dela_form=obracun_izredna_dela_form, 
            )

        return self.render_to_response(context)



    def post(self, request, *args, **kwargs):

        ###########################################################################
        # FORMS
        ###########################################################################

        obracun_izpis_vrsta_form = ObracunIzpisVrstaForm(request.POST or None)
        obracun_izredna_dela_form = ObracunIzrednaDelaForm(request.POST or None)

        obracun_izpis_vrsta_form_is_valid = False
        obracun_izredna_dela_form_is_valid = False

        ###########################################################################
        # PRIDOBIMO PODATKE
        ###########################################################################

        if obracun_izpis_vrsta_form.is_valid():
            vrsta_izpisa = obracun_izpis_vrsta_form.cleaned_data['vrsta_izpisa_field']
            obracun_izpis_vrsta_form_is_valid = True

        if obracun_izredna_dela_form.is_valid():
            obdobje_od = obracun_izredna_dela_form.cleaned_data['datum_od']
            obdobje_do = obracun_izredna_dela_form.cleaned_data['datum_do']
            vrsta_stroska = obracun_izredna_dela_form.cleaned_data['vrsta_stroska']
            narocilo = obracun_izredna_dela_form.cleaned_data['narocilo']
            obracun_izredna_dela_form_is_valid = True

            ''' izpolnemo podakte o računskem času delovnega naloga '''

            stroskovnomesto = vrsta_stroska

            # seznam delovnih nalogov ki so del osnovnega filtra
            delovninalog_filtered_list = DelovniNalog.objects.filter(
                opravilo__narocilo=narocilo, # delovni nalogi ki so del naročila
                # opravilo__planirano_opravilo__isnull=True,  # samo neplanirana opravila
                opravilo__vrsta_stroska=vrsta_stroska,
                datum_stop__isnull=False)
                #.filter(
                #Q(datum_stop__gte=obdobje_od) & Q(datum_stop__lte=obdobje_do)
                #)

            delovninalog_filtered_list = delovninalog_filtered_list.filter(
                Q(datum_stop__gte=obdobje_od) & Q(datum_stop__lte=obdobje_do)
                )

            '''
            Glede na izračunane čase za izvedbo del 
            izračunamo skupne porabljene čase po VRSTA_DELA.
            '''
            dn_list = []
            for dn in delovninalog_filtered_list:

                # skupni porabljen čas za izvedbo glede na vrsto del (ZUN damo ben ker se ne obračunajo)
                dela_filtered_list = Delo.objects.filter(delovninalog=dn).exclude(vrsta_dela__oznaka="ZUN").order_by('datum', 'time_start')
                vrstadel_cas_list = dela_filtered_list.values('vrsta_dela__oznaka', 'vrsta_dela__naziv').order_by('vrsta_dela').annotate(vrstadela_cas_rac_sum=Sum('delo_cas_rac'))

                # dnevnik porabljenega materiala
                material = Dnevnik.objects.filter(delovninalog=dn)

                # če v delovnemu nalogu ni del, ki se obračunajo, ga ne prikažem
                if dela_filtered_list or material:
                    dn_list.append((dn, dela_filtered_list, vrstadel_cas_list, material))


        #Če so formi pravilno izpolnjeni

        if obracun_izpis_vrsta_form_is_valid == True and obracun_izredna_dela_form_is_valid == True:
            ###########################################################################
            # UKAZI
            ###########################################################################

            ''' izpolnemo podakte o računskem času delovnega naloga '''

            stroskovnomesto = vrsta_stroska

            # seznam delovnih nalogov ki so del osnovnega filtra
            delovninalog_filtered_list = DelovniNalog.objects.filter(
                opravilo__narocilo=narocilo, # delovni nalogi ki so del naročila
                # opravilo__planirano_opravilo__isnull=True,  # samo neplanirana opravila
                opravilo__vrsta_stroska=vrsta_stroska,
                datum_stop__isnull=False)
                #.filter(
                #Q(datum_stop__gte=obdobje_od) & Q(datum_stop__lte=obdobje_do)
                #)

            delovninalog_filtered_list = delovninalog_filtered_list.filter(
                Q(datum_stop__gte=obdobje_od) & Q(datum_stop__lte=obdobje_do)
                )

            '''
            Glede na izračunane čase za izvedbo del 
            izračunamo skupne porabljene čase po VRSTA_DELA.
            '''
            dn_list = []
            for dn in delovninalog_filtered_list:

                # skupni porabljen čas za izvedbo glede na vrsto del (ZUN damo ben ker se ne obračunajo)
                dela_filtered_list = Delo.objects.filter(delovninalog=dn).exclude(vrsta_dela__oznaka="ZUN").order_by('datum', 'time_start')
                vrstadel_cas_list = dela_filtered_list.values('vrsta_dela__oznaka', 'vrsta_dela__naziv').order_by('vrsta_dela').annotate(vrstadela_cas_rac_sum=Sum('delo_cas_rac'))

                # dnevnik porabljenega materiala
                material = Dnevnik.objects.filter(delovninalog=dn)

                # če v delovnemu nalogu ni del, ki se obračunajo, ga ne prikažem
                if dela_filtered_list or material:
                    dn_list.append((dn, dela_filtered_list, vrstadel_cas_list, material))


            naslov_data = {
                    'st_dokumenta': "DN-ZBIRNI-EDA20121-201704",
                    'tip_dokumenta': "ZBIRNI DELOVNI NALOG",
                    'obdobje': "Od " + str(obdobje_od) + " Do " + str(obdobje_do),
                    'stroskovnomesto': stroskovnomesto,
                    'narocnik': narocilo.narocnik.kratko_ime + " (" + narocilo.narocnik.davcna_st + ")",
                    'narocilo': narocilo.oznaka + "|" + narocilo.predmet,
                    'delovninalog_filtered_list': delovninalog_filtered_list,
            }


            # prenos podatkov za aplikacijo templated_docs
            if vrsta_izpisa == "neplanirano":
                filename = fill_template(
                    'reports/obracuni/obracun_neplanirana.ods', 
                    {'naslov_data': naslov_data, 'dn_list': dn_list},
                    output_format="xlsx"
                    )
                visible_filename = 'zbirni_obracun.{}'.format("xlsx")
                return FileResponse(filename, visible_filename)

            # prenos podatkov za aplikacijo templated_docs
            if vrsta_izpisa == "neplanirano_delitev":
                filename = fill_template(
                    'reports/obracuni/obracun_neplanirana_delitev.ods', 
                    {'naslov_data': naslov_data, 'dn_list': dn_list},
                    output_format="xlsx"
                    )
                visible_filename = 'zbirni_obracun.{}'.format("xlsx")
                return FileResponse(filename, visible_filename)

        # v primeru, da so zgornji Form-i NISO ustrezno izpolnjeni
        # izvrši spodnje ukaze

        else:
            return render(request, self.template_name, {
                'obracun_izpis_vrsta_form': obracun_izpis_vrsta_form,
                'obracun_izredna_dela_form': obracun_izredna_dela_form,
                }
            )



class ObracunZbirniDelovniNalogPlaniranaView(TemplateView):

    form_class= ObracunIzrednaDelaForm
    template_name = "reports/obracuni/obracuni_zbirni_delovni_nalog_planirano.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ObracunZbirniDelovniNalogPlaniranaView, self).get_context_data(*args, **kwargs)

    #     # zavihek
    #     modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_DETAIL")
    #     context['modul_zavihek'] = modul_zavihek


        context['obracun_izpis_vrsta_form'] = ObracunIzpisVrstaForm
    #     context['obracun_filter_form'] = ObracunFilterForm




    #     context['dn_list'] = dn_list
    #     context['naslov_data'] = naslov_data

        return context


    def get_form_kwargs(self):
        return {
          'initial': self.get_initial(),
          'prefix': self.get_prefix(),
          'data': self.request.GET or None
        }

    def get(self, request, *args, **kwargs):

        #form = self.get_form(self.get_form_class())
        obracun_izredna_dela_form = ObracunIzrednaDelaForm(request.GET or None)

        if obracun_izredna_dela_form.is_valid():
            obdobje_od = obracun_izredna_dela_form.cleaned_data['datum_od']
            obdobje_do = obracun_izredna_dela_form.cleaned_data['datum_do']
            vrsta_stroska = obracun_izredna_dela_form.cleaned_data['vrsta_stroska']
            narocilo = obracun_izredna_dela_form.cleaned_data['narocilo']
            prikazi_izpis_del = obracun_izredna_dela_form.cleaned_data['prikazi_izpis_del']
            prikazi_izpis_dn = obracun_izredna_dela_form.cleaned_data['prikazi_izpis_dn']

            ''' izpolnemo podakte o računskem času delovnega naloga '''

            stroskovnomesto = vrsta_stroska

            # seznam delovnih nalogov ki so del osnovnega filtra
            delovninalog_filtered_list = DelovniNalog.objects.filter(
                opravilo__narocilo=narocilo, # delovni nalogi ki so del naročila
                # opravilo__planirano_opravilo__isnull=True,  # samo neplanirana opravila
                opravilo__vrsta_stroska=vrsta_stroska,
                datum_stop__isnull=False)
                #.filter(
                #Q(datum_stop__gte=obdobje_od) & Q(datum_stop__lte=obdobje_do)
                #)

            delovninalog_filtered_list = delovninalog_filtered_list.filter(
                Q(datum_stop__gte=obdobje_od) & Q(datum_stop__lte=obdobje_do)
                )

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


            
            vrstadel_cas_list = Delo.objects.filter(delovninalog__in=delovninalog_filtered_list).values(
                'delovninalog__opravilo__planirano_opravilo__id', 'delovninalog__opravilo__planirano_opravilo__oznaka', 'vrsta_dela__id').annotate(
                vrstadela_cas_rac_sum=Sum('delo_cas_rac')).order_by('delovninalog__opravilo__planirano_opravilo__oznaka')



            planiranoopravilo_vrstadel_sum_list = []
            for vrsta_del_sum in vrstadel_cas_list:
                planirano_opravilo_id = vrsta_del_sum['delovninalog__opravilo__planirano_opravilo__id']
                vrsta_dela_id = vrsta_del_sum['vrsta_dela__id']
                vrstadela_cas_rac_sum = vrsta_del_sum['vrstadela_cas_rac_sum']


                planiranoopravilo = PlaniranoOpravilo.objects.filter(id=planirano_opravilo_id)
                if not planiranoopravilo:
                    planiranoopravilo = ""

                else:
                    planiranoopravilo = planiranoopravilo[0]


                    dn_list = []
                    dela_delovninalog_list = Delo.objects.filter(
                        delovninalog__in=delovninalog_filtered_list, delovninalog__opravilo__planirano_opravilo=planiranoopravilo).values(
                        'delovninalog__id').annotate(dn_rac_sum=Sum('delo_cas_rac')).order_by('delovninalog__datum_start')

                    for dn in dela_delovninalog_list:
                        dn_id = dn['delovninalog__id']
                        delovninalog = DelovniNalog.objects.get(id=dn_id)
                        
                        dn_rac_sum = dn['dn_rac_sum']
                        dn_list.append((delovninalog, dn_rac_sum))


                    # Material pod delovnim nalogom
                    material_dn_list = []
                    delovninalog_filtered_id_list = delovninalog_filtered_list.values_list('id', flat=True)
                    dela_delovninalog_list = DelovniNalog.objects.filter(
                        id__in=delovninalog_filtered_id_list, opravilo__planirano_opravilo=planiranoopravilo).values(
                        'dnevnik__artikel__id').annotate(material_kom=Sum('dnevnik__kom'))

                    for dn in dela_delovninalog_list:
                        artikel_id = dn['dnevnik__artikel__id']
                        artikel = Artikel.objects.filter(id=artikel_id).first()
                        
                        if artikel:
                            artikel_dn_kom = dn['material_kom']
                            material_dn_list.append((artikel, artikel_dn_kom))





                vrstadela = DeloVrsta.objects.filter(id=vrsta_dela_id)
                if not vrstadela:
                    vrstadela = ""
                else:
                    vrstadela = vrstadela[0]




                vnos = {
                    'plan': planiranoopravilo.plan,
                    'planiranoopravilo': planiranoopravilo,
                    'vrstadela': vrstadela,
                    'dn_list':dn_list,
                    'material_dn_list': material_dn_list,
                    'planiranoopravilo_vrstadela_cas_rac_sum': vrstadela_cas_rac_sum,
                }

                planiranoopravilo_vrstadel_sum_list.append(vnos)






            skupaj_ur = vrstadel_cas_list.aggregate(skupaj_ur=Sum('vrstadela_cas_rac_sum'))

            naslov_data = {
                    'st_dokumenta': "DN-ZBIRNI-" + stroskovnomesto.oznaka + str(obdobje_do),
                    'tip_dokumenta': "ZBIRNI DELOVNI NALOG",
                    'obdobje_od': str(obdobje_od),
                    'obdobje_do': str(obdobje_do),
                    'stroskovnomesto': stroskovnomesto,
                    'narocnik': narocilo.narocnik.kratko_ime + " (" + narocilo.narocnik.davcna_st + ")",
                    'narocilo': narocilo.oznaka + "|" + narocilo.predmet,
                    'delovninalog_filtered_list': delovninalog_filtered_list,
                    'prikazi_izpis_del': prikazi_izpis_del,
                    'prikazi_izpis_dn': prikazi_izpis_dn,
            }



            context = self.get_context_data(
                obracun_izredna_dela_form=obracun_izredna_dela_form, 
                naslov_data=naslov_data,
                planiranoopravilo_vrstadel_sum_list=planiranoopravilo_vrstadel_sum_list,
                skupaj_ur=skupaj_ur,
            )
        else:
            context = self.get_context_data(
                obracun_izredna_dela_form=obracun_izredna_dela_form, 
            )

        return self.render_to_response(context)




    def post(self, request, *args, **kwargs):

        ###########################################################################
        # FORMS
        ###########################################################################

        obracun_izpis_vrsta_form = ObracunIzpisVrstaForm(request.POST or None)
        obracun_izredna_dela_form = ObracunIzrednaDelaForm(request.POST or None)

        obracun_izpis_vrsta_form_is_valid = False
        obracun_izredna_dela_form_is_valid = False

        ###########################################################################
        # PRIDOBIMO PODATKE
        ###########################################################################

        if obracun_izpis_vrsta_form.is_valid():
            vrsta_izpisa = obracun_izpis_vrsta_form.cleaned_data['vrsta_izpisa_field']
            obracun_izpis_vrsta_form_is_valid = True

        if obracun_izredna_dela_form.is_valid():
            obdobje_od = obracun_izredna_dela_form.cleaned_data['datum_od']
            obdobje_do = obracun_izredna_dela_form.cleaned_data['datum_do']
            vrsta_stroska = obracun_izredna_dela_form.cleaned_data['vrsta_stroska']
            narocilo = obracun_izredna_dela_form.cleaned_data['narocilo']
            prikazi_izpis_del = obracun_izredna_dela_form.cleaned_data['prikazi_izpis_del']
            prikazi_izpis_dn = obracun_izredna_dela_form.cleaned_data['prikazi_izpis_dn']
            obracun_izredna_dela_form_is_valid = True



        #Če so formi pravilno izpolnjeni

        if obracun_izpis_vrsta_form_is_valid == True and obracun_izredna_dela_form_is_valid == True:
            ###########################################################################
            # UKAZI
            ###########################################################################

            ''' izpolnemo podakte o računskem času delovnega naloga '''

            stroskovnomesto = vrsta_stroska

            # seznam delovnih nalogov ki so del osnovnega filtra
            delovninalog_filtered_list = DelovniNalog.objects.filter(
                opravilo__narocilo=narocilo, # delovni nalogi ki so del naročila
                # opravilo__planirano_opravilo__isnull=True,  # samo neplanirana opravila
                opravilo__vrsta_stroska=vrsta_stroska,
                datum_stop__isnull=False)
                #.filter(
                #Q(datum_stop__gte=obdobje_od) & Q(datum_stop__lte=obdobje_do)
                #)

            delovninalog_filtered_list = delovninalog_filtered_list.filter(
                Q(datum_stop__gte=obdobje_od) & Q(datum_stop__lte=obdobje_do)
                )
            '''
            Glede na izračunane čase za izvedbo del 
            izračunamo skupne porabljene čase po VRSTA_DELA.
            '''


            
            vrstadel_cas_list = Delo.objects.filter(delovninalog__in=delovninalog_filtered_list).values(
                'delovninalog__opravilo__planirano_opravilo__id', 'delovninalog__opravilo__planirano_opravilo__oznaka', 'vrsta_dela__id').annotate(
                vrstadela_cas_rac_sum=Sum('delo_cas_rac')).order_by('delovninalog__opravilo__planirano_opravilo__oznaka')



            planiranoopravilo_vrstadel_sum_list = []
            for vrsta_del_sum in vrstadel_cas_list:
                planirano_opravilo_id = vrsta_del_sum['delovninalog__opravilo__planirano_opravilo__id']
                vrsta_dela_id = vrsta_del_sum['vrsta_dela__id']
                vrstadela_cas_rac_sum = vrsta_del_sum['vrstadela_cas_rac_sum']


                planiranoopravilo = PlaniranoOpravilo.objects.filter(id=planirano_opravilo_id)
                if not planiranoopravilo:
                    planiranoopravilo = ""

                else:
                    planiranoopravilo = planiranoopravilo[0]


                    dn_list = []
                    dela_delovninalog_list = Delo.objects.filter(
                        delovninalog__in=delovninalog_filtered_list, delovninalog__opravilo__planirano_opravilo=planiranoopravilo).values(
                        'delovninalog__id').annotate(dn_rac_sum=Sum('delo_cas_rac')).order_by('delovninalog__datum_start')

                    for dn in dela_delovninalog_list:
                        dn_id = dn['delovninalog__id']
                        delovninalog = DelovniNalog.objects.get(id=dn_id)
                        
                        dn_rac_sum = dn['dn_rac_sum']
                        dn_list.append((delovninalog, dn_rac_sum))


                    # Material pod delovnim nalogom
                    material_dn_list = []
                    delovninalog_filtered_id_list = delovninalog_filtered_list.values_list('id', flat=True)
                    dela_delovninalog_list = DelovniNalog.objects.filter(
                        id__in=delovninalog_filtered_id_list, opravilo__planirano_opravilo=planiranoopravilo).values(
                        'dnevnik__artikel__id').annotate(material_kom=Sum('dnevnik__kom'))

                    for dn in dela_delovninalog_list:
                        artikel_id = dn['dnevnik__artikel__id']
                        artikel = Artikel.objects.filter(id=artikel_id).first()
                        
                        if artikel:
                            artikel_dn_kom = dn['material_kom']
                            material_dn_list.append((artikel, artikel_dn_kom))



                vrstadela = DeloVrsta.objects.filter(id=vrsta_dela_id)
                if not vrstadela:
                    vrstadela = ""
                else:
                    vrstadela = vrstadela[0]




                vnos = {
                    'plan': planiranoopravilo.plan,
                    'planiranoopravilo': planiranoopravilo,
                    'vrstadela': vrstadela,
                    'dn_list':dn_list,
                    'material_dn_list': material_dn_list,
                    'planiranoopravilo_vrstadela_cas_rac_sum': vrstadela_cas_rac_sum,
                }

                planiranoopravilo_vrstadel_sum_list.append(vnos)






            skupaj_ur = vrstadel_cas_list.aggregate(skupaj_ur=Sum('vrstadela_cas_rac_sum'))

            naslov_data = {
                    'st_dokumenta': "DN-ZBIRNI-" + stroskovnomesto.oznaka + str(obdobje_do),
                    'tip_dokumenta': "ZBIRNI DELOVNI NALOG",
                    'obdobje_od': str(obdobje_od),
                    'obdobje_do': str(obdobje_do),
                    'stroskovnomesto': stroskovnomesto,
                    'narocnik': narocilo.narocnik.kratko_ime + " (" + narocilo.narocnik.davcna_st + ")",
                    'narocilo': narocilo.oznaka + "|" + narocilo.predmet,
                    'delovninalog_filtered_list': delovninalog_filtered_list,
                    'prikazi_izpis_del': prikazi_izpis_del,
                    'prikazi_izpis_dn': prikazi_izpis_dn,
            }


            # prenos podatkov za aplikacijo templated_docs
            if vrsta_izpisa == "planirano":
                filename = fill_template(
                    'reports/obracuni/obracun_planirano.ods', 
                    {
                    'naslov_data': naslov_data,
                    'planiranoopravilo_vrstadel_sum_list': planiranoopravilo_vrstadel_sum_list,
                    'skupaj_ur': skupaj_ur,
                    },
                    output_format="xlsx"
                    )
                visible_filename = 'zbirni_obracun.{}'.format("xlsx")
                return FileResponse(filename, visible_filename)

            # prenos podatkov za aplikacijo templated_docs
            if vrsta_izpisa == "planirano_delitev":
                filename = fill_template(
                     {
                    'naslov_data': naslov_data,
                    'planiranoopravilo_vrstadel_sum_list': planiranoopravilo_vrstadel_sum_list,
                    'skupaj_ur': skupaj_ur,
                    },
                    output_format="xlsx"
                    )
                visible_filename = 'zbirni_obracun.{}'.format("xlsx")
                return FileResponse(filename, visible_filename)

        # v primeru, da so zgornji Form-i NISO ustrezno izpolnjeni
        # izvrši spodnje ukaze

        else:
            return render(request, self.template_name, {
                'obracun_izpis_vrsta_form': obracun_izpis_vrsta_form,
                'obracun_izredna_dela_form': obracun_izredna_dela_form,
                }
            )
