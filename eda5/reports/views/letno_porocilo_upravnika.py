# Python


# Django
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.db.models import Q, F, Sum
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, UpdateView

# Mixins
from braces.views import LoginRequiredMixin

# Models
from ..models import Razdelilnik, StrosekRazdelilnik
from eda5.arhiv.models import ArhivMesto, Arhiviranje
from eda5.moduli.models import Zavihek
from eda5.racunovodstvo.models import Strosek
from eda5.zahtevki.models import Zahtevek
from eda5.zaznamki.models import Zaznamek

# Forms
from ..forms.razdelilnik_forms import RazdelilnikSearchForm, RazdelilnikCreateFromZahtevekForm
from eda5.arhiv.forms import ArhiviranjeZahtevekForm
from eda5.reports.forms import FormatForm
from eda5.zaznamki.forms import ZaznamekForm

# Views
from eda5.core.views import FilteredListView

# Templated docs
from templated_docs import fill_template
from templated_docs.http import FileResponse


class PorocanjeStroskiView(LoginRequiredMixin, TemplateView):
    template_name = "reports/letno_porocilo_upravnika/porocanje_stroski.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PorocanjeStroskiView, self).get_context_data(*args, **kwargs)


        return context


    def post(self, request, *args, **kwargs):

        pass
