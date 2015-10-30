from django.shortcuts import render
from django.views.generic import ListView

from .models import Modul

# mixins
from braces.views import LoginRequiredMixin


class ModulHomeView(LoginRequiredMixin, ListView):

    model = Modul
