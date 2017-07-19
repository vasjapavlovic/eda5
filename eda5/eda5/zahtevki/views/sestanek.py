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

# Zahtevek Sestanek
from ..forms import ZahtevekSestanekCreateForm, ZahtevekSestanekUpdateForm
from ..models import ZahtevekSestanek


# UVOŽENO ##############################################################

# Moduli
from eda5.moduli.models import Zavihek

# Narocila
from eda5.narocila.models import Narocilo

# Partnerji
from eda5.partnerji.models import SkupinaPartnerjev


class ZahtevekSestanekCreateView(TemplateView):
    template_name = "zahtevki/zahtevek/create_sestanek.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ZahtevekSestanekCreateView, self).get_context_data(*args, **kwargs)
        context['zahtevek_splosno_form'] = ZahtevekCreateForm
        context['zahtevek_sestanek_form'] = ZahtevekSestanekCreateForm

        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_SESTANEK_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *Args, **kwargs):

        zahtevek_splosno_form = ZahtevekCreateForm(request.POST or None)
        zahtevek_sestanek_form = ZahtevekSestanekCreateForm(request.POST or None)
        zahtevek_sestanek_update_form = ZahtevekSestanekUpdateForm(request.POST or None)
        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_SESTANEK_CREATE")

        # izdelamo objekt splosni zahtevek
        if zahtevek_splosno_form.is_valid():
            oznaka = zahtevek_splosno_form.cleaned_data['oznaka']
            naziv = zahtevek_splosno_form.cleaned_data['naziv']
            rok_izvedbe = zahtevek_splosno_form.cleaned_data['rok_izvedbe']
            nosilec = zahtevek_splosno_form.cleaned_data['nosilec']

            zahtevek_splosno_data = Zahtevek.objects.create_zahtevek(
                oznaka=oznaka,
                vrsta=2,
                naziv=naziv,
                rok_izvedbe=rok_izvedbe,
                nosilec=nosilec,
                status=3,
            )
            zahtevek = Zahtevek.objects.get(id=zahtevek_splosno_data.pk)

        else:
            return render(request, self.template_name, {
                'zahtevek_splosno_form': zahtevek_splosno_form,
                'zahtevek_sestanek_form': zahtevek_sestanek_form,
                'modul_zavihek': modul_zavihek,
                'zahtevek_sestanek_update_form': zahtevek_sestanek_update_form,
                }
            )

        # izdelamo objekt sestanek
        if zahtevek_sestanek_form.is_valid():

            sklicatelj = zahtevek_sestanek_form.cleaned_data['sklicatelj']
            datum = zahtevek_sestanek_form.cleaned_data['datum']

            zahtevek_sestanek_data = ZahtevekSestanek.objects.create_zahtevek_sestanek(
                zahtevek=zahtevek,
                sklicatelj=sklicatelj,
                datum=datum,
            )
            zahtevek_sestanek_object = ZahtevekSestanek.objects.get(id=zahtevek_sestanek_data.pk)

        else:
            return render(request, self.template_name, {
                'zahtevek_splosno_form': zahtevek_splosno_form,
                'zahtevek_sestanek_form': zahtevek_sestanek_form,
                'modul_zavihek': modul_zavihek,
                'zahtevek_sestanek_update_form': zahtevek_sestanek_update_form,
                }
            )

        # dodamo udeležence (many-to-many, ki se lahko doda samo po tem ko je objekt že izdelan : sestanek)
        if zahtevek_sestanek_update_form.is_valid():
            udelezenci = zahtevek_sestanek_update_form.cleaned_data['udelezenci']

            zahtevek_sestanek_object.udelezenci = udelezenci
            zahtevek_sestanek_object.save()

        else:
            return render(request, self.template_name, {
                'zahtevek_splosno_form': zahtevek_splosno_form,
                'zahtevek_sestanek_form': zahtevek_sestanek_form,
                'zahtevek_sestanek_update_form': zahtevek_sestanek_update_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk}))


