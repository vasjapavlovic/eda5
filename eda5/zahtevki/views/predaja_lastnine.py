# PYTHON ##############################################################


# DJANGO ##############################################################
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView


# INTERNO ##############################################################
# Zahtevek Osnova
from ..forms import ZahtevekCreateForm
from ..models import Zahtevek

# # Zahtevek Sestanek
# from ..forms import ZahtevekSestanekCreateForm, ZahtevekSestanekUpdateForm
# from ..models import ZahtevekSestanek


# UVOŽENO ##############################################################

# Ključi
from eda5.kljuci.forms import PredajaKljucaCreateForm, PredajaKljucaVraciloForm
from eda5.kljuci.models import PredajaKljuca

# Moduli
from eda5.moduli.models import Zavihek

# Narocila
from eda5.narocila.models import Narocilo

# Partnerji
from eda5.partnerji.models import SkupinaPartnerjev

# Lastnistvo
from eda5.lastnistvo.forms import \
    PredajaLastnineCreateForm,\
    ProdajaLastnineCreateForm,\
    ProdajaLastnineUpdateForm,\
    NajemLastnineCreateForm,\
    NajemLastnineVraciloForm
    
from eda5.lastnistvo.models import \
    PredajaLastnine,\
    ProdajaLastnine,\
    NajemLastnine


class ZahtevekPredajaLastnineCreateView(TemplateView):

    template_name = "zahtevki/zahtevek/create_predaja_lastnine.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ZahtevekPredajaLastnineCreateView, self).get_context_data(*args, **kwargs)
        context['zahtevek_splosno_form'] = ZahtevekCreateForm
        context['predaja_lastnine_form'] = PredajaLastnineCreateForm

        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_PREDAJA_LASTNINE_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *Args, **kwargs):

        zahtevek_splosno_form = ZahtevekCreateForm(request.POST or None)
        predaja_lastnine_form = PredajaLastnineCreateForm(request.POST or None)
        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_PREDAJA_LASTNINE_CREATE")

        # izdelamo objekt splosni zahtevek
        if zahtevek_splosno_form.is_valid():
            oznaka = zahtevek_splosno_form.cleaned_data['oznaka']
            naziv = zahtevek_splosno_form.cleaned_data['naziv']
            rok_izvedbe = zahtevek_splosno_form.cleaned_data['rok_izvedbe']
            nosilec = zahtevek_splosno_form.cleaned_data['nosilec']

            zahtevek_splosno_data = Zahtevek.objects.create_zahtevek(
                oznaka=oznaka,
                vrsta=4,
                naziv=naziv,
                rok_izvedbe=rok_izvedbe,
                nosilec=nosilec,
                status=3,
            )
            zahtevek = Zahtevek.objects.get(id=zahtevek_splosno_data.pk)

        else:
            return render(request, self.template_name, {
                'zahtevek_splosno_form': zahtevek_splosno_form,
                'predaja_lastnine_form': predaja_lastnine_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        # izdelamo PredajaLastnine
        if predaja_lastnine_form.is_valid():

            # oznaka predaje lastnine
            try:
                zap_st = PredajaLastnine.objects.all().count()
                zap_st = zap_st + 1
            except:
                zap_st = 1
            oznaka = "LST-%s" % (zap_st)

            prodajalec = predaja_lastnine_form.cleaned_data['prodajalec']
            kupec = predaja_lastnine_form.cleaned_data['kupec']

            PredajaLastnine.objects.create_predaja_lastnine(
                oznaka=oznaka,
                prodajalec=prodajalec,
                kupec=kupec,
                zahtevek=zahtevek,
            )

        else:
            return render(request, self.template_name, {
                'zahtevek_splosno_form': zahtevek_splosno_form,
                'predaja_lastnine_form': predaja_lastnine_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk}))


class ProdajaLastnineCreateView(UpdateView):
    model = Zahtevek
    template_name = "lastnistvo/prodaja_lastnine/create_from_zahtevek.html"
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):
        context = super(ProdajaLastnineCreateView, self).get_context_data(*args, **kwargs)

        # opravilo
        context['prodaja_lastnine_create_form'] = ProdajaLastnineCreateForm
        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="PRODAJA_LASTNINE_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        # object
        zahtevek = Zahtevek.objects.get(id=self.get_object().id)
        # forms
        prodaja_lastnine_create_form = ProdajaLastnineCreateForm(request.POST or None)
        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="PRODAJA_LASTNINE_CREATE")

        # izdelamo opravilo (!!!elemente opravilu dodamo kasneje)
        if prodaja_lastnine_create_form.is_valid():
            lastniska_enota = prodaja_lastnine_create_form.cleaned_data['lastniska_enota']
            datum_predaje = prodaja_lastnine_create_form.cleaned_data['datum_predaje']
            placnik = prodaja_lastnine_create_form.cleaned_data['placnik']
            predaja_lastnine = zahtevek.predajalastnine

            ProdajaLastnine.objects.create_prodaja_lastnine(
                lastniska_enota=lastniska_enota,
                datum_predaje=datum_predaje,
                placnik=placnik,
                predaja_lastnine=predaja_lastnine
            )

        else:
            return render(request, self.template_name, {
                'prodaja_lastnine_create_form': prodaja_lastnine_create_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk}))


