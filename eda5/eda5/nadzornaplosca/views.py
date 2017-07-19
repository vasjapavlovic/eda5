from django.shortcuts import render

from django.views.generic import ListView, DetailView

from .models import NadzorniSistem
from eda5.moduli.models import Zavihek


class NadzorniSistemListView(ListView):
    template_name = "nadzornaplosca/nadzorni_sistem/list/base.html"
    model = NadzorniSistem

    def get_context_data(self, *args, **kwargs):
        context = super(NadzorniSistemListView, self).get_context_data()

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="NADZORNI_SISTEM_LIST")
        context['modul_zavihek'] = modul_zavihek

        return context
