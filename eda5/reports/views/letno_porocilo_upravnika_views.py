# Python


# Django
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.db.models import Q, F, Sum
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, UpdateView

# Mixins
from braces.views import LoginRequiredMixin

# Models
from eda5.moduli.models import Zavihek
from eda5.racunovodstvo.models import Strosek, PodKonto, SkupinaVrsteStroska, VrstaStroska


# Forms
from eda5.reports.forms import FormatForm
from ..forms import LetnoPorociloUpravnikaIzpisIzbiraForm


# Views
from eda5.core.views import FilteredListView

# Templated docs
from templated_docs import fill_template
from templated_docs.http import FileResponse


class PorocanjeStroskiView(LoginRequiredMixin, TemplateView):
    template_name = "reports/letno_porocilo_upravnika/porocanje_stroski.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PorocanjeStroskiView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="REPORT_LETNO_POROCILO_UPRAVNIKA_STROSKI")
        context['modul_zavihek'] = modul_zavihek

        letno_porocilo_upravnika_izpis_izbira_form = LetnoPorociloUpravnikaIzpisIzbiraForm()
        context['letno_porocilo_upravnika_izpis_izbira_form'] = letno_porocilo_upravnika_izpis_izbira_form

        # seznam stroškov

        return context


    def get(self, request, *args, **kwargs):

        # osnovni seznam, ki ga bomo filtrirali
        strosek_list = Strosek.objects.filter(racun__davcna_klasifikacija=1).order_by('datum_storitve_od')
        strosek_list = strosek_list.order_by('strosekrazdelilnik__razdelilnik__obdobje_obracuna_leto__oznaka')
        strosek_list = strosek_list.order_by('strosekrazdelilnik__razdelilnik__obdobje_obracuna_mesec__oznaka')


        # Forms za Filtriranje

        # Na začetku so vsi neustrezni

        # Pridobimo podatke iz formsu


        # Izdelamo filtriran seznam glede
        # v specifičnem letu
        strosek_list = strosek_list.filter(strosekrazdelilnik__razdelilnik__obdobje_obracuna_leto__oznaka="2017")


        # Izpišemo podatke v context

        context = self.get_context_data(
            strosek_list=strosek_list,
        )

        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):

        modul_zavihek = Zavihek.objects.get(oznaka="REPORT_LETNO_POROCILO_UPRAVNIKA_STROSKI")

        format_form = FormatForm(request.POST or None)
        format_form_is_valid = True

        letno_porocilo_upravnika_izpis_izbira_form = LetnoPorociloUpravnikaIzpisIzbiraForm(request.POST or None)
        letno_porocilo_upravnika_izpis_izbira_form_is_valid = False

        if letno_porocilo_upravnika_izpis_izbira_form.is_valid():

            izpis_izbira = letno_porocilo_upravnika_izpis_izbira_form.cleaned_data['izpis_izbira']
            letno_porocilo_upravnika_izpis_izbira_form_is_valid = True

        if format_form_is_valid == True:

            strosek_list = Strosek.objects.filter(racun__davcna_klasifikacija=1).order_by('datum_storitve_od')
            strosek_list = strosek_list.order_by('strosekrazdelilnik__razdelilnik__obdobje_obracuna_leto__oznaka')
            strosek_list = strosek_list.order_by('strosekrazdelilnik__razdelilnik__obdobje_obracuna_mesec__oznaka')

            strosek_list = strosek_list.exclude(vrsta_stroska__skupina__skupina__oznaka="ONU")

            strosek_list = strosek_list.filter(strosekrazdelilnik__razdelilnik__obdobje_obracuna_leto__oznaka="2017")


            if letno_porocilo_upravnika_izpis_izbira_form_is_valid == True:

                if izpis_izbira == '1':

                    self.strosek_list = strosek_list

                    izpis_data = {
                        'strosek_list': strosek_list,
                    }

                    # izdelamo izpis
                    filename = fill_template(
                        # oblikovna datoteka v formatu .odb, ki jo želimo uporabiti
                        'obrazci/letno_porocilo_upravnika/letno_porocilo_upravnika_stroski.ods',
                        # podatki za uporabo v oblikovni datoteki
                        izpis_data,
                        output_format="xlsx"
                    )

                    visible_filename = '{}.{}'.format('letno_porocilo_upravnika_stroski' ,"xlsx")

                    return FileResponse(filename, visible_filename)

                if izpis_izbira == '2':


                    strosek_skupina_list = PodKonto.objects.filter(skupinavrstestroska__vrstastroska__strosek__in=strosek_list)
                    strosek_skupina_list = strosek_skupina_list.distinct()
                    strosek_skupina_list = strosek_skupina_list.annotate(znesek_brez_ddv=Sum('skupinavrstestroska__vrstastroska__strosek__osnova'))
                    strosek_skupina_list = strosek_skupina_list.order_by('skupina__zap_st', 'zap_st')

                    self.strosek_skupina_list = strosek_skupina_list


                    izpis_data = {
                        'strosek_skupina_list': strosek_skupina_list,
                    }

                    # izdelamo izpis
                    filename = fill_template(
                        # oblikovna datoteka v formatu .odb, ki jo želimo uporabiti
                        'obrazci/letno_porocilo_upravnika/letno_porocilo_upravnika_strosek_skupina_list.ods',
                        # podatki za uporabo v oblikovni datoteki
                        izpis_data,
                        output_format="xlsx"
                    )

                    visible_filename = '{}.{}'.format('letno_porocilo_upravnika_strosek_skupina_list' ,"xlsx")

                    return FileResponse(filename, visible_filename)

                if izpis_izbira == '3':


                    strosek_vrsta_list = VrstaStroska.objects.filter(strosek__in=strosek_list)
                    strosek_vrsta_list = strosek_vrsta_list.distinct()
                    strosek_vrsta_list = strosek_vrsta_list.annotate(znesek_brez_ddv=Sum('strosek__osnova'))
                    strosek_vrsta_list = strosek_vrsta_list.order_by('skupina__skupina__skupina__zap_st', 'skupina__skupina__zap_st', 'skupina__zap_st', 'zap_st')

                    self.strosek_vrsta_list = strosek_vrsta_list


                    izpis_data = {
                        'strosek_vrsta_list': strosek_vrsta_list,
                    }

                    # izdelamo izpis
                    filename = fill_template(
                        # oblikovna datoteka v formatu .odb, ki jo želimo uporabiti
                        'obrazci/letno_porocilo_upravnika/letno_porocilo_upravnika_strosek_vrsta_list.ods',
                        # podatki za uporabo v oblikovni datoteki
                        izpis_data,
                        output_format="xlsx"
                    )

                    visible_filename = '{}.{}'.format('letno_porocilo_upravnika_strosek_vrsta_list' ,"xlsx")

                    return FileResponse(filename, visible_filename)


        # IF NOT VALID
        return render(
            request, self.template_name, {
                'format_form': format_form,
                'letno_porocilo_upravnika_izpis_izbira_form': letno_porocilo_upravnika_izpis_izbira_form,
                'modul_zavihek': modul_zavihek,
                }
            )
