from django.shortcuts import render
from django.utils import timezone

from templated_docs import fill_template
from templated_docs.http import FileResponse

from ..forms.forms import FormatForm

from eda5.delovninalogi.models import DelovniNalog
from eda5.planiranje.models import PlaniranoOpravilo, Plan

from django.views.generic import TemplateView
# Moduli
from eda5.moduli.models import Zavihek



def dn_view(request):

    form = FormatForm(request.POST or None)

    delovninalogi = DelovniNalog.objects.all()
    datum_danes = timezone.now().date()

    if form.is_valid():
        doctypex = form.cleaned_data['format_field']
        filename = fill_template(
            'reports/delovninalog/seznam_dn.odt', {'delovninalogi': delovninalogi, 'datum_danes': datum_danes},
            output_format=doctypex)
        visible_filename = 'seznam_dn.{}'.format(doctypex)

        return FileResponse(filename, visible_filename)

    else:
        return render(request, 'reports/delovninalog/seznam_dn.html', {'form': form})



class PrintPlanOVView(TemplateView):

    template_name = "reports/delovninalog/planirana_opravila_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PrintPlanOVView, self).get_context_data(*args, **kwargs)

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

            planirana_opravila_list = PlaniranoOpravilo.objects.filter(is_active=True).order_by(
                'plan__sklop__zap_st',
                'plan__oznaka',
                'oznaka',
            )

            # prenos podatkov za aplikacijo templated_docs

            filename = fill_template(
                'reports/delovninalog/planirana_opravila_list.odt', {'planirana_opravila_list': planirana_opravila_list, 'datum_danes': datum_danes}, output_format=doctypex)
            visible_filename = 'planirana_opravila_list.{}'.format(doctypex)

            return FileResponse(filename, visible_filename)


        # v primeru, da so zgornji Form-i NISO ustrezno izpolnjeni
        # izvrši spodnje ukaze

        else:
            return render(request, self.template_name, {
                'form': form,
                # 'deli_seznam_filter_form': deli_seznam_filter_form,
                }
            )













# def create_pdf_view(request):
#     # Create the HttpResponse object with the appropriate PDF headers.
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

#     buffer = BytesIO()

#     # Create the PDF object, using the BytesIO object as its "file."
#     p = canvas.Canvas(buffer, pagesize=A4)
#     p.line(10,10, 20, 20)
#     p.setFont("Times-Roman", 10)

#     # Draw things on the PDF. Here's where the PDF generation happens.
#     # See the ReportLab documentation for the full list of functionality.

#     delovninalogi = DelovniNalog.objects.filter()


#     p.drawString(0, 0, 'DELOVNI NALOG')
#     x = 0
#     y = 0
#     for dn in delovninalogi:
#         y= y + 15
#         p.drawString(x, y, dn.oznaka)
#         p.drawString(x+100, y, dn.opravilo.oznaka)
#         p.drawString(x+200, y, dn.opravilo.naziv)


#     # Close the PDF object cleanly.
#     p.showPage()
#     p.save()

#     # Get the value of the BytesIO buffer and write it to the response.
#     pdf = buffer.getvalue()
#     buffer.close()
#     response.write(pdf)
#     return response
