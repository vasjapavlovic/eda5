

# DJANGO UVOZI ################################
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import UpdateView

# RELATIVNI UVOZI #############################
from ..forms.strosek_forms import StrosekOsnovaCreateForm
from ..forms.vrsta_stroska_forms import VrstaStroskaIzbiraForm
from ..models import Racun, Strosek


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
        context['vrsta_stroska_izbira_form'] = VrstaStroskaIzbiraForm

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="STROSEK_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        # object
        racun = Racun.objects.get(id=self.get_object().id)
        # forms
        strosek_osnova_create_form = StrosekOsnovaCreateForm(request.POST or None)
        vrsta_stroska_izbira_form = VrstaStroskaIzbiraForm(request.POST or None)
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
            oznaka = strosek_osnova_create_form.cleaned_data['oznaka']
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
            oznaka_racuna = racun.dokument.vrsta_dokumenta.oznaka + "." + \
                            str(racun.oznaka) + "." + \
                            str(racun.racunovodsko_leto)

            try:
                stevilo_stroskov = Strosek.objects.filter(racun=racun).count()
                zap_st_stroska = stevilo_stroskov + 1
            except:
                zap_st_stroska = 1

            oznaka_stroska = oznaka_racuna + "-" + str(zap_st_stroska)
            oznaka = oznaka_stroska
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
