import csv
import io
import os
import getpass
import shutil


from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView


# Import FORMS
from ..forms import \
    import_common_forms, \
    import_lokacija_forms, \
    import_deli_forms


# Deli FORMS
from eda5.deli.forms import \
    skupina_forms,\
    podskupina_forms, \
    projektnomesto_forms, \
    deli_lokacija_forms, \
    delstavbe_forms


# Lokacija FORMS
from eda5.deli.forms import \
    deli_lokacija_forms, \
    projektnomesto_forms


# Lokacija MODELS
from eda5.deli.models import \
    Stavba, Etaza, Lokacija, Skupina, Podskupina, DelStavbe, ProjektnoMesto

# Katalog MODELS
from eda5.katalog.models import \
    TipArtikla

# Moduli
from eda5.moduli.models import Zavihek


class LokacijaUvozPodatkovView(TemplateView):
    template_name = "deli/uvozpodatkov/uvoz_podatkov_create.html"

    def get_context_data(self, *args, **kwargs):
        context = super(LokacijaUvozPodatkovView, self).get_context_data(*args, **kwargs)

        # Deli
        context['csv_file_path_form'] = import_common_forms.CsvFilePath
        # popravi naziv : tak je samo zato ker je uporabljen en template
        context['deli_uvoz_form'] = import_lokacija_forms.LokacijaUvozCsvForm


        # Zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):
        csv_file_path_form = import_common_forms.CsvFilePath(request.POST or None, request.FILES)
        lokacije_uvoz_form = import_lokacija_forms.LokacijaUvozCsvForm(request.POST or None)
        deli_uvoz_form = import_deli_forms.DeliUvozCsvForm(request.POST or None)



        def get_file_data(csv_file):

            ''' Izbrano datoteko začasno shranimo na disk za branje'''

            # pridobimo username iz linuxa
            linux_user = getpass.getuser()

            # če direktorij TEMP ne obstaja ga izdelamo
            if not os.path.exists("/home/%s/temp" % (linux_user)):
                os.mkdir("/home/%s/temp" % (linux_user))

            # Datoteko začasno shranimo na disk
            fout = open("/home/%s/temp/%s" % (linux_user, csv_file.name), 'wb')
            for chunk in csv_file.chunks():
                fout.write(chunk)
            fout.close()

            ''' Uvoz CSV podatkov v bazo'''

            # Uvozimo vrednosti v bazo
            with open("/home/%s/temp/%s" % (linux_user, csv_file), 'r') as file:
                vsebina = file.read()

            rows = io.StringIO(vsebina)


            seznam = csv.DictReader(rows, delimiter=",")

            return seznam, linux_user



        def import_del01_prostori(csv_file):

            ''' Preberemo podatke iz datoteke .csv '''

            seznam, linux_user = get_file_data(csv_file)
            
            # CREATED
            stavbe_records_added = 0
            etaze_records_added = 0
            prostori_records_added = 0
            lokacije_records_added = 0
            projektnamesta_records_added = 0

            # UPDATED
            stavbe_records_updated = 0
            etaze_records_updated = 0
            prostori_records_updated = 0
            lokacije_records_updated = 0
            projektnamesta_records_updated = 0



            for row in seznam:

                ##############################################################################################
                # ATRIBUTI iz SEZNAMA
                #---------------------------------------------------------------------------------------------

                # Pridobimo atribute iz seznama
                delstavbe_prostor_oznaka = row['oznaka']
                delstavbe_prostor_naziv = row['naziv']
                delstavbe_prostor_funkcija = row['funkcija']
                delstavbe_prostor_bim_id = row['bim_id']
                etaza_oznaka = row['etaza']
                etaza_elevation = row['elevation']
                stavba_oznaka = row['stavba']
                delstavbe_klasifikacija = row['klasifikacija']

                errors = []

                # klasifikacijo razdelimo na več atributov
                # skupina, podskupina, delstavbe se pridobi iz klasifikacije
                # npr. A_AA_AA01_Naziv
                eda5, skupina_oznaka, podskupina_oznaka, delstavbe_oznaka, ostanek = delstavbe_klasifikacija.split("_", 4)
                # še naziv dela stavbe
                delstavbe_naziv, ostanek2 = ostanek.split(".", 1)


                # ===========================================================================================
                # ===========================================================================================
                # ===========================================================================================
                # VRSTNI RED IZDELAVE
                # - STAVBA
                # - ETAŽA
                # - DELI STAVBE (prostori)
                # - LOKACIJE
                # - PROJEKTNA MESTA (tlak, strop, stene, el-oprema)
                # ===========================================================================================
                # ===========================================================================================
                # ===========================================================================================

                ##############################################################################################
                # STAVBA
                #---------------------------------------------------------------------------------------------
                
                # 'oznaka',
                # 'naziv', 
                # 'opis', 

                stavba_oznaka = stavba_oznaka
                stavba_naziv = "NA"
                stavba_opis = "NA"

                stavba_data = {
                    'oznaka': stavba_oznaka,
                    'naziv': stavba_naziv,
                    'opis': stavba_opis,
                }

                # CREATE
                # ------------------------------------------------------------
                if not Stavba.objects.filter(oznaka=stavba_oznaka).exists():
                    
                    # definiramo FORM za vnos
                    stavba_create_form = deli_lokacija_forms.StavbaCreateForm(stavba_data)
                    if stavba_create_form.is_valid():
                        # shranimo podakte
                        stavba_create_form.save()
                        # število dodanih vnosov povečamo za 1
                        stavbe_records_added += 1
                        print("Stavba '%s' je bila dodana" % (stavba_data['oznaka']))

                    else:
                        errors.append(stavba_create_form.errors)
                        print(errors)



                ##############################################################################################
                # ETAŽA
                #---------------------------------------------------------------------------------------------
                # Atributi

                # 'oznaka',
                # 'naziv', 
                # 'opis',
                # 'elevation',
                # 'stavba',

                etaza_oznaka = etaza_oznaka
                etaza_naziv = "NA"
                etaza_opis = "NA"
                etaza_elevation = etaza_elevation 
                stavba_object = Stavba.objects.get(oznaka=stavba_oznaka)
                stavba_id = stavba_object.id

                etaza_data = {
                    'oznaka': etaza_oznaka,
                    'naziv': etaza_naziv,
                    'opis': etaza_opis,
                    'elevation': etaza_elevation,
                    'stavba': stavba_id,
                    'stavba_object': stavba_object,
                }

                # CREATE
                # ------------------------------------------------------------
                if not Etaza.objects.filter(oznaka=etaza_oznaka).exists():
                    
                    # definiramo FORM za vnos
                    etaza_create_form = deli_lokacija_forms.EtazaCreateForm(etaza_data)
                    if etaza_create_form.is_valid():
                        # shranimo podakte
                        etaza_create_form.save()
                        # število dodanih vnosov povečamo za 1
                        stavbe_records_added += 1
                        print("Etaža '%s' je bila dodana" % (etaza_data['oznaka']))

                    else:
                        errors.append(etaza_create_form.errors)
                        print(errors)       


                ##############################################################################################
                # DEL STAVBE - PROSTORI
                #---------------------------------------------------------------------------------------------
                
                # Atributi

                    # pridobimo osnovne atribute za vnos
                    # 'oznaka',
                    # 'naziv', 
                    # 'funkcija', 
                    # 'bim_id',
                    # 'podskupina',

                # podskupina
                # podskupino pridobimo iz klasifikacije = naziv archicad layer-ja
                # npr. A_AA_AA01_Naziv

                ##############################################################################################
                # DEL STAVBE
                #---------------------------------------------------------------------------------------------
                
                # 'oznaka',
                # 'naziv', 
                # 'funkcija', 
                # 'bim_id',
                # 'podskupina',

                delstavbe_prostor_oznaka = delstavbe_prostor_oznaka
                delstavbe_prostor_naziv = delstavbe_prostor_naziv
                delstavbe_prostor_funkcija = delstavbe_prostor_funkcija
                delstavbe_prostor_bim_id = delstavbe_prostor_bim_id
                delstavbe_prostor_podskupina = Podskupina.objects.get(oznaka=podskupina_oznaka)
                delstavbe_prostor_podskupina_id = delstavbe_prostor_podskupina.id

                delstavbe_prostor_data = {
                    'oznaka': delstavbe_prostor_oznaka,
                    'naziv': delstavbe_prostor_naziv,
                    'funkcija': delstavbe_prostor_funkcija,
                    'bim_id': delstavbe_prostor_bim_id,
                    'podskupina': delstavbe_prostor_podskupina_id,
                    'podskupina_object': delstavbe_prostor_podskupina,
                }
                
                # CREATE
                # ------------------------------------------------------------
                if not DelStavbe.objects.filter(bim_id=delstavbe_prostor_bim_id).exists():
                    
                    # IZDELAMO PROSTOR
                    # -------------------------------------------------------
                    # definiramo FORM za vnos stavb
                    delstavbe_prostor_create_form = delstavbe_forms.DelCreateForm(delstavbe_prostor_data)
                    if delstavbe_prostor_create_form.is_valid():
                        # shranimo podakte
                        delstavbe_prostor_instance = delstavbe_prostor_create_form.save()
                        # število dodanih vnosov povečamo za 1
                        prostori_records_added += 1
                        print("Prostor '%s' je bil dodan" % (delstavbe_prostor_data['oznaka']))


                        # IZDELAMO LOKACIJO
                        # -------------------------------------------------------

                        # 'prostor',
                        # 'etaza', 
                        
                        # pridobimo instanco prostora
                        prostor = delstavbe_prostor_instance
                        prostor_id = prostor.id

                        # pridobimo instanco etaže
                        etaza = Etaza.objects.get(oznaka=etaza_oznaka)
                        etaza_id = etaza.pk

                        lokacija_data = {
                            'prostor': prostor_id,
                            'etaza': etaza_id,
                        }

                        # definiramo FORM za vnos
                        lokacija_create_form = deli_lokacija_forms.LokacijaCreateForm(lokacija_data)

                        # če je FORM pravilno izpolnjen shranimo podatke
                        if lokacija_create_form.is_valid():
                            # shranimo podakte
                            lokacija_instance = lokacija_create_form.save()
                            # število dodanih vnosov povečamo za 1
                            lokacije_records_added += 1
                            print("Lokacija '%s' je bila vnešena" % (Lokacija.objects.get(prostor=lokacija_data['prostor'])))


                            # IZDELAMO PROJEKTNA MESTA PROSTORA (TLAK, STROP, STENE, EL-OPREMA)
                            # -------------------------------------------------------

                            ##############################################################################################
                            # PROJEKTNA MESTA ZA PROSTORE (TLAK, STENE, STROP, RAZSVETLJAVA, VTIČNICE IN STIKALA)
                            #---------------------------------------------------------------------------------------------
                            
                            # PR-TLAK_Tlak prostora
                            # PR-STENA_Stena prostora
                            # PR-STROP_Strop prostora
                            # PR-EL-OPR_Vtičnice, stikala in razsvetljava

                            # TLAK
                            projektno_mesto_inst = "TLAK"
                            projektno_mesto_inst_naziv = "Tlak prostora"
                            projektno_mesto_inst_funkcija = "NA"

                            tip_artikla_oznaka = "PR-" + projektno_mesto_inst
                            tip_elementa = TipArtikla.objects.get(oznaka=tip_artikla_oznaka)

                            oznaka = delstavbe_prostor_oznaka + "-" + projektno_mesto_inst
                            naziv = projektno_mesto_inst_naziv
                            funkcija = projektno_mesto_inst_funkcija

                            # zaporedna številka vnešenih projektnih mest pod prostor
                            st_pm = ProjektnoMesto.objects.filter(del_stavbe__bim_id=delstavbe_prostor_bim_id).count()
                            nova_zap_st_pm = st_pm + 1
                            nova_zap_st_pm = str(nova_zap_st_pm)
                            bim_id = delstavbe_prostor_bim_id + '-EDA5-' + nova_zap_st_pm

                            projektnomesto_tlak = ProjektnoMesto.objects.create_projektno_mesto(
                                oznaka=oznaka,
                                naziv=naziv,
                                funkcija=funkcija,
                                bim_id=bim_id,
                                tip_elementa=tip_elementa,
                                lokacija=lokacija_instance,
                                del_stavbe=delstavbe_prostor_instance
                                )
                            projektnamesta_records_added += 1

                            # STENE
                            projektno_mesto_inst = "STENA"
                            projektno_mesto_inst_naziv = "Stene prostora"
                            projektno_mesto_inst_funkcija = "NA"

                            tip_artikla_oznaka = "PR-" + projektno_mesto_inst
                            tip_elementa = TipArtikla.objects.get(oznaka=tip_artikla_oznaka)

                            oznaka = delstavbe_prostor_oznaka + "-" + projektno_mesto_inst
                            naziv = projektno_mesto_inst_naziv
                            funkcija = projektno_mesto_inst_funkcija

                            # zaporedna številka vnešenih projektnih mest pod prostor
                            st_pm = ProjektnoMesto.objects.filter(del_stavbe__bim_id=delstavbe_prostor_bim_id).count()
                            nova_zap_st_pm = st_pm + 1
                            nova_zap_st_pm = str(nova_zap_st_pm)
                            bim_id = delstavbe_prostor_bim_id + '-EDA5-' + nova_zap_st_pm

                            projektnomesto_tlak = ProjektnoMesto.objects.create_projektno_mesto(
                                oznaka=oznaka,
                                naziv=naziv,
                                funkcija=funkcija,
                                bim_id=bim_id,
                                tip_elementa=tip_elementa,
                                lokacija=lokacija_instance,
                                del_stavbe=delstavbe_prostor_instance
                                )
                            projektnamesta_records_added += 1


                            # STROP
                            projektno_mesto_inst = "STROP"
                            projektno_mesto_inst_naziv = "Strop prostora"
                            projektno_mesto_inst_funkcija = "NA"

                            tip_artikla_oznaka = "PR-" + projektno_mesto_inst
                            tip_elementa = TipArtikla.objects.get(oznaka=tip_artikla_oznaka)

                            oznaka = delstavbe_prostor_oznaka + "-" + projektno_mesto_inst
                            naziv = projektno_mesto_inst_naziv
                            funkcija = projektno_mesto_inst_funkcija

                            # zaporedna številka vnešenih projektnih mest pod prostor
                            st_pm = ProjektnoMesto.objects.filter(del_stavbe__bim_id=delstavbe_prostor_bim_id).count()
                            nova_zap_st_pm = st_pm + 1
                            nova_zap_st_pm = str(nova_zap_st_pm)
                            bim_id = delstavbe_prostor_bim_id + '-EDA5-' + nova_zap_st_pm

                            projektnomesto_tlak = ProjektnoMesto.objects.create_projektno_mesto(
                                oznaka=oznaka,
                                naziv=naziv,
                                funkcija=funkcija,
                                bim_id=bim_id,
                                tip_elementa=tip_elementa,
                                lokacija=lokacija_instance,
                                del_stavbe=delstavbe_prostor_instance
                                )
                            projektnamesta_records_added += 1


                            # EL OPREMA - VTIČNICE - STIKALA - RAZSVETLJAVA
                            projektno_mesto_inst = "EL"
                            projektno_mesto_inst_naziv = "Vtičnice, stikala in razsvetljava prostora"
                            projektno_mesto_inst_funkcija = "Upravljanje z razsvetljavo in električni priklop za vzdrževanje prostorov"

                            tip_artikla_oznaka = "PR-" + projektno_mesto_inst
                            tip_elementa = TipArtikla.objects.get(oznaka=tip_artikla_oznaka)

                            oznaka = delstavbe_prostor_oznaka + "-" + projektno_mesto_inst
                            naziv = projektno_mesto_inst_naziv
                            funkcija = projektno_mesto_inst_funkcija

                            # zaporedna številka vnešenih projektnih mest pod prostor
                            st_pm = ProjektnoMesto.objects.filter(del_stavbe__bim_id=delstavbe_prostor_bim_id).count()
                            nova_zap_st_pm = st_pm + 1
                            nova_zap_st_pm = str(nova_zap_st_pm)
                            bim_id = delstavbe_prostor_bim_id + '-EDA5-' + nova_zap_st_pm

                            projektnomesto_tlak = ProjektnoMesto.objects.create_projektno_mesto(
                                oznaka=oznaka,
                                naziv=naziv,
                                funkcija=funkcija,
                                bim_id=bim_id,
                                tip_elementa=tip_elementa,
                                lokacija=lokacija_instance,
                                del_stavbe=delstavbe_prostor_instance
                                )
                            projektnamesta_records_added += 1


                    else:
                        errors.append(delstavbe_prostor_create_form.errors)
                        print(errors)


                
                # UPDATE
                # ------------------------------------------------------------
                
                else:
                    # p1.__dict__.update(mydatadict)
                    # p1.save()
                    # pridobimo instanco Dela stavbe - prostor
                    instance = DelStavbe.objects.get(bim_id=delstavbe_prostor_bim_id)
                    # posodobimo podatke
                    instance.oznaka = delstavbe_prostor_data['oznaka']
                    instance.naziv = delstavbe_prostor_data['naziv']
                    instance.funkcija = delstavbe_prostor_data['funkcija']
                    instance.podskupina = delstavbe_prostor_data['podskupina_object']
                    # shranimo spremembe
                    instance.save()

                    # števec vnosov povečamo za 1
                    prostori_records_updated += 1
                    print("Prostor '%s' je bil posodobljen" % (delstavbe_prostor_data['oznaka']))





            ''' izbrišemo temp direktorij '''
            shutil.rmtree("/home/%s/temp" % (linux_user))

            return messages.success(request, "STAVBE:%s, ETAŽE:%s, PROSTORI:%s, LOKACIJA:%s, PROJEKTNA MESTA:%s" % (stavbe_records_added, etaze_records_added, prostori_records_added, lokacije_records_added, projektnamesta_records_added))






























########################################################################################
# 
#---------------------------------------------------------------------------------------




        if csv_file_path_form.is_valid():

            csv_file = csv_file_path_form.cleaned_data['csv_file_path']

            if lokacije_uvoz_form.is_valid():


                #--------------------------------------
                # RAZLIČNI MODULI
                #--------------------------------------


                # STAVBA, ETAŽE, PROSTORI
                del01_prostori = lokacije_uvoz_form.cleaned_data['del01_prostori']
                if del01_prostori is True:
                    import_del01_prostori(csv_file)
                    return HttpResponseRedirect(reverse('moduli:home'))

            if deli_uvoz_form.is_valid():

                #--------------------------------------
                # RAZLIČNI MODULI
                #--------------------------------------

                # STAVBA, ETAŽE, PROSTORI
                del02_ostali_deli_stavbe = deli_uvoz_form.cleaned_data['del02_ostali_deli_stavbe']
                if del02_ostali_deli_stavbe is True:
                    import_del02_ostali_deli_stavbe(csv_file)
                    return HttpResponseRedirect(reverse('moduli:home'))




