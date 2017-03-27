from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView	

# templated docs
from templated_docs import fill_template
from templated_docs.http import FileResponse

# Models
from ..models import ObrazecSplosno
from eda5.moduli.models import Zavihek

# Forms
from ..forms.forms import ObrazecCreateForm
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

	def form_valid(self, form):

        # pridobimo podatke iz forma
		vrsta_dokumenta = form.cleaned_data['vrsta_dokumenta']
		objava = form.cleaned_data['objava']

		# izdelamo oznako dokumenta
		# ====================================================================
		# izgled:  DOP-20170308-1223	{oznaka vrste dokumenta}-{datum}-{ura}

		# pridobimo oznako vrste dokumenta
		#---------------------------------------------------------
		oznaka_vrste_dokumenta = vrsta_dokumenta.oznaka

		# izdelamo datum dokumenta v textovni in željeni obliki
		#------------------------------------------------------------
		# leto izdelanega dokumenta
		datum_leto = objava.date().year
		datum_leto = str(datum_leto) # pretvorimo v text
		# Mesec izdelanega dokumenta ( prikaz 01, 02, ..., 12)
		datum_mesec = objava.date().month
		if datum_mesec < 10:
			datum_mesec = "0" + str(datum_mesec)
		else:
			datum_mesec = str(datum_mesec)
		# Dan izdelanega dokumenta ( prikaz 01, 02, ..., 31)
		datum_dan = objava.date().day
		if datum_dan < 10:
			datum_dan = "0" + str(datum_dan)
		else:
			datum_dan = str(datum_dan)

		datum_text = datum_leto + datum_mesec + datum_dan

		# izdelamo uro dokumenta v tekstovni obliki
		#------------------------------------------------------------
		cas_ura = objava.time().hour
		if cas_ura < 10:
			cas_ura = "0" + str(cas_ura)
		else:
			cas_ura = str(cas_ura)

		cas_minuta = objava.time().minute
		if cas_minuta < 10:
			cas_minuta = "0" + str(cas_minuta)
		else:
			cas_minuta = str(cas_minuta)

		cas_text = cas_ura + cas_minuta

		# oznaka dokumenta
		dokument_oznaka = oznaka_vrste_dokumenta + "-" + datum_text + "-" + cas_text

		# shranimo podatek o dokumentu v "form"
		form.instance.oznaka = dokument_oznaka

		return super(DopisCreateView, self).form_valid(form)



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
				'objava': obrazec.objava,
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
