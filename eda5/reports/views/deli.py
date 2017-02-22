from django.shortcuts import render
from django.utils import timezone

from django.views.generic import TemplateView

from templated_docs import fill_template
from templated_docs.http import FileResponse




# Deli
from eda5.deli.models import DelStavbe

# Etažna Lastnina
from eda5.etaznalastnina.models import LastniskaSkupina, Program

# Reports
from eda5.reports.forms import FormatForm, DeliSeznamFilterForm




def DeliSeznamPrintView(request):

    form = FormatForm(request.POST or None)
    deli_seznam_filter_form = DeliSeznamFilterForm(request.POST or None)

    datum_danes = timezone.now().date()



    form_is_valid = False
    deli_seznam_filter_form_is_valid = False



    if form.is_valid():
        doctypex = form.cleaned_data['format_field']
        form_is_valid = True

    if deli_seznam_filter_form.is_valid():
        program = deli_seznam_filter_form.cleaned_data['program']
        deli_filter_list = DelStavbe.objects.filter(lastniska_skupina__program=program)
        deli_seznam_filter_form_is_valid = True

    #Če so formi pravilno izpolnjeni

    if form_is_valid == True and deli_seznam_filter_form_is_valid == True:

        filename = fill_template(
            'reports/deli/deli_seznam.odt', {'deli_filter_list': deli_filter_list, 'datum_danes': datum_danes, 'program': program},
            output_format=doctypex)
        visible_filename = 'deli_seznam_filter.{}'.format(doctypex)

        return FileResponse(filename, visible_filename)

    else:
        return render(request, 'reports/deli/deli_seznam_filter.html', {'form': form, 'deli_seznam_filter_form':deli_seznam_filter_form})
