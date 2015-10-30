from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView
from .models import DelStavbe, Skupina


class DelHomeView(TemplateView):
    template_name = "deli/home.html"


class DelListView(ListView):
    template_name = "deli/list.html"
    model = Skupina


class DelDetailView(DetailView):
    template_name = "deli/detail.html"
    model = DelStavbe
