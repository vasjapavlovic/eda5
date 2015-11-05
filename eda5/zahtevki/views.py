from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView
from .models import Zahtevek


class ZahtevekHomeView(TemplateView):
    template_name = "zahtevki/home.html"


class ZahtevekListView(ListView):
    model = Zahtevek
    template_name = "zahtevki/zahtevek/list.html"


class ZahtevekDetailView(DetailView):
    model = Zahtevek
    template_name = "zahtevki/zahtevek/detail.html"
