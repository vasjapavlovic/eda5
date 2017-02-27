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


# Deli FORMS
from eda5.deli.forms import \
    deli_uvozpodatkov_forms, \
    skupina_forms,\
    podskupina_forms

# Deli MODELS
from eda5.deli.models import \
    Skupina

# Moduli
from eda5.moduli.models import Zavihek


class DeliUvozPodatkovView(TemplateView):
    template_name = "deli/uvozpodatkov/uvoz_podatkov_create.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DeliUvozPodatkovView, self).get_context_data(*args, **kwargs)

        # Deli
        context['csv_file_path_form'] = deli_uvozpodatkov_forms.CsvFilePath
        context['deli_uvoz_form'] = deli_uvozpodatkov_forms.DeliUvozCsvForm

        # Zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):
        csv_file_path_form = deli_uvozpodatkov_forms.CsvFilePath(request.POST or None, request.FILES)
        deli_uvoz_form = deli_uvozpodatkov_forms.DeliUvozCsvForm(request.POST or None)


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
                podskupine_delov_stavbe = deli_uvoz_form.cleaned_data['podskupine_delov_stavbe']
                if podskupine_delov_stavbe is True:
                    import_deli_podskupine(csv_file)
                    return HttpResponseRedirect(reverse('moduli:deli:del_list'))


