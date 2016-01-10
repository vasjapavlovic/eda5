

# DJANGO UVOZI ################################
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.generic import UpdateView

# RELATIVNI UVOZI #############################
from ..forms.strosek_forms import StrosekOsnovaCreateForm
from ..forms.vrsta_stroska_forms import VrstaStroskaIzbiraForm
from ..models import Racun, Strosek, Konto, PodKonto, SkupinaVrsteStroska, VrstaStroska


# ABSOLUTNI UVOZI #############################
from eda5.moduli.models import Zavihek

# ==================================================================================================


class StrosekCreateView(UpdateView):

    model = Racun
    template_name = "racunovodstvo/strosek/create_from_racun.html"
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):
        context = super(StrosekCreateView, self).get_context_data(*args, **kwargs)

        # strosek
        context['strosek_osnova_create_form'] = StrosekOsnovaCreateForm

        racun = Racun.objects.get(id=self.get_object().id)
        davcna_klasifikacija = racun.davcna_klasifikacija
        context['vrsta_stroska_izbira_form'] = VrstaStroskaIzbiraForm(davcna_klasifikacija=davcna_klasifikacija)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="STROSEK_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        # object
        racun = Racun.objects.get(id=self.get_object().id)
        davcna_klasifikacija = racun.davcna_klasifikacija
        # forms
        strosek_osnova_create_form = StrosekOsnovaCreateForm(request.POST or None)
        vrsta_stroska_izbira_form = VrstaStroskaIzbiraForm(request.POST or None, davcna_klasifikacija=davcna_klasifikacija)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="STROSEK_CREATE")

        if vrsta_stroska_izbira_form.is_valid():
            vrsta_stroska = vrsta_stroska_izbira_form.cleaned_data['vrsta_stroska']

        else:
            return render(request, self.template_name, {
                'strosek_osnova_create_form': strosek_osnova_create_form,
                'vrsta_stroska_izbira_form': vrsta_stroska_izbira_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        if strosek_osnova_create_form.is_valid():

            # cleaned data
            naziv = strosek_osnova_create_form.cleaned_data['naziv']
            datum_storitve_od = strosek_osnova_create_form.cleaned_data['datum_storitve_od']
            datum_storitve_do = strosek_osnova_create_form.cleaned_data['datum_storitve_do']
            obdobje_obracuna_leto = strosek_osnova_create_form.cleaned_data['obdobje_obracuna_leto']
            obdobje_obracuna_mesec = strosek_osnova_create_form.cleaned_data['obdobje_obracuna_mesec']
            delovni_nalog = strosek_osnova_create_form.cleaned_data['delovni_nalog']
            osnova = strosek_osnova_create_form.cleaned_data['osnova']
            stopnja_ddv = strosek_osnova_create_form.cleaned_data['stopnja_ddv']

            ''' AVTOMATSKA DODELITEV OZNAKE STROŠKA '''
            #############################################################################
            # oznaka_racuna = racun.dokument.vrsta_dokumenta.oznaka + "." + \
            #                 str(racun.oznaka) + "." + \
            #                 str(racun.racunovodsko_leto)

            try:
                stevilo_stroskov = Strosek.objects.filter(racun=racun).count()
                zap_st_stroska = stevilo_stroskov + 1
            except:
                zap_st_stroska = 1

            # oznaka_stroska = oznaka_racuna + "-" + str(zap_st_stroska)
            oznaka = zap_st_stroska
            # ****************************************************************************

            # create strosek
            Strosek.objects.create_strosek(
                oznaka=oznaka,
                naziv=naziv,
                datum_storitve_od=datum_storitve_od,
                datum_storitve_do=datum_storitve_do,
                obdobje_obracuna_leto=obdobje_obracuna_leto,
                obdobje_obracuna_mesec=obdobje_obracuna_mesec,
                delovni_nalog=delovni_nalog,
                osnova=osnova,
                stopnja_ddv=stopnja_ddv,

                # relacije izven tega obrazca
                vrsta_stroska=vrsta_stroska,
                racun=racun,
            )

        else:
            return render(request, self.template_name, {
                'strosek_osnova_create_form': strosek_osnova_create_form,
                'vrsta_stroska_izbira_form': vrsta_stroska_izbira_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        return HttpResponseRedirect(reverse('moduli:racunovodstvo:racun_detail', kwargs={'pk': racun.pk}))


class StrosekUpdateView(UpdateView):
    pass


# view called with ajax to reload the month drop down list
def reload_controls_vrsta_stroska_podkonto_view(request):

    c = {}
    c.update(csrf(request))

    context = {}
    # get the object
    konto = request.POST['konto']
    konto = Konto.objects.get(id=konto)

    # podskupine glede na izbrano skupino
    konto_list = []
    for podkonto in konto.podkonto_set.all():
        konto_list.append(podkonto.id)

    # OUTPUT FILTER
    # Podskupine
    context['podkonto_to_display'] = konto_list

    return JsonResponse(context)


# view called with ajax to reload the month drop down list
def reload_controls_vrsta_stroska_skupinavrstestroska_view(request):

    c = {}
    c.update(csrf(request))

    context = {}
    # get the object
    podkonto = request.POST['podkonto']
    podkonto = PodKonto.objects.get(id=podkonto)

    # deli stavbe glede na izbrano podskupino
    skupinavrstestroska_list = []
    for skupina_vrste_stroska in podkonto.skupinavrstestroska_set.all():
        skupinavrstestroska_list.append(skupina_vrste_stroska.id)

    # OUTPUT FILTER

    # DelStavbe
    context['skupinavrstestroska_to_display'] = skupinavrstestroska_list

    return JsonResponse(context)


# view called with ajax to reload the month drop down list
def reload_controls_vrsta_stroska_view(request):

    c = {}
    c.update(csrf(request))

    context = {}
    # get the object
    skupinavrstestroska = request.POST['skupinavrstestroska']
    skupinavrstestroska = SkupinaVrsteStroska.objects.get(id=skupinavrstestroska)

    # deli stavbe glede na izbrano podskupino
    vrstastroska_list = []
    for vrstastroska in skupinavrstestroska.vrstastroska_set.all():
        vrstastroska_list.append(vrstastroska.id)

    # OUTPUT FILTER

    # DelStavbe
    context['vrstastroska_to_display'] = vrstastroska_list

    return JsonResponse(context)
