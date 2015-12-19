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

from eda5.moduli.models import Zavihek


class PartnerHomeView(TemplateView):
    template_name = "partnerji/home.html"


class PartnerCreateView(CreateView):
    model = Partner
    form_class = PartnerCreateForm
    template_name = "partnerji/partner/create.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PartnerCreateView, self).get_context_data(*args, **kwargs)
        modul_zavihek = Zavihek.objects.get(oznaka="PR_CREATE")
        context['modul_zavihek'] = modul_zavihek
        return context


class PartnerUpdateView(UpdateView):
    model = Partner
    form_class = PartnerUpdateForm


class PartnerListView(PartnerSearchMixin, ListView):
    model = Partner
    template_name = "partnerji/partner/list.html"

    # order_by
    def get_queryset(self):
        queryset = super(PartnerListView, self).get_queryset()
        queryset = queryset.order_by('kratko_ime')
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(PartnerListView, self).get_context_data(*args, **kwargs)
        modul_zavihek = Zavihek.objects.get(oznaka="PR_LIST")
        context['modul_zavihek'] = modul_zavihek
        return context


class OsebaCreateView(CreateView):
    model = Oseba
    form_class = OsebaCreateForm


class OsebaUpdateView(CreateView):
    model = Oseba
    form_class = OsebaUpdateForm


class PartnerDetailView(DetailView):
    model = Partner
    template_name = "partnerji/partner/detail/base.html"

    # subform "Dodaj Osebo"
    form_class = OsebaCreateWidget

    def get_context_data(self, *args, **kwargs):
        context = super(PartnerDetailView, self).get_context_data(*args, **kwargs)
        context['oseba_form'] = self.form_class
        context['trr_form'] = TrrCreateWidget

        modul_zavihek = Zavihek.objects.get(oznaka="PR_LIST")
        context['modul_zavihek'] = modul_zavihek

        modul_zavihek2 = Zavihek.objects.get(oznaka="PR_DETAIL")
        context['modul_zavihek2'] = modul_zavihek2

        return context

    def post(self, request, *args, **kwargs):
        oseba_form = OsebaCreateWidget(request.POST or None)
        trr_form = TrrCreateWidget(request.POST or None)

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
                return HttpResponseRedirect(reverse('moduli:partnerji:partner_detail', kwargs={'pk': partner.pk}))

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
                return HttpResponseRedirect(reverse('moduli:partnerji:partner_detail', kwargs={'pk': partner.pk}))

            TRRacun.objects.create_trr(
                iban=iban,
                banka=Banka.objects.get(id=int(banka_id)),
                partner=partner,
                )

        return HttpResponseRedirect(reverse('moduli:partnerji:partner_detail', kwargs={'pk': partner.pk}))


