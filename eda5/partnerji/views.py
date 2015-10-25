from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView

from .forms import PartnerCreateForm, PartnerUpdateForm
from .forms import OsebaCreateForm, OsebaUpdateForm

from .models import Partner, Oseba

# mixins
from .viewmixins import PartnerSearchMixin


class PartnerHomeView(TemplateView):
    template_name="partnerji/home.html"


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


class OsebaCreateView(CreateView):
    model = Oseba
    form_class = OsebaCreateForm


class OsebaUpdateView(CreateView):
    model = Oseba
    form_class = OsebaUpdateForm
