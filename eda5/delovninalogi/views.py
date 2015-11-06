from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView, UpdateView

from .forms import OpraviloModelForm
from .models import Opravilo


class AppHomeView(TemplateView):
    template_name = "delovninalogi/home.html"


class OpraviloListView(ListView):
    model = Opravilo
    template_name = "delovninalogi/opravilo/list.html"


class OpraviloDetailView(DetailView):
    model = Opravilo
    template_name = "delovninalogi/opravilo/detail.html"


class OpraviloUpdateView(UpdateView):
    model = Opravilo
    form_class = OpraviloModelForm
    template_name = "delovninalogi/opravilo/update.html"
