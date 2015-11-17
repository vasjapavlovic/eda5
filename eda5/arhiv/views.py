from django.shortcuts import render
from django.views.generic import ListView

from .models import Arhiviranje, ArhivMesto


class ArhiviranjeListView(ListView):
    model = Arhiviranje
    template_name = "arhiv/arhiviranje/list/base.html"