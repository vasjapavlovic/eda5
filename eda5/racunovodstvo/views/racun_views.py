# PYTHON #############################################################
from decimal import Decimal

# DJANGO #############################################################
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render



# INTERNO ############################################################
from ..models import Racun, Strosek
from ..forms.racun_forms import RacunCreateForm, RacunUpdateForm


# UVOŽENO ############################################################
# Arhiv
from eda5.arhiv.forms import ArhiviranjeRacunForm
from eda5.arhiv.models import ArhivMesto, Arhiviranje

# core
from eda5.core.models import ObdobjeLeto

# Partnerji
from eda5.partnerji.models import Oseba

# Posta
from eda5.posta.models import Dokument

# Zavihek
from eda5.moduli.models import Zavihek


class RacunCreateView(TemplateView):
    model = Dokument
    template_name = "racunovodstvo/racun/create.html"

    def get_context_data(self, *args, **kwargs):
        context = super(RacunCreateView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="RACUN_CREATE")
        context['modul_zavihek'] = modul_zavihek

        # Racun
        context['racun_create_form'] = RacunCreateForm

        # arhiv
        context['arhiviranje_create_form'] = ArhiviranjeRacunForm

        return context

    def post(self, request, *args, **kwargs):

        racun_create_form = RacunCreateForm(request.POST or None)
        arhiviranje_create_form = ArhiviranjeRacunForm(request.POST or None)
        modul_zavihek = Zavihek.objects.get(oznaka="RACUN_CREATE")

        if racun_create_form.is_valid():
            # racunovodsko_leto = racun_create_form.cleaned_data['racunovodsko_leto']
            # oznaka = racun_create_form.cleaned_data['oznaka']
            davcna_klasifikacija = racun_create_form.cleaned_data['davcna_klasifikacija']
            stavba = racun_create_form.cleaned_data['stavba']
            datum_storitve_od = racun_create_form.cleaned_data['datum_storitve_od']
            datum_storitve_do = racun_create_form.cleaned_data['datum_storitve_do']
            valuta = racun_create_form.cleaned_data['valuta']
            povracilo_stroskov_zaposlenemu = racun_create_form.cleaned_data['povracilo_stroskov_zaposlenemu']
            je_reprezentanca = racun_create_form.cleaned_data['je_reprezentanca']
            reprezentanca_opis = racun_create_form.cleaned_data['reprezentanca_opis']
            zavrnjen = racun_create_form.cleaned_data['zavrnjen']
            zavrnjen_datum = racun_create_form.cleaned_data['zavrnjen_datum']
            zavrnjen_obrazlozitev_text = racun_create_form.cleaned_data['zavrnjen_obrazlozitev_text']
            form_racun_is_valid = 1  # pogoj - glej spodaj

        else:
            return render(request, self.template_name, {
                'racun_create_form': racun_create_form,
                'arhiviranje_create_form': arhiviranje_create_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        if arhiviranje_create_form.is_valid():

            dokument = arhiviranje_create_form.cleaned_data['dokument']

            lokacija_hrambe = ArhivMesto.objects.get(oznaka="RAC")

            # Računi se hranijo v elektronski in fizični obliki
            elektronski = True
            fizicni = True

            # trenutni logirani uporabnik
            user = request.user
            oseba = Oseba.objects.get(user=user)

            form_arhiviranje_is_valid = 1  # pogoj - glej spodaj

        else:
            return render(request, self.template_name, {
                'racun_create_form': racun_create_form,
                'arhiviranje_create_form': arhiviranje_create_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        if form_racun_is_valid == 1 and form_arhiviranje_is_valid == 1:

            #########################################################################################
            '''AVTOMATSKO OZNAČEVANJE RAČUNA'''
            #########################################################################################
            # leto računa
            racunovodsko_leto_oznaka = datum_storitve_od.year
            racunovodsko_leto = ObdobjeLeto.objects.get(oznaka=racunovodsko_leto_oznaka)

            # za račun = "RAČ"
            if dokument.vrsta_dokumenta.oznaka == "RAC":
                try:
                    zadnji_racun_rac_leta = Racun.objects.filter(
                        racunovodsko_leto=racunovodsko_leto,
                        arhiviranje__dokument__vrsta_dokumenta__oznaka="RAC"
                        ).latest('oznaka')
                    nova_oznaka = zadnji_racun_rac_leta.oznaka + 1
                    oznaka = nova_oznaka
                except:
                    oznaka = 1

            # za račun = "INR"
            if dokument.vrsta_dokumenta.oznaka == "INR":
                try:
                    zadnji_racun_rac_leta = Racun.objects.filter(
                        racunovodsko_leto=racunovodsko_leto,
                        arhiviranje__dokument__vrsta_dokumenta__oznaka="INR"
                        ).latest('oznaka')
                    nova_oznaka = zadnji_racun_rac_leta.oznaka + 1
                    oznaka = nova_oznaka
                except:
                    oznaka = 1

            # za račun = "INR"
            if dokument.vrsta_dokumenta.oznaka == "DBR":
                try:
                    zadnji_racun_rac_leta = Racun.objects.filter(
                        racunovodsko_leto=racunovodsko_leto,
                        arhiviranje__dokument__vrsta_dokumenta__oznaka="DBR"
                        ).latest('oznaka')
                    nova_oznaka = zadnji_racun_rac_leta.oznaka + 1
                    oznaka = nova_oznaka
                except:
                    oznaka = 1

            # za račun = "AVR"
            if dokument.vrsta_dokumenta.oznaka == "AVR":
                try:
                    zadnji_racun_rac_leta = Racun.objects.filter(
                        racunovodsko_leto=racunovodsko_leto,
                        arhiviranje__dokument__vrsta_dokumenta__oznaka="AVR"
                        ).latest('oznaka')
                    nova_oznaka = zadnji_racun_rac_leta.oznaka + 1
                    oznaka = nova_oznaka
                except:
                    oznaka = 1

            # za račun = "PRV"
            if dokument.vrsta_dokumenta.oznaka == "PRV":
                try:
                    zadnji_racun_rac_leta = Racun.objects.filter(
                        racunovodsko_leto=racunovodsko_leto,
                        arhiviranje__dokument__vrsta_dokumenta__oznaka="PRV"
                        ).latest('oznaka')
                    nova_oznaka = zadnji_racun_rac_leta.oznaka + 1
                    oznaka = nova_oznaka
                except:
                    oznaka = 1

            # ***************************************************************************************

            racun_data = Racun.objects.create_racun(
                racunovodsko_leto=racunovodsko_leto,
                oznaka=oznaka,
                davcna_klasifikacija=davcna_klasifikacija,
                stavba=stavba,
                datum_storitve_od=datum_storitve_od,
                datum_storitve_do=datum_storitve_do,
                valuta=valuta,
                povracilo_stroskov_zaposlenemu=povracilo_stroskov_zaposlenemu,
                je_reprezentanca=je_reprezentanca,
                reprezentanca_opis=reprezentanca_opis,
                zavrnjen=zavrnjen,
                zavrnjen_datum=zavrnjen_datum,
                zavrnjen_obrazlozitev_text=zavrnjen_obrazlozitev_text,
                )

            racun = Racun.objects.get(id=racun_data.pk)

            Arhiviranje.objects.create_arhiviranje(
                racun=racun,
                dokument=dokument,
                arhiviral=oseba,
                elektronski=elektronski,
                fizicni=fizicni,
                lokacija_hrambe=lokacija_hrambe,
            )

        return HttpResponseRedirect(reverse("moduli:racunovodstvo:racun_detail", kwargs={"pk": racun.pk}))


class RacunListView(ListView):
    model = Racun
    template_name = "racunovodstvo/racun/list/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(RacunListView, self).get_context_data(*args, **kwargs)

        # seznam nelikvidirane računovodske dokumentacije
        racun_nelikvidiran_list = Dokument.objects.filter(
            Q(arhiviranje__isnull=True, vrsta_dokumenta__oznaka="RAC",) |
            Q(arhiviranje__isnull=True, vrsta_dokumenta__oznaka="INR",) |
            Q(arhiviranje__isnull=True, vrsta_dokumenta__oznaka="PRV",)
        )

        context['racun_nelikvidiran_list'] = racun_nelikvidiran_list

        # seznam arhivirane računovodske dokumentacije
        racun_likvidiran_list = Racun.objects.all()
        context['racun_likvidiran_list'] = racun_likvidiran_list

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="RACUN_LIST")

        context['modul_zavihek'] = modul_zavihek
        return context


class RacunDetailView(DetailView):
    model = Racun
    template_name = "racunovodstvo/racun/detail/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(RacunDetailView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="RACUN_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        # Stroski
        strosek_list = Strosek.objects.filter(racun=self.object.id)
        context['strosek_list'] = strosek_list

        # sum stroska
        strosek_vrednost_brez_ddv = 0
        strosek_vrednost_z_ddv = 0

        for strosek in strosek_list:

            # določimo ddv
            if strosek.stopnja_ddv == 0:
                stopnja_ddv = 0.000
            if strosek.stopnja_ddv == 1:
                stopnja_ddv = 0.095
            if strosek.stopnja_ddv == 2:
                stopnja_ddv = 0.220

            strosek_vrednost_brez_ddv += Decimal(strosek.osnova)
            strosek_vrednost_z_ddv += Decimal(strosek.osnova) * (1 + Decimal(stopnja_ddv))

        context['strosek_vrednost_brez_ddv'] = "%.2f" % (strosek_vrednost_brez_ddv)
        context['strosek_vrednost_z_ddv'] = "%.2f" % (strosek_vrednost_z_ddv)

        return context




class RacunUpdateView(UpdateView):
    model = Racun
    form_class = RacunUpdateForm
    template_name = "racunovodstvo/racun/update.html"

    def get_context_data(self, *args, **kwargs):
        context = super(RacunUpdateView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="RACUN_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context

    def get_success_url(self, **kwargs):
        return reverse('moduli:racunovodstvo:racun_detail', kwargs={'pk': self.object.pk})