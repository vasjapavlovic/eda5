from django.shortcuts import render
from django.utils import timezone

from templated_docs import fill_template
from templated_docs.http import FileResponse

from eda5.reports.forms import FormatForm

from eda5.delovninalogi.models import DelovniNalog
from eda5.planiranje.models import PlaniranoOpravilo, Plan

from django.views.generic import TemplateView


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


def PrintPlanOVView(request):

    form = FormatForm(request.POST or None)

    plan_list = Plan.objects.all()
    planirana_opravila_list = PlaniranoOpravilo.objects.all()
    datum_danes = timezone.now().date()

    if form.is_valid():
        doctypex = form.cleaned_data['format_field']
        filename = fill_template(
            'reports/delovninalog/planirana_opravila_list.odt', {'plan_list': plan_list, 'datum_danes': datum_danes},
            output_format=doctypex)
        visible_filename = 'planirana_opravila_list.{}'.format(doctypex)

        return FileResponse(filename, visible_filename)

    else:
        return render(request, 'reports/delovninalog/planirana_opravila_list.html', {'form': form})



















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

