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
            


            stavbe_records_added = 0
            etaze_records_added = 0
            prostori_records_added = 0
            lokacije_records_added = 0
            projektnamesta_records_added = 0

            for row in seznam:

                # default vrednost shranimo v parametre za nadaljno uporabo
                delstavbe_oznaka = row['oznaka']
                delstavbe_naziv = row['naziv']
                delstavbe_bim_id = row['bim_id']
                stavba_oznaka = row['stavba']
                etaza_oznaka = row['etaza']
                etaza_elevation = row['elevation']
                delstavbe_klasifikacija = row['klasifikacija']

                # pridobimo ločene podatke klasifikacije
                eda5, skupina_oznaka, podskupina_oznaka, delstavbe_prostor_oznaka, ostanek = delstavbe_klasifikacija.split("_", 4)


                # try:

                ##############################################################################################
                # STAVBE
                #---------------------------------------------------------------------------------------------

                # Atributi

                    # 'oznaka',
                    # 'naziv', 
                    # 'opis', 

                # preimenujemo atribute stavbe na seznamu
                row['oznaka'] = stavba_oznaka
                row['naziv'] = "NA"
                row['opis'] = "NA"

                # definiramo FORM za vnos stavb
                stavba_create_form = deli_lokacija_forms.StavbaCreateForm(row)


                # če je FORM pravilno izpolnjen shranimo podatke
                if stavba_create_form.is_valid():
                    # shranimo podakte
                    stavba_create_form.save()
                    # število dodanih vnosov povečamo za 1
                    stavbe_records_added += 1
                    print("STAVBA JE BILA VNESENA")

                #---------------------------------------------------------------------------------------------
                # STAVBE
                ##############################################################################################



                ##############################################################################################
                # ETAŽE
                #---------------------------------------------------------------------------------------------
                # Atributi

                    # 'oznaka',
                    # 'naziv', 
                    # 'opis',
                    # 'elevation',
                    # 'stavba',


                # pridobimo relacije za vnos
                stavba = Stavba.objects.get(oznaka=stavba_oznaka)
                stavba_id = stavba.pk

                # preimenujemo atribute na seznamu
                row['oznaka'] = etaza_oznaka
                row['naziv'] = "NA"
                row['elevation'] = etaza_elevation
                row['stavba'] = stavba_id


                # definiramo FORM za vnos stavb
                etaza_create_form = deli_lokacija_forms.EtazaCreateForm(row)


                # če je FORM pravilno izpolnjen shranimo podatke
                if etaza_create_form.is_valid():
                    # shranimo podakte
                    etaza_create_form.save()
                    # število dodanih vnosov povečamo za 1
                    etaze_records_added += 1
                    print("ETAŽA JE BILA VNESENA")

                #---------------------------------------------------------------------------------------------
                # ETAŽE
                ##############################################################################################




                ##############################################################################################
                # PROSTORI
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


                
                # pridobimo instanco podskupine dela stavbe
                podskupina = Podskupina.objects.get(oznaka=podskupina_oznaka)
                podskupina_id = podskupina.pk


                # preimenujemo atribute stavbe na seznamu
                row['oznaka'] = delstavbe_oznaka
                row['naziv'] = delstavbe_naziv
                row['bim_id'] = delstavbe_bim_id
                row['podskupina'] = podskupina_id

                # definiramo FORM za vnos stavb
                delstavbe_prostor_create_form = deli_lokacija_forms.DelStavbeProstorCreateForm(row)

                # če je FORM pravilno izpolnjen shranimo podatke
                if delstavbe_prostor_create_form.is_valid():
                    # shranimo podakte
                    delstavbe_instance = delstavbe_prostor_create_form.save() 
                    # število dodanih vnosov povečamo za 1
                    prostori_records_added += 1
                    print("PROSTOR JE BIL VNEŠEN")

                #---------------------------------------------------------------------------------------------
                # PROSTORI
                ##############################################################################################




                ##############################################################################################
                # LOKACIJA
                #---------------------------------------------------------------------------------------------
                
                # Atributi

                    # pridobimo osnovne atribute za vnos
                    # 'oznaka',
                    # 'tip_artikla', 
                    # 'lokacija',
                    # ''

                
                # pridobimo instanco prostora
                prostor = DelStavbe.objects.get(oznaka=delstavbe_oznaka)
                prostor_id = prostor.pk

                # pridobimo instanco etaže
                etaza = Etaza.objects.get(oznaka=etaza_oznaka)
                etaza_id = etaza.pk

                # preimenujemo atribute stavbe na seznamu
                row['prostor'] = prostor_id
                row['etaza'] = etaza_id


                # definiramo FORM za vnos
                lokacija_create_form = deli_lokacija_forms.LokacijaCreateForm(row)

                # če je FORM pravilno izpolnjen shranimo podatke
                if lokacija_create_form.is_valid():
                    # shranimo podakte
                    lokacija_instance = lokacija_create_form.save()
                    # število dodanih vnosov povečamo za 1
                    lokacije_records_added += 1
                    print("LOKACIJA JE BILA VNEŠENA")

                #---------------------------------------------------------------------------------------------
                # LOKACIJA
                ##############################################################################################

                ##############################################################################################
                # PROJEKTNA MESTA ZA PROSTORE (TLAK, STENE, STROP, RAZSVETLJAVA, VTIČNICE IN STIKALA)
                #---------------------------------------------------------------------------------------------
                
                # LUX_Razsvetljava prostorov
                # PR-TLAK_Tlak prostora
                # PR-STENA_Stena prostora
                # PR-STROP_Strop prostora
                # PR-EL-OPR_Vtičnice in stikala

                # TLAK
                projektno_mesto_inst = "TLAK"
                projektno_mesto_inst_naziv = "Tlak prostora"
                projektno_mesto_inst_funkcija = "NA"

                tip_artikla_oznaka = "PR-" + projektno_mesto_inst
                tip_elementa = TipArtikla.objects.get(oznaka=tip_artikla_oznaka)

                oznaka = delstavbe_oznaka + "-" + projektno_mesto_inst
                naziv = projektno_mesto_inst_naziv
                funkcija = projektno_mesto_inst_funkcija

                projektnomesto_tlak = ProjektnoMesto.objects.create_projektno_mesto(
                    oznaka=oznaka,
                    naziv=naziv,
                    funkcija=funkcija,
                    bim_id="NA",
                    tip_elementa=tip_elementa,
                    lokacija=lokacija_instance,
                    del_stavbe=delstavbe_instance
                    )
                projektnamesta_records_added += 1

                # TLAK
                projektno_mesto_inst = "STENA"
                projektno_mesto_inst_naziv = "Stene prostora"
                projektno_mesto_inst_funkcija = "NA"

                tip_artikla_oznaka = "PR-" + projektno_mesto_inst
                tip_elementa = TipArtikla.objects.get(oznaka=tip_artikla_oznaka)

                oznaka = delstavbe_oznaka + "-" + projektno_mesto_inst
                naziv = projektno_mesto_inst_naziv
                funkcija = projektno_mesto_inst_funkcija

                projektnomesto_tlak = ProjektnoMesto.objects.create_projektno_mesto(
                    oznaka=oznaka,
                    naziv=naziv,
                    funkcija=funkcija,
                    bim_id="NA",
                    tip_elementa=tip_elementa,
                    lokacija=lokacija_instance,
                    del_stavbe=delstavbe_instance
                    )
                projektnamesta_records_added += 1


                # STROP
                projektno_mesto_inst = "STROP"
                projektno_mesto_inst_naziv = "Strop prostora"
                projektno_mesto_inst_funkcija = "NA"

                tip_artikla_oznaka = "PR-" + projektno_mesto_inst
                tip_elementa = TipArtikla.objects.get(oznaka=tip_artikla_oznaka)

                oznaka = delstavbe_oznaka + "-" + projektno_mesto_inst
                naziv = projektno_mesto_inst_naziv
                funkcija = projektno_mesto_inst_funkcija

                projektnomesto_tlak = ProjektnoMesto.objects.create_projektno_mesto(
                    oznaka=oznaka,
                    naziv=naziv,
                    funkcija=funkcija,
                    bim_id="NA",
                    tip_elementa=tip_elementa,
                    lokacija=lokacija_instance,
                    del_stavbe=delstavbe_instance
                    )
                projektnamesta_records_added += 1


                # RAZSVETLJAVA
                projektno_mesto_inst = "LUX"
                projektno_mesto_inst_naziv = "Razsvetljava prostora"
                projektno_mesto_inst_funkcija = "NA"

                tip_artikla_oznaka = projektno_mesto_inst
                tip_elementa = TipArtikla.objects.get(oznaka=tip_artikla_oznaka)

                oznaka = delstavbe_oznaka + "-" + projektno_mesto_inst
                naziv = projektno_mesto_inst_naziv
                funkcija = projektno_mesto_inst_funkcija

                projektnomesto_tlak = ProjektnoMesto.objects.create_projektno_mesto(
                    oznaka=oznaka,
                    naziv=naziv,
                    funkcija=funkcija,
                    bim_id="NA",
                    tip_elementa=tip_elementa,
                    lokacija=lokacija_instance,
                    del_stavbe=delstavbe_instance
                    )
                projektnamesta_records_added += 1


                # EL OPREMA - VTIČNICE - STIKALA
                projektno_mesto_inst = "EL-OPR"
                projektno_mesto_inst_naziv = "Vtičnice in stikala prostora"
                projektno_mesto_inst_funkcija = "Upravljanje z razsvetljavo in električni priklop za vzdrževanje prostorov"

                tip_artikla_oznaka = "PR-" + projektno_mesto_inst
                tip_elementa = TipArtikla.objects.get(oznaka=tip_artikla_oznaka)

                oznaka = delstavbe_oznaka + "-" + projektno_mesto_inst
                naziv = projektno_mesto_inst_naziv
                funkcija = projektno_mesto_inst_funkcija

                projektnomesto_tlak = ProjektnoMesto.objects.create_projektno_mesto(
                    oznaka=oznaka,
                    naziv=naziv,
                    funkcija=funkcija,
                    bim_id="NA",
                    tip_elementa=tip_elementa,
                    lokacija=lokacija_instance,
                    del_stavbe=delstavbe_instance
                    )

                projektnamesta_records_added += 1
                print("DODANA SO BILA PROJEKTNA MESTA PROSTORA")

                # Atributi

                    # 'oznaka',
                    # 'naziv',
                    # 'funkcija',
                    # 'bim_id',
                    # 'tip_elementa',
                    # 'lokacija',
                    # 'del_stavbe',

                
                # delstavbe = DelStavbe.objects.get(oznaka=delstavbe_oznaka)
                # delstavbe_id = delstavbe.pk


                # tip_artikla = TipArtikla.objects.get(oznaka=tip_artikla_oznaka)
                # tip_artikla_id = tip_artikla.pk


                # # pridobimo instanco prostora
                # lokacija = Lokacija.objects.get(prostor__oznaka=projektnomesto_lokacija)
                # lokacija_id = lokacija.pk

                
                # # pridobimo instanco prostora
                # prostor = DelStavbe.objects.get(oznaka=delstavbe_oznaka)
                # prostor_id = prostor.pk

                # # pridobimo instanco etaže
                # etaza = Etaza.objects.get(oznaka=etaza_oznaka)
                # etaza_id = etaza.pk

                # preimenujemo atribute stavbe na seznamu
                # row['prostor'] = prostor_id
                # row['etaza'] = etaza_id


                # definiramo FORM za vnos
                # lokacija_create_form = deli_lokacija_forms.LokacijaCreateForm(row)

                # # če je FORM pravilno izpolnjen shranimo podatke
                # if lokacija_create_form.is_valid():
                #     # shranimo podakte
                #     lokacija_create_form.save()
                #     # število dodanih vnosov povečamo za 1
                #     lokacije_records_added += 1
                #     print("LOKACIJA JE BILA VNEŠENA")

                #---------------------------------------------------------------------------------------------
                # LOKACIJA
                ##############################################################################################


                # except:
                #     return messages.error(request, "NEKAJ JE BILO NAROBE")


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




