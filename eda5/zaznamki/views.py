from django.core.urlresolvers import reverse, reverse_lazy

from django.views.generic import UpdateView


from .forms import ZaznamekUpdateForm
from .models import Zaznamek


class ZaznamekUpdateFromZahtevekView(UpdateView):
    model = Zaznamek
    form_class = ZaznamekUpdateForm
    template_name = "zaznamki/zaznamek/update.html"
