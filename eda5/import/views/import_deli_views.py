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
    deli_lokacija_forms, \
    delstavbe_forms

# Deli MODELS
from eda5.deli.models import \
    Skupina, \
    Podskupina, \
    DelStavbe, \
    Lokacija, \
    ProjektnoMesto  

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
        delstavbe_create_form = delstavbe_forms.DelCreateForm(request.POST or None)
        projektnomesto_create_form = projektnomesto_forms.ProjektnoMestoCreateForm(request.POST or None)
        
    

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
            

            # CREATED
            deli_stavbe_records_added = 0
            projektno_mesto_records_added = 0

            # UPDATED
            deli_stavbe_records_updated = 0
            projektno_mesto_records_updated = 0


            for row in seznam:

                ##############################################################################################
                # ATRIBUTI iz SEZNAMA
                #---------------------------------------------------------------------------------------------

                # Pridobimo atribute iz seznama
                projektnomesto_oznaka = row['oznaka']
                projektnomesto_naziv = row['naziv']
                projektnomesto_funkcija = row['funkcija']
                projektnomesto_tip_elementa = row['tip_elementa']
                projektnomesto_bim_id = row['bim_id']
                klasifikacija = row['klasifikacija']
                projektnomesto_prostor = row['prostor']
                stavba_oznaka = row['stavba']

                errors = []

                # klasifikacijo razdelimo na več atributov
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
                
                # 'oznaka',
                # 'naziv', 
                # 'funkcija', 
                # 'bim_id',
                # 'podskupina',

                delstavbe_oznaka = delstavbe_oznaka
                delstavbe_naziv = delstavbe_naziv
                delstavbe_funkcija = 'NA'
                delstavbe_bim_id = 'NA'
                delstavbe_podskupina_id = Podskupina.objects.get(oznaka=podskupina_oznaka).id

                delstavbe_data = {
                    'oznaka': delstavbe_oznaka,
                    'naziv': delstavbe_naziv,
                    'funkcija': delstavbe_funkcija,
                    'bim_id': delstavbe_bim_id,
                    'podskupina': delstavbe_podskupina_id,
                }
                
                # CREATE
                # ------------------------------------------------------------
                if not DelStavbe.objects.filter(oznaka=delstavbe_oznaka).exists():
                    
                    # definiramo FORM za vnos stavb
                    delstavbe_create_form = delstavbe_forms.DelCreateForm(delstavbe_data)
                    if delstavbe_create_form.is_valid():
                        # shranimo podakte
                        delstavbe_create_form.save()
                        # število dodanih vnosov povečamo za 1
                        deli_stavbe_records_added += 1
                        print("Del stavbe '%s' je bil dodan" % (delstavbe_data['oznaka']))

                    else:
                        errors.append(delstavbe_create_form.errors)
                        print(errors)


                ##############################################################################################
                # PROJEKTNO MESTO
                #---------------------------------------------------------------------------------------------

                # 'oznaka',
                # 'naziv',
                # 'funkcija',
                # 'bim_id',
                # 'tip_elementa',
                # 'lokacija',
                # 'del_stavbe',

                projektnomesto_oznaka = projektnomesto_oznaka
                projektnomesto_naziv = projektnomesto_naziv
                projektnomesto_funkcija = projektnomesto_funkcija
                projektnomesto_bim_id = projektnomesto_bim_id

                projektnomesto_tip_elementa = TipArtikla.objects.get(oznaka=tip_artikla_oznaka)
                projektnomesto_tip_elementa_id = projektnomesto_tip_elementa.id

                projektnomesto_lokacija = Lokacija.objects.get(prostor__oznaka=projektnomesto_prostor)
                projektnomesto_lokacija_id = projektnomesto_lokacija.id

                projektnomesto_del_stavbe = DelStavbe.objects.get(oznaka=delstavbe_oznaka)
                projektnomesto_del_stavbe_id = projektnomesto_del_stavbe.id

                projektnomesto_data = {
                    'oznaka': projektnomesto_oznaka,
                    'naziv': projektnomesto_naziv,
                    'funkcija': projektnomesto_funkcija,
                    'bim_id': projektnomesto_bim_id,
                    'tip_elementa': projektnomesto_tip_elementa_id,
                    'lokacija': projektnomesto_lokacija_id,
                    'del_stavbe': projektnomesto_del_stavbe_id,
                    'tip_elementa_object': projektnomesto_tip_elementa,
                    'lokacija_object': projektnomesto_lokacija,
                    'del_stavbe_object': projektnomesto_del_stavbe,
                }

                
                # CREATE
                # ------------------------------------------------------------
                # BIM_ID je unikaten
                if not ProjektnoMesto.objects.filter(bim_id=projektnomesto_bim_id).exists():
                    
                    # definiramo FORM za vnos stavb
                    projektnomesto_create_form = projektnomesto_forms.ProjektnoMestoCreateForm(projektnomesto_data)

                    if projektnomesto_create_form.is_valid():
                        # shranimo podakte
                        projektnomesto_create_form.save()
                        # število dodanih vnosov povečamo za 1
                        deli_stavbe_records_added += 1
                        print("Projektno mesto '%s' je bilo vnešeno" % (projektnomesto_data['oznaka']))

                    else:
                        # Če se pojavi napaka pri validaciji jo izpiši
                        errors.append(projektnomesto_create_form.errors)
                        print(errors)


                # UPDATE
                # ------------------------------------------------------------
                
                else:
                    # p1.__dict__.update(mydatadict)
                    # p1.save()
                    # pridobimo instanco Projektnega mesta
                    instance = ProjektnoMesto.objects.get(bim_id=projektnomesto_bim_id)
                    # posodobimo podatke
                    instance.oznaka = projektnomesto_data['oznaka']
                    instance.naziv = projektnomesto_data['naziv']
                    instance.funkcija = projektnomesto_data['funkcija']
                    instance.bim_id = projektnomesto_data['bim_id']
                    instance.tip_elementa = projektnomesto_data['tip_elementa_object']
                    instance.lokacija = projektnomesto_data['lokacija_object']
                    instance.del_stavbe = projektnomesto_data['del_stavbe_object']
                    # shranimo spremembe
                    instance.save()

                    # števec vnosov povečamo za 1
                    projektno_mesto_records_updated += 1
                    print("Projektno mesto '%s' je bilo posodobljeno" % (projektnomesto_data['oznaka']))



            ''' izbrišemo temp direktorij '''
            shutil.rmtree("/home/%s/temp" % (linux_user))

            return messages.success(
                request, 
                "DELI STAVBE: Created-%s|Updated-%s, PROJEKTNA MESTA: Created-%s|Updated-%s" % (
                    deli_stavbe_records_added, 
                    deli_stavbe_records_updated, 
                    projektno_mesto_records_added, 
                    projektno_mesto_records_updated
                )
            )





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


