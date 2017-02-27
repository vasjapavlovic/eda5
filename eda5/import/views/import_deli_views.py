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
    import_deli_forms

# Deli FORMS
from eda5.deli.forms import \
    skupina_forms,\
    podskupina_forms, \
    projektnomesto_forms, \
    deli_lokacija_forms

# Deli MODELS
from eda5.deli.models import \
    Skupina, \
    Podskupina, \
    DelStavbe, \
    Lokacija

# Katalog MODELS
from eda5.katalog.models import \
    TipArtikla

# Moduli
from eda5.moduli.models import Zavihek




class DeliUvozPodatkovView(TemplateView):
    template_name = "deli/uvozpodatkov/uvoz_podatkov_create.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DeliUvozPodatkovView, self).get_context_data(*args, **kwargs)

        # Deli
        context['csv_file_path_form'] = import_common_forms.CsvFilePath
        context['deli_uvoz_form'] = import_deli_forms.DeliUvozCsvForm
        context['projektnomesto_create_form'] = projektnomesto_forms.ProjektnoMestoCreateForm

        # Zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):
        csv_file_path_form = import_common_forms.CsvFilePath(request.POST or None, request.FILES)
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


        def import_deli_skupine(csv_file):

            seznam, linux_user = get_file_data(csv_file)

            records_added = 0
            for row in seznam:
                form = skupina_forms.SkupinaCreateForm(row)
                if form.is_valid():
                    form.save()
                    records_added += 1


            ''' izbrišemo temp direktorij '''
            shutil.rmtree("/home/%s/temp" % (linux_user))

            return messages.success(request, "SKUPINE DELOV STAVBE: Število dodanih vnosov: %s" % (records_added))


        def import_deli_podskupine(csv_file):

            seznam, linux_user = get_file_data(csv_file)
            ''' Prebrane podatke shranimo v bazo'''

            records_added = 0
            for row in seznam:
                skupina_oznaka = row['skupina']
                try:
                    skupina = Skupina.objects.get(oznaka=skupina_oznaka)
                    row['skupina'] = skupina.pk
                    form = podskupina_forms.PodskupinaCreateForm(row)

                    if form.is_valid():
                        form.save()
                        records_added += 1

                except:
                    return messages.error(request, "NEKAJ JE BILO NAROBE")


            ''' izbrišemo temp direktorij '''
            shutil.rmtree("/home/%s/temp" % (linux_user))

            return messages.success(request, "SKUPINE DELOV STAVBE: Število dodanih vnosov: %s" % (records_added))





        def import_del02_ostali_deli_stavbe(csv_file):

            ''' Preberemo podatke iz datoteke .csv '''

            seznam, linux_user = get_file_data(csv_file)
            

            deli_stavbe_records_added = 0
            projektno_mesto_records_added = 0


            for row in seznam:



                # default vrednost shranimo v parametre za nadaljno uporabo
                stavba_oznaka = row['stavba']

                projektnomesto_oznaka = row['oznaka']
                projektnomesto_tip_elementa = row['tip_elementa']
                projektnomesto_bim_id = row['bim_id']
                klasifikacija = row['klasifikacija']
                projektnomesto_lokacija = row['lokacija']

                # skupina, podskupina, delstavbe se pridobi iz klasifikacije
                # npr. A_AA_AA01_Naziv
                eda5, skupina_oznaka, podskupina_oznaka, delstavbe_oznaka, ostanek = klasifikacija.split("_", 4)
                # še naziv dela stavbe
                delstavbe_naziv, ostanek2 = ostanek.split(".", 1)


                # pridobimo ločene podatke o tipu artikla
                tip_artikla_oznaka, tip_artikla_naziv = projektnomesto_tip_elementa.split("_", 1)



                ##############################################################################################
                # DEL STAVBE
                #---------------------------------------------------------------------------------------------
                
                # Atributi

                    # pridobimo osnovne atribute za vnos
                    # 'oznaka',
                    # 'naziv', 
                    # 'funkcija', 
                    # 'bim_id',
                    # 'podskupina',

                # pridobimo instanco podskupine dela stavbe
                podskupina = Podskupina.objects.get(oznaka=podskupina_oznaka)
                podskupina_id = podskupina.pk


                # preimenujemo atribute stavbe na seznamu
                row['oznaka'] = delstavbe_oznaka
                row['naziv'] = delstavbe_naziv
                row['bim_id'] = "NA"
                row['podskupina'] = podskupina_id

                # definiramo FORM za vnos stavb
                delstavbe_prostor_create_form = deli_lokacija_forms.DelStavbeProstorCreateForm(row)

                # če je FORM pravilno izpolnjen shranimo podatke
                if delstavbe_prostor_create_form.is_valid():
                    # shranimo podakte
                    delstavbe_prostor_create_form.save()
                    # število dodanih vnosov povečamo za 1
                    deli_stavbe_records_added += 1
                    print("DEL STAVBE JE BIL VNEŠEN")

                #---------------------------------------------------------------------------------------------
                # DEL STAVBE
                ##############################################################################################

                ##############################################################################################
                # PROJEKTNO MESTO
                #---------------------------------------------------------------------------------------------
                
                # Atributi

                    # 'oznaka',
                    # 'naziv',
                    # 'funkcija',
                    # 'bim_id',
                    # 'tip_elementa',
                    # 'lokacija',
                    # 'del_stavbe',

                
                delstavbe = DelStavbe.objects.get(oznaka=delstavbe_oznaka)
                delstavbe_id = delstavbe.pk


                tip_artikla = TipArtikla.objects.get(oznaka=tip_artikla_oznaka)
                tip_artikla_id = tip_artikla.pk


                # pridobimo instanco prostora
                lokacija = Lokacija.objects.get(prostor__oznaka=projektnomesto_lokacija)
                lokacija_id = lokacija.pk


                # preimenujemo atribute stavbe na seznamu
                row['oznaka'] = projektnomesto_oznaka
                row['naziv'] = "NA"
                row['bim_id'] = projektnomesto_bim_id
                row['tip_elementa'] = tip_artikla_id
                row['lokacija'] = lokacija_id
                row['del_stavbe'] = delstavbe_id

                # definiramo FORM za vnos
                projektnomesto_create_form = projektnomesto_forms.ProjektnoMestoCreateForm(row)

                # če je FORM pravilno izpolnjen shranimo podatke
                if projektnomesto_create_form.is_valid():
                    # shranimo podakte
                    projektnomesto_create_form.save()
                    # število dodanih vnosov povečamo za 1
                    projektno_mesto_records_added += 1
                    print("PROJEKTNO-MESTO JE BILO VNEŠENO")

                #---------------------------------------------------------------------------------------------
                # PROJEKTNO MESTO
                ##############################################################################################





            ''' izbrišemo temp direktorij '''
            shutil.rmtree("/home/%s/temp" % (linux_user))

            return messages.success(request, "DELI STAVBE:%s, PROJEKTNA MESTA:%s" % (deli_stavbe_records_added, projektno_mesto_records_added))
























        if csv_file_path_form.is_valid():

            csv_file = csv_file_path_form.cleaned_data['csv_file_path']

            if deli_uvoz_form.is_valid():


                #--------------------------------------
                # RAZLIČNI MODULI
                #--------------------------------------


                # SKUPINE DELOV
                skupine_delov_stavbe = deli_uvoz_form.cleaned_data['skupine_delov_stavbe']
                if skupine_delov_stavbe is True:
                    import_deli_skupine(csv_file)
                    return HttpResponseRedirect(reverse('moduli:deli:del_list'))


                # PODSKUPINE DELOV
                podskupine_delov_stavbe = deli_uvoz_form.cleaned_data['podskupine_delov_stavbe']
                if podskupine_delov_stavbe is True:
                    import_deli_podskupine(csv_file)
                    return HttpResponseRedirect(reverse('moduli:deli:del_list'))


                # PODSKUPINE DELOV
                del02_ostali_deli_stavbe = deli_uvoz_form.cleaned_data['del02_ostali_deli_stavbe']
                if del02_ostali_deli_stavbe is True:
                    import_del02_ostali_deli_stavbe(csv_file)
                    return HttpResponseRedirect(reverse('moduli:deli:del_list'))


