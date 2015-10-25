from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Partner

# mixins
from .viewmixins import PartnerSearchMixin


class PartnerListView(PartnerSearchMixin, ListView):

    model = Partner
