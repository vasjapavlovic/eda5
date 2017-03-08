from django.shortcuts import render
from django.views.generic import ListView

from .models import Arhiviranje, ArhivMesto
from .forms import ArhiviranjeSearchForm


class ArhiviranjeListView(ListView):
    model = Arhiviranje
    template_name = "arhiv/arhiviranje/list/base.html"



# POPUP
# dodatek za filtriranje prikazanega seznama
from eda5.core.views import FilteredListView
class ArhiviranjePopUpListView(FilteredListView):
    model = Arhiviranje
    form_class= ArhiviranjeSearchForm
    template_name = "arhiv/arhiviranje/popup/popup_base.html"
    paginate_by = 10