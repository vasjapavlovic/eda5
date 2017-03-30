from django.shortcuts import render
from django.db.models import Max, Q
from django.http import JsonResponse
from django.core.context_processors import csrf
from django.views.generic.edit import FormMixin



import os

from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, ListView, TemplateView, UpdateView
from django.utils import timezone

from .forms import AktivnostCreateForm, DokumentCreateForm, DokumentSearchForm, SkupinaDokumentaIzbiraForm
from .models import Aktivnost, Dokument, SkupinaDokumenta, VrstaDokumenta

from eda5.arhiv.forms import ArhiviranjeCreateForm
from eda5.arhiv.models import Arhiviranje, ArhivMesto, Arhiv

# core
from eda5.core.views import FilteredListView

from eda5.nastavitve.models import NastavitevPartnerja

from eda5.partnerji.models import Oseba, Partner

from eda5.moduli.models import Zavihek


class PostaHomeView(TemplateView):
    template_name = "posta/home.html"


class DokumentListView(FilteredListView):
    model = Dokument
    form_class= DokumentSearchForm
    template_name = "posta/dokument/list/base.html"
    paginate_by = 10


    def get_context_data(self, *args, **kwargs):
        context = super(DokumentListView, self).get_context_data(*args, **kwargs)

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


class DokumentUpdateFromPartnerView(UpdateView):

    model = Dokument
    form_class = DokumentCreateForm
    template_name = 'posta/dokument/update.html'

    def get_success_url(self):
        return reverse("moduli:partnerji:partner_list")

    def get_context_data(self, *args, **kwargs):
        context = super(DokumentUpdateFromPartnerView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="DOKUMENT_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context


class DokumentUpdateView(UpdateView):

    model = Dokument
    form_class = DokumentCreateForm
    template_name = 'posta/dokument/update.html'

    def get_success_url(self):
        return reverse("moduli:posta:dokument_list")

    def get_context_data(self, *args, **kwargs):
        context = super(DokumentUpdateView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="DOKUMENT_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context


class DokumentCreateView(TemplateView):
    template_name = "posta/dokument/create.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DokumentCreateView, self).get_context_data(*args, **kwargs)
        context['aktivnost_form'] = AktivnostCreateForm
        context['dokument_form'] = DokumentCreateForm
        context['skupina_dokumenta_form'] = SkupinaDokumentaIzbiraForm

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="DOKUMENT_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        aktivnost_form = AktivnostCreateForm(request.POST or None)
        dokument_form = DokumentCreateForm(request.POST or None, request.FILES)
        skupina_dokumenta_form = SkupinaDokumentaIzbiraForm(request.POST or None)
        modul_zavihek = Zavihek.objects.get(oznaka="DOKUMENT_CREATE")

        if aktivnost_form.is_valid():

            datum_aktivnosti = aktivnost_form.cleaned_data['datum_aktivnosti']

            # trenutni logirani uporabnik
            user = request.user
            oseba = Oseba.objects.get(user=user)

            aktivnost_create_data = Aktivnost.objects.create_aktivnost(
                izvajalec=oseba,
                datum_aktivnosti=datum_aktivnosti,
            )

            aktivnost = Aktivnost.objects.get(id=aktivnost_create_data.pk)

        else:
            return render(request, self.template_name, {
                'aktivnost_form': aktivnost_form,
                'dokument_form': dokument_form,
                'modul_zavihek': modul_zavihek,
                'skupina_dokumenta_form': skupina_dokumenta_form,
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
            kraj_izdaje = dokument_form.cleaned_data['kraj_izdaje']


            ################################################
            '''OZNAČEVANJE DOKUMENTOV NA MEDIA SERVERJU'''
            ################################################
            # oznaka_baza
            try:
                object_last = Dokument.objects.all().latest('oznaka_baza')
                nova_oznaka_baza = object_last.oznaka_baza + 1
                oznaka_baza = nova_oznaka_baza
            except:  # če ni nobenega vnosa v bazi
                oznaka_baza = 1
            # ***************************************************************************************

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
                kraj_izdaje=kraj_izdaje,
            )

        else:
            return render(request, self.template_name, {
                'aktivnost_form': aktivnost_form,
                'dokument_form': dokument_form,
                'modul_zavihek': modul_zavihek,
                'skupina_dokumenta_form': skupina_dokumenta_form,
                }
            )

        return HttpResponseRedirect(reverse('moduli:posta:dokument_list'))


# view called with ajax to reload the month drop down list
def reload_controls_view(request):

    c = {}
    c.update(csrf(request))

    context = {}
    skupina_dokumenta = request.POST['skupina_dokumenta']
    context['list_to_display'] = list(VrstaDokumenta.objects.filter(skupina=skupina_dokumenta).values_list('id', flat=True))

    return JsonResponse(context)
