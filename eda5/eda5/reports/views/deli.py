from django.shortcuts import render
from django.utils import timezone

from django.views.generic import TemplateView, DetailView

from templated_docs import fill_template
from templated_docs.http import FileResponse

# Moduli
from eda5.moduli.models import Zavihek


# Deli
from eda5.deli.models import Podskupina, DelStavbe

# Etažna Lastnina
from eda5.etaznalastnina.models import LastniskaSkupina, Program

# Reports
from eda5.reports.forms import FormatForm, DeliSeznamFilterForm




###########################################################
# SEZNAM DELOV STAVBE PO PROGRAMIH - PRINT
###########################################################
class DeliSeznamPrintView(TemplateView):

    template_name = "reports/deli/deli_seznam_filter.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DeliSeznamPrintView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        context['form'] = FormatForm
        context['deli_seznam_filter_form'] = DeliSeznamFilterForm

        return context


    def post(self, request, *args, **kwargs):

        ###########################################################################
        # FORMS
        ###########################################################################

        form = FormatForm(request.POST or None)
        deli_seznam_filter_form = DeliSeznamFilterForm(request.POST or None)

        form_is_valid = False
        deli_seznam_filter_form_is_valid = False

        ###########################################################################
        # PRIDOBIMO PODATKE
        ###########################################################################

        if form.is_valid():
            doctypex = form.cleaned_data['format_field']
            form_is_valid = True

        if deli_seznam_filter_form.is_valid():
            program = deli_seznam_filter_form.cleaned_data['program']
            deli_seznam_filter_form_is_valid = True

        #Če so formi pravilno izpolnjeni

        if form_is_valid == True and deli_seznam_filter_form_is_valid == True:
            ###########################################################################
            # UKAZI
            ###########################################################################

            # pridobimo današnji datum za izpis na izpisu

            datum_danes = timezone.now().date()

            # izdelamo seznam delov glede na izbrane programe
            deli_filter_list = DelStavbe.objects.filter(lastniska_skupina__program=program)

            # pridobimo še podskupine, ki jih potrebujemo za prikaz delov po podskupinah
            podskupina_list = Podskupina.objects.all()

            # prenos podatkov za aplikacijo templated_docs
            if not doctypex == 'xlsx':
                filename = fill_template(
                    'reports/deli/deli_seznam.odt', {'podskupina_list': podskupina_list,'deli_filter_list': deli_filter_list, 'datum_danes': datum_danes, 'program': program},
                    output_format=doctypex)
                visible_filename = 'deli_seznam_filter.{}'.format(doctypex)

            else:
                filename = fill_template(
                    'reports/deli/deli_seznam.ods', {'podskupina_list': podskupina_list,'deli_filter_list': deli_filter_list, 'datum_danes': datum_danes, 'program': program},
                    output_format=doctypex)
                visible_filename = 'deli_seznam_filter.{}'.format(doctypex)


            return FileResponse(filename, visible_filename)

        # v primeru, da so zgornji Form-i NISO ustrezno izpolnjeni
        # izvrši spodnje ukaze

        else:
            return render(request, self.template_name, {
                'form': form,
                'deli_seznam_filter_form': deli_seznam_filter_form,
                }
            )


###########################################################
# SEZNAM DELOV STAVBE PO PROGRAMIH - PRINT
###########################################################
class ProstoriSeznamPrintView(TemplateView):

    template_name = "reports/deli/prostori_seznam_filter.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProstoriSeznamPrintView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        context['form'] = FormatForm

        return context


    def post(self, request, *args, **kwargs):

        ###########################################################################
        # FORMS
        ###########################################################################

        form = FormatForm(request.POST or None)
        deli_seznam_filter_form_is_valid = False

        ###########################################################################
        # PRIDOBIMO PODATKE
        ###########################################################################

        if form.is_valid():
            doctypex = form.cleaned_data['format_field']
            form_is_valid = True

        #Če so formi pravilno izpolnjeni

        if form_is_valid == True:
            ###########################################################################
            # UKAZI
            ###########################################################################

            # pridobimo današnji datum za izpis na izpisu

            datum_danes = timezone.now().date()

            # izdelamo seznam prostorov glede na izbrane programe
            prostori_filter_list = DelStavbe.objects.filter(podskupina__oznaka="CA")

            # prenos podatkov za aplikacijo templated_docs
            print(doctypex)
            if not doctypex == 'xlsx':
                filename = fill_template(
                    'reports/deli/prostori_seznam.odt', {'prostori_filter_list': prostori_filter_list, 'datum_danes': datum_danes},
                    output_format=doctypex)
                visible_filename = 'prostori_seznam_filter.{}'.format(doctypex)

            else:
                filename = fill_template(
                    'reports/deli/prostori_seznam.ods', {'prostori_filter_list': prostori_filter_list, 'datum_danes': datum_danes},
                    output_format=doctypex)
                visible_filename = 'prostori_seznam_filter.{}'.format(doctypex)


            return FileResponse(filename, visible_filename)

        # v primeru, da so zgornji Form-i NISO ustrezno izpolnjeni
        # izvrši spodnje ukaze

        else:
            return render(request, self.template_name, {
                'form': form,
                }
            )