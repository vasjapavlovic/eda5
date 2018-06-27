from django.db.models import Q
from django.shortcuts import render
from django.views.generic import CreateView, ListView, TemplateView


# Moduli
from eda5.moduli.models import Zavihek

from .models import SklopKljucev, Kljuc, PredajaKljuca



class PredajaKljucaListView(ListView):
	model = PredajaKljuca
	template_name = "kljuci/predaja_kljuca/list/base.html"

	def get_context_data(self, *args, **kwargs):
		context = super(PredajaKljucaListView, self).get_context_data(*args, **kwargs)

        # content
		modul_zavihek = Zavihek.objects.get(oznaka="PREDAJA_KLJUCA_LIST")
		context['modul_zavihek'] = modul_zavihek

		return context

	def get_queryset(self, *args, **kwargs):
		queryset = super(PredajaKljucaListView, self).get_queryset(*args, **kwargs)


		# prikaži samo daljince
		queryset = queryset.filter(kljuc__vrsta_kljuca=2)

		# prikaži samo oddane daljince
		# odpisane daljince
		# daljince za vzdrževalce
		queryset = queryset.filter(Q(vracilo_datum__isnull=True) | Q(kljuc__status_kljuca=2) | Q(kljuc__status_kljuca=3))

		# sortiranje po oznaki ključa od 1 -->
		queryset = queryset.order_by('kljuc__oznaka')


		return queryset





# class PredajaCreateView(CreateView):
#     model = PredajaLastnine
#     template_name = "predaja_lastnine/predajalastnine/create.html"
#     fields = "__all__"
