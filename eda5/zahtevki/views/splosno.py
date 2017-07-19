# Python


# Django
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, UpdateView

# Mixins
from braces.views import LoginRequiredMixin

# Models
from ..models import Zahtevek
from eda5.arhiv.models import Arhiviranje, ArhivMesto
from eda5.deli.models import Skupina, Podskupina, DelStavbe, ProjektnoMesto
from eda5.delovninalogi.models import Opravilo
from eda5.dogodki.models import Dogodek
from eda5.kljuci.models import PredajaKljuca
from eda5.moduli.models import Zavihek
from eda5.narocila.models import Narocilo
from eda5.partnerji.models import Oseba
from eda5.pomanjkljivosti.models import Pomanjkljivost
from eda5.povprasevanje.models import Povprasevanje
from eda5.razdelilnik.models import Razdelilnik
from eda5.reklamacije.models import Reklamacija
from eda5.sestanki.models import Sestanek
from eda5.zaznamki.models import Zaznamek

# Forms
from ..forms import ZahtevekUpdateForm, ZahtevekIzbiraForm, ZahtevekSearchForm
from eda5.arhiv.forms import ArhiviranjeZahtevekForm
from eda5.delovninalogi.forms import OpraviloCreateForm, OpraviloElementUpdateForm, OpraviloPomanjkljivostUpdateForm
from eda5.dogodki.forms import DogodekCreateForm, DogodekUpdateForm
from eda5.kljuci.forms import PredajaKljucaCreateForm, PredajaKljucaVraciloForm
from eda5.zaznamki.forms import ZaznamekForm

# Views
from eda5.core.views import FilteredListView


class ZahtevekListView(LoginRequiredMixin, FilteredListView):
    model = Zahtevek
    form_class= ZahtevekSearchForm
    template_name = "zahtevki/zahtevek/list/base.html"
    paginate_by = 30

    def get_context_data(self, *args, **kwargs):
        context = super(ZahtevekListView, self).get_context_data(*args, **kwargs)

        # content
        # context['zahtevki_vresevanju_list'] = self.model.objects.zahtevki_vresevanju()
        # context['zahtevki_zakljuceni_list'] = self.model.objects.zahtevki_zakljuceni()

        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_LIST")
        context['modul_zavihek'] = modul_zavihek
        return context


class ZahtevekCreateIzbiraView(LoginRequiredMixin, TemplateView):
    model = Zahtevek
    template_name = "zahtevki/zahtevek/create_izbira.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ZahtevekCreateIzbiraView, self).get_context_data(*args, **kwargs)

        # zahtevek
        context['zahtevek_izbira_form'] = ZahtevekIzbiraForm

        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        zahtevek_izbira_form = ZahtevekIzbiraForm(request.POST or None)

        if zahtevek_izbira_form.is_valid():

            vrsta_zahtevka = zahtevek_izbira_form.cleaned_data['vrsta_zahtevka']

            if vrsta_zahtevka == '1':
                return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_create_skodni_dogodek'))
            if vrsta_zahtevka == '2':
                return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_create_sestanek'))
            if vrsta_zahtevka == '3':
                return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_create_izvedba_del'))
            if vrsta_zahtevka == '4':
                return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_create_predaja_lastnine'))
            if vrsta_zahtevka == '5':
                return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_create_analiza'))
            if vrsta_zahtevka == '6':
                return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_create_povprasevanje'))
            if vrsta_zahtevka == '7':
                return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_create_reklamacija'))


class ZahtevekUpdateView(LoginRequiredMixin, UpdateView):
    model = Zahtevek
    form_class = ZahtevekUpdateForm
    template_name = "zahtevki/zahtevek/update_zahtevek_main.html"


