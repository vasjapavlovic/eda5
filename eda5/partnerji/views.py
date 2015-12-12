import csv
import io
import os

from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView

from .forms import PartnerCreateForm, PartnerUpdateForm
from .forms import OsebaCreateForm, OsebaUpdateForm, OsebaCreateWidget, TrrCreateWidget, UvozPartnerjiCsvForm, PostaCreateForm

from .models import Partner, Oseba, TRRacun, Banka, Posta

# mixins
from .viewmixins import PartnerSearchMixin


class PartnerHomeView(TemplateView):
    template_name = "partnerji/home.html"


class PartnerListView(PartnerSearchMixin, ListView):
    model = Partner

    # order_by
    def get_queryset(self):
        queryset = super(PartnerListView, self).get_queryset()
        queryset = queryset.order_by('kratko_ime')
        return queryset


class PartnerDetailView(DetailView):
    model = Partner

    # subform "Dodaj Osebo"
    form_class = OsebaCreateWidget

    def get_context_data(self, *args, **kwargs):
        context = super(PartnerDetailView, self).get_context_data(*args, **kwargs)
        context['oseba_form'] = self.form_class
        context['trr_form'] = TrrCreateWidget
        return context

    def post(self, request, *args, **kwargs):
        oseba_form = OsebaCreateWidget(request.POST or None)
        trr_form = TrrCreateWidget(request.POST or None)
        print("###############Tatatatattat######################")

        podjetje = Partner.objects.get(id=self.get_object().id)
        partner = Partner.objects.get(id=self.get_object().id)

        if oseba_form.is_valid():
            ime = oseba_form.cleaned_data['ime']
            priimek = oseba_form.cleaned_data['priimek']
            status = oseba_form.cleaned_data['status']
            kvalifikacije = oseba_form.cleaned_data['kvalifikacije']

            # validacija: če oseba že obstaja vrni redirect in obvesti uporabnika
            osebe_baza = Oseba.objects.filter(priimek=priimek, ime=ime)

            if osebe_baza.count() == 1:  # če je oseba že v bazi
                messages.error(request, "OSEBA: %s %s že obstaja." % (priimek, ime))
                return HttpResponseRedirect(reverse('moduli:partnerji:detail', kwargs={'pk': partner.pk}))

            Oseba.objects.create_oseba(
                priimek=priimek,
                ime=ime,
                status=status,
                kvalifikacije=kvalifikacije,
                podjetje=podjetje,
                )

            '''Oseba je samo enkrat registrirana pod partnerja'''
            # OPCIJA Z UPORABO MODEL FORM
            # obj_instance = oseba_form.save(commit=False)
            # obj_instance.priimek = oseba_form.cleaned_data['priimek']
            # obj_instance.save()

        if trr_form.is_valid():
            iban = trr_form.cleaned_data['iban']
            banka_clean = trr_form.cleaned_data['banka']
            banka_id = banka_clean.id

            # validacija: v primeru da TRR že obstaja
            trracuni = TRRacun.objects.filter(iban=iban)
            if trracuni.count() == 1:
                messages.error(request, "IBAN: %s že obstaja." % (iban))
                return HttpResponseRedirect(reverse('moduli:partnerji:detail', kwargs={'pk': partner.pk}))

            TRRacun.objects.create_trr(
                iban=iban,
                banka=Banka.objects.get(id=int(banka_id)),
                partner=partner,
                )

        return HttpResponseRedirect('/moduli/partnerji/seznam/')


class PartnerCreateView(CreateView):
    model = Partner
    form_class = PartnerCreateForm


class PartnerUpdateView(UpdateView):
    model = Partner
    form_class = PartnerUpdateForm


class OsebaCreateView(CreateView):
    model = Oseba
    form_class = OsebaCreateForm


class OsebaUpdateView(CreateView):
    model = Oseba
    form_class = OsebaUpdateForm


class UvozPartnerjevCsv(TemplateView):
    template_name = "partnerji/uvoz.html"

    def get_context_data(self, *args, **kwargs):
        context = super(UvozPartnerjevCsv, self).get_context_data(*args, **kwargs)
        context['uvoz_form'] = UvozPartnerjiCsvForm
        return context

    def post(self, request, *args, **kwargs):
        uvoz_form = UvozPartnerjiCsvForm(request.POST or None)

        def add_new_partners(rows):
            rows = io.StringIO(rows)
            records_added = 0

            seznam = csv.DictReader(rows, delimiter=",")

            for row in seznam:

                # poštno številko pretvorimo v ID
                print(row)
                postna_stevilka = row['posta']
                try:
                    posta = Posta.objects.get(postna_stevilka=postna_stevilka)
                except:
                    print("NEPRAVILNA POSTA:", row['posta'], row['kratko_ime'])
                    posta = Posta.objects.get(postna_stevilka=5000)
                row['posta'] = posta.pk
                form = PartnerCreateForm(row)

                if form.is_valid():
                    form.save()
                    records_added += 1

            return messages.success(request, "Število dodatnih vnosov: %s" % (records_added))

        if uvoz_form.is_valid():
            filename = os.path.abspath("eda5/partnerji/uvoz_partnerji.csv")
            with open(filename, 'r') as file:
                partnerji_file = file.read()

            add_new_partners(partnerji_file)

        return HttpResponseRedirect('/moduli/partnerji/seznam/')


class UvozPostCsv(TemplateView):
    template_name = "partnerji/uvoz_posta.html"

    def get_context_data(self, *args, **kwargs):
        context = super(UvozPostCsv, self).get_context_data(*args, **kwargs)
        context['uvoz_posta_form'] = UvozPartnerjiCsvForm
        return context

    def post(self, request, *args, **kwargs):
        uvoz_posta_form = UvozPartnerjiCsvForm(request.POST or None)

        def add_new_partners(rows):
            rows = io.StringIO(rows)
            records_added = 0

            seznam = csv.DictReader(rows, delimiter=",")
            print(seznam.fieldnames)

            # for row in csv.DictReader(rows, delimiter=";"):
            for row in seznam:
            # Generate a dict per row, with the first CSV row being the keys.
            
            # Bind the row data to the PurchaseForm.
                print(row)
                form2 = PostaCreateForm(row)
                # Check to see if the row data is valid.
                if form2.is_valid():
                # Row data is valid so save the record.
                    form2.save()
                    records_added += 1

            print(records_added)
            return messages.success(request, "Število dodatnih vnosov: %s" % (records_added))

        if uvoz_posta_form.is_valid():
            filename = os.path.abspath("eda5/partnerji/poste_slovenije.csv")
            with open(filename, 'r') as file:
                poste_slovenije = file.read()
                print(poste_slovenije)

            add_new_partners(poste_slovenije)

        return HttpResponseRedirect('/moduli/partnerji/seznam/')