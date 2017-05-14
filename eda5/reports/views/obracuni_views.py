# Python
# Django
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import TemplateView, DetailView

# Templated Docs
from templated_docs import fill_template
from templated_docs.http import FileResponse

#Models
from eda5.deli.models import Podskupina, DelStavbe
from eda5.delovninalogi.models import DelovniNalog
from eda5.etaznalastnina.models import LastniskaSkupina, Program
from eda5.moduli.models import Zavihek

# Forms
from eda5.reports.forms import FormatForm, DeliSeznamFilterForm, ObracunFilterForm




###########################################################
# SEZNAM DELOV STAVBE PO PROGRAMIH - PRINT
###########################################################
class ObracunMesecPrintView(TemplateView):

    template_name = "reports/obracuni/deli_seznam_filter.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ObracunMesecPrintView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        context['form'] = FormatForm
        context['obracun_filter_form'] = ObracunFilterForm

        return context


    def post(self, request, *args, **kwargs):

        ###########################################################################
        # FORMS
        ###########################################################################

        form = FormatForm(request.POST or None)
        obracun_filter_form = ObracunFilterForm(request.POST or None)

        form_is_valid = False
        obracun_filter_form_is_valid = False

        ###########################################################################
        # PRIDOBIMO PODATKE
        ###########################################################################

        if form.is_valid():
            doctypex = form.cleaned_data['format_field']
            form_is_valid = True

        if obracun_filter_form_is_valid.is_valid():
            obdobje_leto = obracun_filter_form_is_valid.cleaned_data['obdobje_leto']
            obdobje_mesec = obracun_filter_form_is_valid.cleaned_data['obdobje_mesec']
            obracun_filter_form_is_valid = True

        #Če so formi pravilno izpolnjeni

        if form_is_valid == True and obracun_filter_form_is_valid == True:
            ###########################################################################
            # UKAZI
            ###########################################################################

            # pridobimo današnji datum za izpis na izpisu

            datum_danes = timezone.now().date()

            # izdelamo seznam delovnih nalogov glede na izbrane filtre (Mesečni obračun)
            delovninalog_filtered_list = DelovniNalog.objects.filter(
                opravilo__narocilo__izvajalec__davcna_st="97041823",  # prikažemo samo delovne naloge za izvajalca EDAFM
                # filter glede na izbrano leto,
                # filter glede na izbran mesec,
            )

            return HttpResponseRedirect(reverse('moduli:reports:zahtevek_detail', kwargs={'pk': zahtevek.pk}))




            return FileResponse(filename, visible_filename)

        # v primeru, da so zgornji Form-i NISO ustrezno izpolnjeni
        # izvrši spodnje ukaze

        else:
            return render(request, self.template_name, {
                'form': form,
                'deli_seznam_filter_form': deli_seznam_filter_form,
                }
            )