class PodzahtevekSestanekCreateView(UpdateView):
    model = Zahtevek
    fields = ('id', )
    template_name = "zahtevki/zahtevek/create_sestanek.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PodzahtevekSestanekCreateView, self).get_context_data(*args, **kwargs)
        context['zahtevek_splosno_form'] = ZahtevekCreateForm
        context['zahtevek_sestanek_form'] = ZahtevekSestanekCreateForm

        modul_zavihek = Zavihek.objects.get(oznaka="PODZAHTEVEK_SESTANEK_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *Args, **kwargs):

        # object
        zahtevek_parent = Zahtevek.objects.get(id=self.get_object().id)

        zahtevek_splosno_form = ZahtevekCreateForm(request.POST or None)
        zahtevek_sestanek_form = ZahtevekSestanekCreateForm(request.POST or None)
        modul_zavihek = Zavihek.objects.get(oznaka="PODZAHTEVEK_SESTANEK_CREATE")

        if zahtevek_splosno_form.is_valid():
            oznaka = zahtevek_splosno_form.cleaned_data['oznaka']
            naziv = zahtevek_splosno_form.cleaned_data['naziv']
            rok_izvedbe = zahtevek_splosno_form.cleaned_data['rok_izvedbe']
            nosilec = zahtevek_splosno_form.cleaned_data['nosilec']

            zahtevek_splosno_data = Zahtevek.objects.create_zahtevek(
                oznaka=oznaka,
                vrsta=2,
                naziv=naziv,
                rok_izvedbe=rok_izvedbe,
                nosilec=nosilec,
                status=3,
                zahtevek_parent=zahtevek_parent,
            )
            zahtevek = Zahtevek.objects.get(id=zahtevek_splosno_data.pk)

        else:
            return render(request, self.template_name, {
                'zahtevek_splosno_form': zahtevek_splosno_form,
                'zahtevek_sestanek_form': zahtevek_sestanek_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        if zahtevek_sestanek_form.is_valid():

            sklicatelj = zahtevek_sestanek_form.cleaned_data['sklicatelj']
            # udelezenci = zahtevek_sestanek_form.cleaned_data['udelezenci']
            datum = zahtevek_sestanek_form.cleaned_data['datum']

            ZahtevekSestanek.objects.create_zahtevek_sestanek(
                zahtevek=zahtevek,
                sklicatelj=sklicatelj,
                # udelezenci=udelezenci,
                datum=datum,
            )

        else:
            return render(request, self.template_name, {
                'zahtevek_splosno_form': zahtevek_splosno_form,
                'zahtevek_sestanek_form': zahtevek_sestanek_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk}))


class ZahtevekUpdateSestanekView(UpdateView):
    model = ZahtevekSestanek
    form_class = ZahtevekSestanekUpdateForm
    template_name = "zahtevki/zahtevek/update_zahtevek_sestanek.html"


# view called with ajax to reload the month drop down list
def reload_controls_view(request):

    c = {}
    c.update(csrf(request))

    context = {}
    # get the object
    narocilo = request.POST['narocilo']
    narocilo = Narocilo.objects.get(id=narocilo)

    # osebe od izvajalca
    osebe_izvajalec = []
    for oseba in narocilo.izvajalec.oseba_set.all():
        osebe_izvajalec.append(oseba.id)

    # osebe od naročnika
    osebe_narocnik = []
    for partner in narocilo.narocnik.partner.all():
        for oseba in partner.oseba_set.all():
            osebe_narocnik.append(oseba.id)

    skupine_partnerjev = []
    # skupine partnerjev od izvajalca
    partner_davcna_st = narocilo.izvajalec.davcna_st
    skupina_partnerjev = SkupinaPartnerjev.objects.get(oznaka=partner_davcna_st)
    skupine_partnerjev.append(skupina_partnerjev.id)

    # skupine partnerjev od izvajalca
    skupine_partnerjev.append(narocilo.narocnik.id)

    # FILTER NOSILCI ZAHTEVKA
    context['nosilci_to_display'] = osebe_izvajalec

    # FILTER UDELEŽENCI
    # osebe naročnika + osebe izvajalca
    udelezenci = osebe_narocnik + osebe_izvajalec
    context['udelezenci_to_display'] = udelezenci

    # FILTER SKLICATELJ
    context['sklicatelj_to_display'] = skupine_partnerjev

    return JsonResponse(context)
