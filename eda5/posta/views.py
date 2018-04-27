# Python
import os

# Django
from django.conf import settings

from django.core.context_processors import csrf
from django.core.urlresolvers import reverse

from django.db.models import Max
from django.db.models import Q

from django.http import HttpResponseRedirect
from django.http import JsonResponse

from django.shortcuts import render

from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import UpdateView
from django.views.generic.edit import FormMixin

from django.utils import timezone

# Utils

# Models
from .models import Aktivnost
from .models import Dokument
from .models import SkupinaDokumenta
from .models import VrstaDokumenta

from eda5.arhiv.models import Arhiviranje
from eda5.arhiv.models import ArhivMesto
from eda5.arhiv.models import Arhiviranje

from eda5.moduli.models import Zavihek
from eda5.nastavitve.models import NastavitevPartnerja

from eda5.partnerji.models import Oseba
from eda5.partnerji.models import Partner


# Forms
from .forms import AktivnostCreateForm
from .forms import DokumentCreateForm
from .forms import DokumentFilterForm
from .forms import DokumentSearchForm
from .forms import KlasifikacijaDokumentaForm
from .forms import SkupinaDokumentaIzbiraForm
from .forms import VrstaDokumentaForm



from eda5.arhiv.forms import ArhiviranjeCreateForm

# Views
from eda5.core.views import FilteredListView


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


class DokumentCustomListView(TemplateView):
    template_name = "posta/dokument/list_filter.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DokumentCustomListView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="DOKUMENT_LIST_FILTERED")
        context['modul_zavihek'] = modul_zavihek
        return context

    def get_form_kwargs(self):
        return {
          'initial': self.get_initial(),
          'prefix': self.get_prefix(),
          'data': self.request.GET or None
        }

    def get(self, request, *args, **kwargs):

        # form za filtriranje
        dokument_filter_form = DokumentFilterForm(request.GET or None)
        vrsta_dokumenta_izbira = SkupinaDokumentaIzbiraForm(request.GET or None)
        vrsta_dokumenta_form = VrstaDokumentaForm(request.GET or None)
        klasifikacija_dokumenta_form = KlasifikacijaDokumentaForm(request.GET or None)

        # na začetku so vsi formi neustrezni
        dokument_filter_form_is_valid = False
        vrsta_dokumenta_izbira_is_valid = False
        vrsta_dokumenta_form_is_valid = False
        klasifikacija_dokumenta_form_is_valid = False

        # Filtriranje prejete in izdane pošte splošno
        if dokument_filter_form.is_valid():
            oznaka = dokument_filter_form.cleaned_data['oznaka']
            naziv = dokument_filter_form.cleaned_data['naziv']
            kraj_izdaje = dokument_filter_form.cleaned_data['kraj_izdaje']
            avtor = dokument_filter_form.cleaned_data['avtor']
            naslovnik = dokument_filter_form.cleaned_data['naslovnik']
            datum_od = dokument_filter_form.cleaned_data['datum_od']
            datum_do = dokument_filter_form.cleaned_data['datum_do']
            dokument_filter_form_is_valid = True

        # vrsta dokumenta form
        if vrsta_dokumenta_izbira.is_valid():
            vrsta_dokumenta_izbira_is_valid = True


        if vrsta_dokumenta_form.is_valid():
            vrsta_dokumenta = vrsta_dokumenta_form.cleaned_data['vrsta_dokumenta']
            vrsta_dokumenta_form_is_valid = True

        if klasifikacija_dokumenta_form.is_valid():
            klasifikacija_dokumenta = klasifikacija_dokumenta_form.cleaned_data['klasifikacija_dokumenta']
            klasifikacija_dokumenta_form_is_valid = True

        # IZDELAMO FILTRIRAN SEZNAM DOKUMENTOV
        # če ne vpišemo niti enega podatka vrni prazen seznam - da ne odpiramo vseh dokumentov brez veze
        if dokument_filter_form_is_valid == True:
            dokument_list_filtered = Dokument.objects.filter()
            dokument_list_filtered = dokument_list_filtered.order_by('-datum_dokumenta')
        else:
            dokument_list_filtered = []

        if dokument_filter_form_is_valid == True:
            # filtriraj samo glede na podane podatke. Če podatka ni ga ne uporabiš.
            if oznaka:
                dokument_list_filtered = dokument_list_filtered.filter(oznaka__icontains=oznaka)
            if naziv:
                dokument_list_filtered = dokument_list_filtered.filter(naziv__icontains=naziv)
            if kraj_izdaje:
                dokument_list_filtered = dokument_list_filtered.filter(kraj_izdaje__icontains=kraj_izdaje)

            if avtor:
                dokument_list_filtered = dokument_list_filtered.filter(avtor=avtor)

            if naslovnik:
                dokument_list_filtered = dokument_list_filtered.filter(naslovnik=naslovnik)

            if datum_od:
                dokument_list_filtered = dokument_list_filtered.filter(datum_dokumenta__gte=datum_od)

            if datum_do:
                dokument_list_filtered = dokument_list_filtered.filter(datum_dokumenta__lte=datum_do)

        if vrsta_dokumenta_form_is_valid == True:
            if vrsta_dokumenta:
                dokument_list_filtered = dokument_list_filtered.filter(vrsta_dokumenta=vrsta_dokumenta)

        if klasifikacija_dokumenta_form_is_valid == True:
            if klasifikacija_dokumenta:
                dokument_list_filtered = dokument_list_filtered.filter(klasifikacija_dokumenta=klasifikacija_dokumenta)

        # podatke izpišemo v kontekst
        context = self.get_context_data(
            dokument_filter_form=dokument_filter_form,
            vrsta_dokumenta_izbira=vrsta_dokumenta_izbira,
            vrsta_dokumenta_form=vrsta_dokumenta_form,
            dokument_list_filtered=dokument_list_filtered,
            klasifikacija_dokumenta_form=klasifikacija_dokumenta_form,
        )

        return self.render_to_response(context)

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


# POPUP
# dodatek za filtriranje prikazanega seznama
from eda5.core.views import FilteredListView
class DokumentPopUpListView(FilteredListView):
    model = Dokument
    form_class= DokumentSearchForm
    template_name = "posta/dokument/popup/popup_base.html"
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        queryset = super(DokumentPopUpListView, self).get_queryset(*args, **kwargs)
        queryset = queryset.filter(arhiviranje__isnull=True)
        skupina_dokumenta = SkupinaDokumenta.objects.get(oznaka="RAC")
        queryset = queryset.exclude(vrsta_dokumenta__skupina=skupina_dokumenta)
        return queryset
