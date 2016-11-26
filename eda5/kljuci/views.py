from django.shortcuts import render
from django.views.generic import CreateView, ListView, TemplateView

# Moduli
from eda5.moduli.models import Zavihek

from .models import SklopKljucev, Kljuc, PredajaKljuca



class PredajaKljucaListView(ListView):
	model = PredajaKljuca
	template_name = "kljuci/predaja_kljuca/list/base.html"

	def get_context_data(self, *args, **kwargs):
		context = super(PredajaListView, self).get_context_data(*args, **kwargs)

        # content
		modul_zavihek = Zavihek.objects.get(oznaka="PREDAJA_KLJUCA_LIST")
		context['modul_zavihek'] = modul_zavihek

		return context




# class PredajaCreateView(CreateView):
#     model = PredajaLastnine
#     template_name = "predaja_lastnine/predajalastnine/create.html"
#     fields = "__all__"

