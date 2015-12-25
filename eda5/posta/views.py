from django.shortcuts import render
from django.db.models import Max

import os

from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, ListView, TemplateView

from .forms import AktivnostCreateForm, DokumentCreateForm
from .models import Aktivnost, Dokument

from eda5.arhiv.forms import ArhiviranjeCreateForm
from eda5.arhiv.models import Arhiviranje, ArhivMesto, Arhiv

from eda5.moduli.models import Zavihek


class PostaHomeView(TemplateView):
    template_name = "posta/home.html"


class DokumentListView(ListView):
    model = Dokument
    template_name = "posta/dokument/list/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DokumentListView, self).get_context_data(*args, **kwargs)

        # dokumentacija za arhiviranje
        za_arhiviranje_list = Dokument.objects.filter(arhiviranje__isnull=True)
        context['za_arhiviranje_list'] = za_arhiviranje_list

        # arhivirana dokumentacija
        arhivirano_list = Dokument.objects.filter(arhiviranje__isnull=False)
        context['arhivirano_list'] = arhivirano_list

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="DOKUMENT_LIST")
        context['modul_zavihek'] = modul_zavihek

        return context


class PostaDokumentDetailView(DetailView):

    model = Dokument
    template_name = 'posta/dokument/detail/base.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostaDokumentDetailView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="DOKUMENT_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context


class DokumentCreateView(TemplateView):
    template_name = "posta/dokument/create.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DokumentCreateView, self).get_context_data(*args, **kwargs)
        context['aktivnost_form'] = AktivnostCreateForm
        context['dokument_form'] = DokumentCreateForm

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="DOKUMENT_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        aktivnost_form = AktivnostCreateForm(request.POST or None)
        dokument_form = DokumentCreateForm(request.POST or None, request.FILES)
        modul_zavihek = Zavihek.objects.get(oznaka="DOKUMENT_CREATE")

        if aktivnost_form.is_valid():

            izvajalec = aktivnost_form.cleaned_data['izvajalec']
            likvidiral = aktivnost_form.cleaned_data['likvidiral']
            vrsta_aktivnosti = aktivnost_form.cleaned_data['vrsta_aktivnosti']
            datum_aktivnosti = aktivnost_form.cleaned_data['datum_aktivnosti']

            aktivnost_create_data = Aktivnost.objects.create_aktivnost(
                izvajalec=izvajalec,
                likvidiral=likvidiral,
                vrsta_aktivnosti=vrsta_aktivnosti,
                datum_aktivnosti=datum_aktivnosti,
            )

            aktivnost = Aktivnost.objects.get(id=aktivnost_create_data.pk)

        else:
            return render(request, self.template_name, {
                'aktivnost_form': aktivnost_form,
                'dokument_form': dokument_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        if dokument_form.is_valid():

            vrsta_dokumenta = dokument_form.cleaned_data['vrsta_dokumenta']
            avtor = dokument_form.cleaned_data['avtor']
            naslovnik = dokument_form.cleaned_data['naslovnik']
            oznaka = dokument_form.cleaned_data['oznaka']
            naziv = dokument_form.cleaned_data['naziv']
            datum_dokumenta = dokument_form.cleaned_data['datum_dokumenta']
            priponka = dokument_form.cleaned_data['priponka']

            # oznaka_baza
            max_oznaka_baza = Dokument.objects.all().aggregate(Max('oznaka_baza'))['oznaka_baza__max']
            max_dokument = Dokument.objects.get(oznaka_baza=max_oznaka_baza)

            nova_oznaka_baza = max_dokument.oznaka_baza + 1
            oznaka_baza = nova_oznaka_baza

            Dokument.objects.create_dokument(
                vrsta_dokumenta=vrsta_dokumenta,
                avtor=avtor,
                naslovnik=naslovnik,
                oznaka_baza=oznaka_baza,
                oznaka=oznaka,
                naziv=naziv,
                datum_dokumenta=datum_dokumenta,
                priponka=priponka,
                aktivnost=aktivnost,
            )

        else:
            return render(request, self.template_name, {
                'aktivnost_form': aktivnost_form,
                'dokument_form': dokument_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        return HttpResponseRedirect(reverse('moduli:posta:dokument_list'))