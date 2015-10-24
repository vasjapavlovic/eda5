from django.shortcuts import render

from django.views.generic import ListView

from .models import Modul


class ModulListView(ListView):

    model = Modul
