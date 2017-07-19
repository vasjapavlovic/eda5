from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Modul

# mixins
from braces.views import LoginRequiredMixin


class ModulHomeView(LoginRequiredMixin, ListView):

    model = Modul
    template_name = "moduli/modul_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ModulHomeView, self).get_context_data(*args, **kwargs)
        moduli = Modul.objects.all()
        context['moduli_list'] = moduli
        return context


class ModulDetailView(DetailView):

    model = Modul
    template_name = "moduli/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ModulDetailView, self).get_context_data(*args, **kwargs)
        modul = Modul.objects.get(id=self.get_object().pk)
        context['modul'] = modul
        return context