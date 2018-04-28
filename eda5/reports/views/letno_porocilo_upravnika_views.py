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
from eda5.racunovodstvo.models import Strosek


# Forms
from eda5.reports.forms import FormatForm


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

        ###########################################################################
        # FORMS
        ###########################################################################
        format_form = FormatForm(request.POST or None)
        format_form_is_valid = True

        #==========================================
        # PRIDOBIMO PODATKE
        #==========================================

        # Zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="REPORT_LETNO_POROCILO_UPRAVNIKA_STROSKI")


        if format_form_is_valid == True:
            ###########################################################################
            # UKAZI
            ###########################################################################

            # iz instance pridobimo željene podatke
            # ki jih bomo uporabili v izpisu

            # Pripravimo seznam Stroškov vezanih na razdelilnik
            strosek_list = Strosek.objects.filter(racun__davcna_klasifikacija=1).order_by('datum_storitve_od')
            strosek_list = strosek_list.order_by('strosekrazdelilnik__razdelilnik__obdobje_obracuna_leto__oznaka')
            strosek_list = strosek_list.order_by('strosekrazdelilnik__razdelilnik__obdobje_obracuna_mesec__oznaka')

            strosek_list = strosek_list.filter(strosekrazdelilnik__razdelilnik__obdobje_obracuna_leto__oznaka="2017")


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

        # IF NOT VALID
        return render(
            request, self.template_name, {
                'format_form': format_form,
                'modul_zavihek': modul_zavihek,
                }
            )
