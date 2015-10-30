from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView
from .models import DelStavbe, Skupina, Element


class DelHomeView(TemplateView):
    template_name = "deli/home.html"


class DelListView(ListView):
    template_name = "deli/list.html"
    model = Skupina


class DelDetailView(DetailView):
    template_name = "deli/del_detail.html"
    model = DelStavbe


class ElementDetailView(DetailView):
    template_name = "deli/element_detail.html"
    model = Element
