# Python


# Django
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.db.models import Q, F, Sum
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.db.models import Value
from django.db.models.functions import Concat

# Mixins
from braces.views import LoginRequiredMixin

# Models
from eda5.delovninalogi.models import DelovniNalog, Delo
from eda5.deli.models import DelStavbe, ProjektnoMesto
from eda5.dogodki.models import Dogodek
from eda5.moduli.models import Zavihek
from eda5.partnerji.models import Oseba
from eda5.racunovodstvo.models import Strosek, PodKonto, SkupinaVrsteStroska, VrstaStroska


# Forms
from ..forms import \
    LetoIzbiraForm,\
    MesecIzbiraForm,\
    UporabimFilterForm,\
    DelavecIzbiraForm,\
    NarociloSelectForm,\
    VrstaStroskaIzbiraForm,\
    ObdobjeDatumForm


# Views
from eda5.core.views import FilteredListView

# Utils
from eda5.core.utils import zaokrozen_zmin
from eda5.core.utils import pretvori_v_ure

# Templated docs
from templated_docs import fill_template
from templated_docs.http import FileResponse



class EvidencaDelovnegaCasa(TemplateView):

    template_name = "reports/delovninalog/evidenca_delovnega_casa.html"

    def get_context_data(self, *args, **kwargs):
        context = super(EvidencaDelovnegaCasa, self).get_context_data(*args, **kwargs)

        modul_zavihek = Zavihek.objects.get(oznaka="REPORT_DELOVNINALOGI_EVIDENCADELOVNEGACASA")
        context['modul_zavihek'] = modul_zavihek

        return context


    def get(self, request, *args, **kwargs):

        uporabim_filter_form = UporabimFilterForm(request.GET or None)
        delavec_izbira_form = DelavecIzbiraForm(request.GET or None)
        vrsta_stroska_izbira_form = VrstaStroskaIzbiraForm(request.GET or None, davcna_klasifikacija=None)
        leto_izbira_form = LetoIzbiraForm(request.GET or None)
        mesec_izbira_form = MesecIzbiraForm(request.GET or None)
        narocilo_izbira_form = NarociloSelectForm(request.GET or None)
        obdobje_datum_form = ObdobjeDatumForm(request.GET or None)

        delo_list = Delo.objects.filter().order_by('datum')


        if uporabim_filter_form.is_valid():

            if delavec_izbira_form.is_valid():
                delavec = delavec_izbira_form.cleaned_data['delavec']
                if delavec:
                    delavec = Oseba.objects.get(id=delavec.pk)
                    delo_list = delo_list.filter(delavec=delavec)

            if leto_izbira_form.is_valid():
                obdobje_leto = leto_izbira_form.cleaned_data['obdobje_leto']
                if obdobje_leto:
                    delo_list = delo_list.filter(datum__year=obdobje_leto.oznaka)

            if mesec_izbira_form.is_valid():
                obdobje_mesec = mesec_izbira_form.cleaned_data['obdobje_mesec']
                if obdobje_mesec:
                    delo_list = delo_list.filter(datum__month=obdobje_mesec.oznaka)

            if obdobje_datum_form.is_valid():
                datum_od = obdobje_datum_form.cleaned_data['datum_od']
                datum_do = obdobje_datum_form.cleaned_data['datum_do']
                if datum_od:
                    delo_list = delo_list.filter(datum__gte=datum_od)
                if datum_do:
                    delo_list = delo_list.filter(datum__lte=datum_do)

            if vrsta_stroska_izbira_form.is_valid():
                vrsta_stroska = vrsta_stroska_izbira_form.cleaned_data['vrsta_stroska']
                if vrsta_stroska:
                    delo_list = delo_list.filter(delovninalog__opravilo__vrsta_stroska=vrsta_stroska)

            if narocilo_izbira_form.is_valid():
                narocilo = narocilo_izbira_form.cleaned_data['narocilo']
                if narocilo:
                    delo_list = delo_list.filter(delovninalog__opravilo__narocilo=narocilo)


            # preračun delo_cas_rac
            delo_list = delo_list.annotate(delo_cas=F('time_stop')-F('time_start'))

            for delo in delo_list:

                # osnovni dejanski delo_cas
                delo_cas = delo.delo_cas
                # enota za zaokroževanje
                zmin = delo.delovninalog.opravilo.zmin
                # zaokrožen delo_cas
                delo_cas_rac = zaokrozen_zmin(delo_cas, zmin, '+')
                # pretvorjen v decimalno številko delo_cas
                delo_cas_rac = pretvori_v_ure(delo_cas_rac)
                # shranimo v bazo
                delo.delo_cas_rac = delo_cas_rac
                delo.save()



            delo_cas_sum = delo_list.aggregate(skupaj=Sum('delo_cas_rac'))

            context = self.get_context_data(
                delo_list=delo_list,
                delo_cas_sum=delo_cas_sum,
                delavec_izbira_form=delavec_izbira_form,
                uporabim_filter_form=uporabim_filter_form,
                vrsta_stroska_izbira_form=vrsta_stroska_izbira_form,
                leto_izbira_form=leto_izbira_form,
                mesec_izbira_form=mesec_izbira_form,
                obdobje_datum_form=obdobje_datum_form,
                narocilo_izbira_form=narocilo_izbira_form,
            )

        else:
            context = self.get_context_data(
                uporabim_filter_form=uporabim_filter_form,
                delavec_izbira_form=delavec_izbira_form,
                vrsta_stroska_izbira_form=vrsta_stroska_izbira_form,
                leto_izbira_form=leto_izbira_form,
                mesec_izbira_form=mesec_izbira_form,
                obdobje_datum_form=obdobje_datum_form,
                narocilo_izbira_form=narocilo_izbira_form,
            )

        return self.render_to_response(context)
