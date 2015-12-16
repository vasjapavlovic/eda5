from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Modul

# mixins
from braces.views import LoginRequiredMixin


class ModulHomeView(LoginRequiredMixin, ListView):

    model = Modul
    template_name = "moduli/modul_list.html"


class ModulDetailView(DetailView):

    model = Modul
    template_name = "moduli/detail.html"
