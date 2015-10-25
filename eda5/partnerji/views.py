from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import PartnerCreateForm, PartnerUpdateForm
from .models import Partner

# mixins
from .viewmixins import PartnerSearchMixin


class PartnerListView(PartnerSearchMixin, ListView):
    model = Partner

    # order_by
    def get_queryset(self):
        queryset = super(PartnerListView, self).get_queryset()
        queryset = queryset.order_by('kratko_ime')
        return queryset


class PartnerDetailView(DetailView):
    model = Partner


class PartnerCreateView(CreateView):
    model = Partner
    form_class = PartnerCreateForm


class PartnerUpdateView(UpdateView):
    model = Partner
    form_class = PartnerUpdateForm
