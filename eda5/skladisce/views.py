from django.shortcuts import render

from django.views.generic import TemplateView, ListView, CreateView

from .forms import DobavaCreateForm
from .models import Dobava


class SkladisceHomeView(TemplateView):
    template_name = "skladisce/home.html"


class DobavaListView(ListView):
    model = Dobava
    template_name = "skladisce/dobava/list.html"


class DobavaCreateView(CreateView):
    model = Dobava
    template_name = "skladisce/dobava/create.html"
    form_class = DobavaCreateForm
