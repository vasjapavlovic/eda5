from django.shortcuts import render

from django.views.generic import CreateView, UpdateView, DetailView, ListView


from .forms import IceCreamStoreCreateForm
from .forms import IceCreamStoreUpdateForm
from .models import IceCreamStore

# mixins
from .viewmixins import StoresSearchMixin


class IceCreamStoreListView(StoresSearchMixin, ListView):
    model = IceCreamStore


class IceCreamStoreCreateView(CreateView):
    model = IceCreamStore
    form_class = IceCreamStoreCreateForm


class IceCreamStoreUpdateView(UpdateView):
    model = IceCreamStore
    form_class = IceCreamStoreUpdateForm


class IceCreamStoreDetailView(DetailView):
    model = IceCreamStore
