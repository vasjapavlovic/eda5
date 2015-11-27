from django.shortcuts import render
from django.views.generic import CreateView, ListView, TemplateView

from .models import PredajaLastnine


class PredajaLastnineHomeView(TemplateView):
    template_name = "predaja_lastnine/home.html"


class PredajaListView(ListView):
    model = PredajaLastnine
    template_name = "predaja_lastnine/predajalastnine/list.html"


class PredajaCreateView(CreateView):
    model = PredajaLastnine
    template_name = "predaja_lastnine/predajalastnine/create.html"
    fields = "__all__"
