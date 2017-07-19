# PYTHON ##############################################################
from datetime import datetime, timedelta
import os


# DJANGO ##############################################################
from django.conf import settings
from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import TemplateView, ListView, DetailView, UpdateView


# UVOZI ZNOTRAJ APLIKACIJE ############################################
from ..forms import DeloCreateForm, DeloUpdateForm, DeloKoncajUpdateForm

from ..models import Delo, DelovniNalog

from ..mixins import MessagesActionMixin


# UVOZI ZUNANJIH APLIKAIJ ############################################

# Moduli
from eda5.moduli.models import Zavihek


class DeloCreateFromDelovniNalogView(MessagesActionMixin, UpdateView):
    model = DelovniNalog
    template_name = "delovninalogi/delo/create_from_delovninalog.html"
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):
        context = super(DeloCreateFromDelovniNalogView, self).get_context_data(*args, **kwargs)

        # opravilo
        context['delo_create_form'] = DeloCreateForm
        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="DN_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context


    def post(self, request, *args, **kwargs):

        # Delovni nalog s katerim imamo opravka (instanca)
        delovninalog = DelovniNalog.objects.get(id=self.get_object().id)

        # FORMS
        delo_create_form = DeloCreateForm(request.POST or None)

        delo_create_form_is_valid = False


        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="DN_DETAIL")


        if delo_create_form.is_valid():

            # PODATKI IZ FORMS*********************************************
            # pridobimo podatke iz DeloCreateForm
            oznaka = delo_create_form.cleaned_data['oznaka']
            naziv = delo_create_form.cleaned_data['naziv']
            vrsta_dela = delo_create_form.cleaned_data['vrsta_dela']
            delavec = delo_create_form.cleaned_data['delavec']
            datum = delo_create_form.cleaned_data['datum']
            time_start = delo_create_form.cleaned_data['time_start']
            delo_create_form_is_valid = True

            

        if delo_create_form_is_valid == True:

            # VNOS V BAZO **************************************************


            # VALIDACIJE **************************************************
            # validacija_01
            # Delovnim nalogom "V ČAKANJU" ni mogoče dodajati del
            if delovninalog.status == 1:
                # sporočilo uporabniku
                messages.error(request, 'Delovnim nalogom "V ČAKANJU" ni mogoče dodajati del. Najprej je potrebno delo planirati.')
                # preusmeritev na obstoječi delovni nalog brez vnosa
                return HttpResponseRedirect(reverse('moduli:delovninalogi:dn_detail', kwargs={'pk': delovninalog.pk}))

            # validacija_02
            # pred vnosom novega dela NOSILEC ali DELAVEC ne sme imeti odprtih del. 
            # Istočasno ni mogoče opravljati več del
            for delo in Delo.objects.filter(time_stop__isnull=True):
                # preverimo, če ima željeni delavec, ki delo odpira že odprto drugo delo
                # v nedokončanih delih.
                if delo.delavec.id == delavec.id:
                    # sporočilo uporabniku
                    messages.error(request, "Končati je potrebno predhodno delo v delovnem nalogu z oznako '%s'"
                                   % (delo.delovninalog.oznaka))
                    # preusmerimo na obstoječi delovni nalog
                    return HttpResponseRedirect(reverse('moduli:delovninalogi:dn_detail', kwargs={'pk': delovninalog.pk}))

            # validacija_03
            # Zaključenim delovnim nalogom ni mogoče dodajati novih del.
            if delovninalog.status == 4:
                # sporočilo uporabniku
                messages.error(request, "Delovni nalog je že zaključen! Novih del ni mogoče vnašati.")
                # preusmeritev na obstoječi delovni nalog
                return HttpResponseRedirect(reverse('moduli:delovninalogi:dn_detail', kwargs={'pk': delovninalog.pk}))


            # Izdelamo delo
            delo = Delo.objects.create_delo(
                oznaka=oznaka,
                naziv=naziv,
                delavec=delavec,
                datum=datum,
                vrsta_dela=vrsta_dela,
                time_start=time_start,
                delovninalog=delovninalog,
            )

            # Spremenimo status delovnega naloga na = "v reševanju"
            # pridobimo delovninalog glede na trenutno izdelano delo
            delovninalog = DelovniNalog.objects.get(id=delo.delovninalog.pk)
            # spremenimo status delovnega naloga
            # če status že ni spremenjen
            if not delovninalog.status == 3:
                delovninalog.status = 3
                delovninalog.datum_start = timezone.now().date()
                # shranimo v bazo
                delovninalog.save()


            # ob izdelavi dela sporočimo uporabniku
            messages.success(request, 'Novo delo je začeto.')

            # ter izvedemo preusmeritev na obstoječi delovni nalog
            return HttpResponseRedirect(reverse('moduli:delovninalogi:dn_detail', kwargs={'pk': delovninalog.pk}))

        else:
        # v primeru, da so zgornji Form-i NISO ustrezno izpolnjeni
        # izvrši spodnje ukaze


            return render(request, self.template_name, {
                'delo_create_form': delo_create_form,
                'modul_zavihek': modul_zavihek,
                }
            )


class DeloKoncajUpdateView(MessagesActionMixin, UpdateView):
    model = Delo
    form_class = DeloKoncajUpdateForm
    template_name = "delovninalogi/delo/update_delo_koncaj.html"

    success_msg = "Delo je uspešno končano."

    def get_context_data(self, *args, **kwargs):
        context = super(DeloKoncajUpdateView, self).get_context_data(*args, **kwargs)

        # Zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="DN_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context


class DeloUpdateView(MessagesActionMixin, UpdateView):
    model = Delo
    form_class = DeloUpdateForm
    template_name = "delovninalogi/delo/update_from_delovninalog.html"
    success_msg = "Delo je uspešno posodobljeno."

    def get_context_data(self, *args, **kwargs):
        context = super(DeloUpdateView, self).get_context_data(*args, **kwargs)

        # Zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="DN_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context
