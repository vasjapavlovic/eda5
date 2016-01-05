# PYTHON #############################################################
from decimal import Decimal

# DJANGO #############################################################
from django.views.generic import TemplateView, ListView, DetailView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render


# INTERNO ############################################################
from ..models import Racun, Strosek
from ..forms.racun_forms import RacunCreateForm


# UVOŽENO ############################################################
# Arhiv
from eda5.arhiv.forms import ArhiviranjeRacunForm
from eda5.arhiv.models import ArhivMesto, Arhiviranje

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
            racunovodsko_leto = racun_create_form.cleaned_data['racunovodsko_leto']
            oznaka = racun_create_form.cleaned_data['oznaka']
            davcna_klasifikacija = racun_create_form.cleaned_data['davcna_klasifikacija']

            racun_data = Racun.objects.create_racun(
                racunovodsko_leto=racunovodsko_leto,
                oznaka=oznaka,
                davcna_klasifikacija=davcna_klasifikacija,
                )

            racun = Racun.objects.get(id=racun_data.pk)

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

            Arhiviranje.objects.create_arhiviranje(
                racun=racun,
                dokument=dokument,
                arhiviral=oseba,
                elektronski=elektronski,
                fizicni=fizicni,
                lokacija_hrambe=lokacija_hrambe,
            )

        else:
            return render(request, self.template_name, {
                'racun_create_form': racun_create_form,
                'arhiviranje_create_form': arhiviranje_create_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        return HttpResponseRedirect(reverse("moduli:racunovodstvo:racun_detail", kwargs={"pk": racun.pk}))


class RacunListView(ListView):
    model = Racun
    template_name = "racunovodstvo/racun/list/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(RacunListView, self).get_context_data(*args, **kwargs)

        # SEZNAM NElikvidirani in Likvidirani računi
        arhiviranje_list = Arhiviranje.objects.all()

        racun_likvidiran_list = []
        racun_nelikvidiran_list = []
        for arhiviranje in arhiviranje_list:
            if arhiviranje.racun:
                racun_likvidiran_list.append(arhiviranje.racun)
            else:
                racun_nelikvidiran_list.append(arhiviranje.racun)

        context['racun_nelikvidiran_list'] = racun_nelikvidiran_list
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
        strosek_vrednost_z_dvv = 0

        for strosek in strosek_list:

            # določimo ddv
            if strosek.stopnja_ddv == 0:
                stopnja_ddv = 0.000
            if strosek.stopnja_ddv == 1:
                stopnja_ddv = 0.095
            if strosek.stopnja_ddv == 2:
                stopnja_ddv = 0.220

            strosek_vrednost_brez_ddv += Decimal(strosek.osnova)
            strosek_vrednost_z_dvv += Decimal(strosek.osnova) * (1 + Decimal(stopnja_ddv))

        context['strosek_vrednost_brez_ddv'] = "%.2f" % (strosek_vrednost_brez_ddv)
        context['strosek_vrednost_z_dvv'] = "%.2f" % (strosek_vrednost_z_dvv)

        return context