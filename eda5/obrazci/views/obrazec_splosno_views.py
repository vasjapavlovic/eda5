from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView	

# dodatki
from templated_docs import fill_template
from templated_docs.http import FileResponse

# relative imports
from ..models import ObrazecSplosno
from ..forms.forms import ObrazecCreateForm

# absolute imports
from eda5.moduli.models import Zavihek
from eda5.reports.forms import FormatForm


class DopisCreateView(CreateView):
	
	model = ObrazecSplosno
	template_name = "obrazci/dopis/create/create.html"
	form_class = ObrazecCreateForm

	def get_context_data(self, *args, **kwargs):
		context = super(DopisCreateView, self).get_context_data(*args, **kwargs)
		# context
		#-------------------------------------------------------------

		modul_zavihek = Zavihek.objects.get(oznaka="dopis_create")
		context['modul_zavihek'] = modul_zavihek

		#-------------------------------------------------------------
		# end context
		return context


class DopisListView(ListView):
	
	model = ObrazecSplosno
	template_name = "obrazci/dopis/list/base.html"

	def get_context_data(self, *args, **kwargs):
		context = super(DopisListView, self).get_context_data(*args, **kwargs)
		# context
		#-------------------------------------------------------------

		modul_zavihek = Zavihek.objects.get(oznaka="dopis_list")
		context['modul_zavihek'] = modul_zavihek

		#-------------------------------------------------------------
		# end context
		return context

class DopisDetailView(DetailView):
	
	model = ObrazecSplosno
	template_name = 'obrazci/dopis/detail/base.html'

	def get_context_data(self, *args, **kwargs):
		context = super(DopisDetailView, self).get_context_data(*args, **kwargs)
		# context
		#-------------------------------------------------------------

		modul_zavihek = Zavihek.objects.get(oznaka="dopis_detail")
		context['modul_zavihek'] = modul_zavihek

		# from za izbiro formata izvoza
		context['form'] = FormatForm 

		obrazec = ObrazecSplosno.objects.get(id=self.get_object().id)
		context['obrazec'] = obrazec

		#-------------------------------------------------------------
		# end context
		return context

	def post(self, request, *args, **kwargs):

		###########################################################################
        # FORMS
        ###########################################################################
		form = FormatForm(request.POST or None)
		form_is_valid = False

        ###########################################################################
        # PRIDOBIMO PODATKE
        ###########################################################################
		if form.is_valid():
			doctypex = form.cleaned_data['format_field']
			form_is_valid = True

		povezava = '<text:a xlink:href="http://site.ru" office:target-frame-name="_top" xlink:show="replace"></text:a>'

        # instanca
		obrazec = ObrazecSplosno.objects.get(id=self.get_object().id)

		if form_is_valid == True:
            ###########################################################################
            # UKAZI
            ###########################################################################
		
			# iz instance pridobimo željene podatke
			# ki jih bomo uporabili v izpisu
			izpis_data = {
				'vrsta_dokumenta': obrazec.vrsta_dokumenta.naziv,
				'oznaka': obrazec.oznaka,
				'datum': obrazec.datum,
				'zadeva': obrazec.zadeva,
				'vsebina': obrazec.vsebina,
				'posiljatelj': obrazec.posiljatelj,
				'naslovnik': obrazec.naslovnik,
				'oseba_izdelal': obrazec.oseba_izdelal,
				'oseba_odgovorna': obrazec.oseba_odgovorna,
				'priloge': obrazec.priloge,
				'povezava': povezava
			}

			# izdelamo izpis
			filename = fill_template(
				# oblikovna datoteka v formatu .odb, ki jo želimo uporabiti
	            'obrazci/dopis/dopis_01.odt', 
	            # podatki za uporabo v oblikovni datoteki	
	            izpis_data,						
	            output_format=doctypex
	        )

			visible_filename = 'dopis.{}'.format(doctypex)

			return FileResponse(filename, visible_filename)

        # v primeru, da so zgornji Form-i NISO ustrezno izpolnjeni
        # izvrši spodnje ukaze

		else:
			return render(request, self.template_name, {
                'form': form,
                }
            )
