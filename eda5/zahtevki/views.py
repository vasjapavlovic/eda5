from django.shortcuts import render

from django.views.generic import TemplateView


class ZahtevkiHomeView(TemplateView):
    template_name = "zahtevki/home.html"


