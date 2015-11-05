from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView
from .models import Delilnik, Odcitek
from .viewmixins import DelilnikSearchMixin


class StevciHomeView(TemplateView):
    template_name = "stevci/home.html"


class DelilnikListView(DelilnikSearchMixin, ListView):
    template_name = "stevci/delilnik/list.html"
    model = Delilnik


class DelilnikDetailView(DetailView):
    template_name = "stevci/delilnik/detail.html"
    model = Delilnik