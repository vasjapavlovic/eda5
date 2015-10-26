from django.shortcuts import render

from django.views.generic import TemplateView


class RacunovodstvoHomeView(TemplateView):
    template_name = "racunovodstvo/home.html"
