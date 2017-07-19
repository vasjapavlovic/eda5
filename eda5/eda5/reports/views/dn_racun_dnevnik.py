from django.shortcuts import render
from django.utils import timezone

from django.views.generic import TemplateView, DetailView

from templated_docs import fill_template
from templated_docs.http import FileResponse

# Moduli
from eda5.moduli.models import Zavihek


# Deli
from eda5.deli.models import DelStavbe

# Delovninalogi
from eda5.delovninalogi.models import DelovniNalog

# Etažna Lastnina
from eda5.etaznalastnina.models import LastniskaSkupina, Program

# Reports
from eda5.reports.forms import FormatForm, DeliSeznamFilterForm




###########################################################
# SEZNAM DELOV STAVBE PO PROGRAMIH - PRINT
###########################################################
class DnevnikIzvedenihDelView(TemplateView):

    template_name = "reports/delovninalog/dnevnik_izvedenih_del.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DnevnikIzvedenihDelView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        context['form'] = FormatForm
        # context['deli_seznam_filter_form'] = DeliSeznamFilterForm

        return context


    def post(self, request, *args, **kwargs):

        ###########################################################################
        # FORMS
        ###########################################################################

        form = FormatForm(request.POST or None)
        # deli_seznam_filter_form = DeliSeznamFilterForm(request.POST or None)

        form_is_valid = False
        # deli_seznam_filter_form_is_valid = False

        ###########################################################################
        # PRIDOBIMO PODATKE
        ###########################################################################

        if form.is_valid():
            doctypex = form.cleaned_data['format_field']
            form_is_valid = True

        # if deli_seznam_filter_form.is_valid():
        #     program = deli_seznam_filter_form.cleaned_data['program']
        #     deli_filter_list = DelStavbe.objects.filter(lastniska_skupina__program=program)
        #     deli_seznam_filter_form_is_valid = True

        #Če so formi pravilno izpolnjeni

        if form_is_valid == True:
            ###########################################################################
            # UKAZI
            ###########################################################################

            # pridobimo današnji datum za izpis na izpisu

            datum_danes = timezone.now().date()

            # pridobimo seznam delovnih nalogov

            delovninalog_list = DelovniNalog.objects.filter(status=4)  # zaključeni delovni nalogi

            # prenos podatkov za aplikacijo templated_docs

            filename = fill_template(
                'reports/delovninalog/dnevnik_izvedenih_del.odt', {'delovninalog_list': delovninalog_list, 'datum_danes': datum_danes, },
                output_format=doctypex)
            visible_filename = 'dnevnik_izvedenih_del.{}'.format(doctypex)

            return FileResponse(filename, visible_filename)

        # v primeru, da so zgornji Form-i NISO ustrezno izpolnjeni
        # izvrši spodnje ukaze

        else:
            return render(request, self.template_name, {
                'form': form,
                # 'deli_seznam_filter_form': deli_seznam_filter_form,
                }
            )