class ZahtevekDetailView(LoginRequiredMixin, DetailView):
    model = Zahtevek
    template_name = "zahtevki/zahtevek/detail/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ZahtevekDetailView, self).get_context_data(*args, **kwargs)

        # arhiv_mesto
        context['arhiv_mesto'] = ArhivMesto.objects.get(oznaka=self.object.oznaka)

        # dogodek
        context['dogodek_create_form'] = DogodekCreateForm

        # kljuci
        context['predajakljuca_create_form'] = PredajaKljucaCreateForm
        context['predajakljuca_vracilo_form'] = PredajaKljucaVraciloForm
        context['predaja_kljuca_list'] = PredajaKljuca.objects.filter(
                zahtevek=self.object.id)

        # naročila
        context['narocila_list'] = Narocilo.objects.filter(zahtevek=self.object.id)

        # opravilo
        context['opravilo_form'] = OpraviloCreateForm
        context['opravilo_list'] = Opravilo.objects.filter(zahtevek=self.object.id)

        # pomanjkljivosti
        context['pomanjkljivost_list'] = Pomanjkljivost.objects.filter(zahtevek=self.object.id)

        # povprasevanje
        context['povprasevanje_list'] = Povprasevanje.objects.filter(zahtevek=self.object.id)

        # razdelilnik
        context['razdelilnik_list'] = Razdelilnik.objects.filter(zahtevek=self.object.id)

        # reklamacije
        context['reklamacija_list'] = Reklamacija.objects.filter(zahtevek=self.object.id)

        # sestanki
        context['sestanek_list'] = Sestanek.objects.filter(zahtevek=self.object.id)

        # zaznamek
        context['zaznamek_form'] = ZaznamekForm
        context['zaznamek_list'] = Zaznamek.objects.filter(zahtevek=self.object.id).order_by('-datum', '-ura')

        # zahtevek - child
        context['zahtevek_create_form'] = ZahtevekIzbiraForm
        context['zahtevek_child_list'] = Zahtevek.objects.filter(zahtevek_parent=self.object.id)

        context['arhiviranje_form'] = ArhiviranjeZahtevekForm

        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):
        # opravilo_form = OpraviloCreateForm(request.POST or None)
        arhiviranje_form = ArhiviranjeZahtevekForm(request.POST or None)
        dogodek_create_form = DogodekCreateForm(request.POST or None)
        zaznamek_form = ZaznamekForm(request.POST or None)
        zahtevek_create_form = ZahtevekIzbiraForm(request.POST or None)


        zahtevek = Zahtevek.objects.get(id=self.get_object().id)

        opravilo_list = Opravilo.objects.filter(zahtevek=zahtevek)
        zaznamek_list = Zaznamek.objects.filter(zahtevek=zahtevek)
        zahtevek_child_list = Zahtevek.objects.filter(zahtevek_parent=zahtevek)

        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_DETAIL")

        # DODAJANJE ZAZNAMKOV
        if zaznamek_form.is_valid():
            tekst = zaznamek_form.cleaned_data['tekst']
            datum = zaznamek_form.cleaned_data['datum']
            ura = zaznamek_form.cleaned_data['ura']

            Zaznamek.objects.create_zaznamek(tekst=tekst,
                                             datum=datum,
                                             ura=ura,
                                             zahtevek=zahtevek,
                                             )

            return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk}))

        # DODAJANJE PODZAHTEVKOV
        if zahtevek_create_form.is_valid():

            vrsta_zahtevka = zahtevek_create_form.cleaned_data['vrsta_zahtevka']

            if vrsta_zahtevka == '1':
                return HttpResponseRedirect(reverse('moduli:zahtevki:podzahtevek_create_skodni_dogodek',
                                                    kwargs={'pk': zahtevek.pk}))
            if vrsta_zahtevka == '2':
                return HttpResponseRedirect(reverse('moduli:zahtevki:podzahtevek_create_sestanek',
                                                    kwargs={'pk': zahtevek.pk}))
            if vrsta_zahtevka == '3':
                return HttpResponseRedirect(reverse('moduli:zahtevki:podzahtevek_create_izvedba_del',
                                                    kwargs={'pk': zahtevek.pk}))
            if vrsta_zahtevka == '4':
                return HttpResponseRedirect(reverse('moduli:zahtevki:podzahtevek_create_predaja_lastnine',
                                                    kwargs={'pk': zahtevek.pk}))
            if vrsta_zahtevka == '5':
                return HttpResponseRedirect(reverse('moduli:zahtevki:podzahtevek_create_analiza',
                                                    kwargs={'pk': zahtevek.pk}))
            if vrsta_zahtevka == '6':
                return HttpResponseRedirect(reverse('moduli:zahtevki:podzahtevek_create_povprasevanje',
                                                    kwargs={'pk': zahtevek.pk}))
            if vrsta_zahtevka == '7':
                return HttpResponseRedirect(reverse('moduli:zahtevki:podzahtevek_create_reklamacija',
                                                    kwargs={'pk': zahtevek.pk}))


        # ARHIVIRANJE

        if arhiviranje_form.is_valid():

            dokument = arhiviranje_form.cleaned_data['dokument']
            elektronski = arhiviranje_form.cleaned_data['elektronski']
            fizicni = arhiviranje_form.cleaned_data['fizicni']
            lokacija_hrambe = ArhivMesto.objects.get(oznaka=zahtevek.oznaka)

            # arhiviral
            user = request.user
            oseba = Oseba.objects.get(user=user)
            arhiviral = oseba

            Arhiviranje.objects.create_arhiviranje(
                zahtevek=zahtevek,
                dokument=dokument,
                arhiviral=arhiviral,
                elektronski=elektronski,
                fizicni=fizicni,
                lokacija_hrambe=lokacija_hrambe,
            )

            return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk}))



        # IF NOT VALID
        return render(request, self.template_name, {
            'object': zahtevek,
            # 'opravilo_form': opravilo_form,
            'opravilo_list': opravilo_list,
            'zaznamek_form': zaznamek_form,
            'zaznamek_list': zaznamek_list,
            'zahtevek_create_form': zahtevek_create_form,
            'zahtevek_child_list': zahtevek_child_list,
            'arhiviranje_form': arhiviranje_form,
            'modul_zavihek': modul_zavihek,
            }
        )


# POPUP
# dodatek za filtriranje prikazanega seznama
from eda5.core.views import FilteredListView
from ..forms import ZahtevekSearchForm
class ZahtevekPopUpListView(FilteredListView):
    model = Zahtevek
    form_class= ZahtevekSearchForm
    template_name = "zahtevki/zahtevek/popup/popup_base.html"
    paginate_by = 10