class NajemLastnineCreateView(UpdateView):
    model = Zahtevek
    template_name = "lastnistvo/najem_lastnine/create_from_zahtevek.html"
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):
        context = super(NajemLastnineCreateView, self).get_context_data(*args, **kwargs)

        # opravilo
        context['najem_lastnine_create_form'] = NajemLastnineCreateForm
        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="NAJEM_LASTNINE_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        # object
        zahtevek = Zahtevek.objects.get(id=self.get_object().id)
        # forms
        najem_lastnine_create_form = NajemLastnineCreateForm(request.POST or None)
        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="NAJEM_LASTNINE_CREATE")

        # izdelamo opravilo (!!!elemente opravilu dodamo kasneje)
        if najem_lastnine_create_form.is_valid():
            lastniska_enota = najem_lastnine_create_form.cleaned_data['lastniska_enota']
            predaja_datum = najem_lastnine_create_form.cleaned_data['predaja_datum']
            placnik = najem_lastnine_create_form.cleaned_data['placnik']
            veljavnost_datum = najem_lastnine_create_form.cleaned_data['veljavnost_datum']
            veljavnost_trajanje_opisno = najem_lastnine_create_form.cleaned_data['veljavnost_trajanje_opisno']
            predaja_lastnine = zahtevek.predajalastnine

            NajemLastnine.objects.create_najem_lastnine(
                lastniska_enota=lastniska_enota,
                predaja_datum=predaja_datum,
                placnik=placnik,
                veljavnost_datum=veljavnost_datum,
                veljavnost_trajanje_opisno=veljavnost_trajanje_opisno,
                predaja_lastnine=predaja_lastnine
            )

        else:
            return render(request, self.template_name, {
                'najem_lastnine_create_form': najem_lastnine_create_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk}))


class ProdajaLastnineUpdateView(UpdateView):
    model = ProdajaLastnine
    form_class = ProdajaLastnineUpdateForm
    template_name = "lastnistvo/prodaja_lastnine/update_from_zahtevek.html"


class NajemLastnineVraciloView(UpdateView):
    model = NajemLastnine
    form_class = NajemLastnineVraciloForm
    template_name = "lastnistvo/najem_lastnine/update_from_zahtevek.html"


class PredajaKljucaCreateView(UpdateView):
    model = Zahtevek
    template_name = "kljuci/predaja_kljuca/create_from_zahtevek.html"
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):
        context = super(PredajaKljucaCreateView, self).get_context_data(*args, **kwargs)

        # opravilo
        context['predaja_kljuca_create_form'] = PredajaKljucaCreateForm
        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="PREDAJA_KLJUCA_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        # object
        zahtevek = Zahtevek.objects.get(id=self.get_object().id)
        # forms
        predaja_kljuca_create_form = PredajaKljucaCreateForm(request.POST or None)
        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="PREDAJA_KLJUCA_CREATE")

        # izdelamo predajo
        if predaja_kljuca_create_form.is_valid():
            kljuc = predaja_kljuca_create_form.cleaned_data['kljuc']
            predaja_datum = predaja_kljuca_create_form.cleaned_data['predaja_datum']
            vrsta_predaje = predaja_kljuca_create_form.cleaned_data['vrsta_predaje']


            PredajaKljuca.objects.create_predaja_kljuca(
                kljuc=kljuc,
                predaja_datum=predaja_datum,
                vrsta_predaje=vrsta_predaje,
                zahtevek=zahtevek
            )

        else:

            return render(request, self.template_name, {
                'predaja_kljuca_create_form': predaja_kljuca_create_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk}))


class VraciloKljucaUpdateView(UpdateView):
    model = PredajaKljuca
    form_class = PredajaKljucaVraciloForm
    template_name = "kljuci/predaja_kljuca/update_from_zahtevek.html"
