from django.shortcuts import render
from django.views.generic import ListView

from ..models import PredajaLastnine, NajemLastnine, ProdajaLastnine

# Moduli
from eda5.moduli.models import Zavihek


class PredajaLastnineListView(ListView):

	model = PredajaLastnine
	template_name = "lastnistvo/predajalastnine/list/base.html"
	queryset = PredajaLastnine.objects.order_by('-pk')

	def get_context_data(self, *args, **kwargs):
		# ukaz za dopolnitev contexta
		context = super(PredajaLastnineListView, self).get_context_data(*args, **kwargs)

		# zavihek
		modul_zavihek = Zavihek.objects.get(oznaka="predajalastnine_list")
		context['modul_zavihek'] = modul_zavihek

		return context

