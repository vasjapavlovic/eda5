from django.shortcuts import render

from django.views.generic import TemplateView, ListView, CreateView
from .models import Dokument
from .forms import PrejetaPostaCreateForm


class PostaHomeView(TemplateView):
    template_name = "posta/home.html"


class PostaLikvidacijaListView(ListView):
    model = Dokument
    template_name = "posta/dokument_likvidacija.html"

    def get_queryset(self):
        queryset = super(PostaLikvidacijaListView, self).get_queryset()
        queryset = queryset.filter(is_likvidiran=False)
        return queryset


class PostaLikvidiranListView(ListView):
    model = Dokument
    template_name = "posta/dokument_likvidiran.html"

    def get_queryset(self):
        queryset = super(PostaLikvidiranListView, self).get_queryset()
        queryset = queryset.filter(is_likvidiran=True)
        return queryset


class PostaCreateView(CreateView):
    model = Dokument
    form_class = PrejetaPostaCreateForm
