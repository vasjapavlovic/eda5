# # PYTHON ##############################################################
# import os


# # DJANGO ##############################################################
# from django.conf import settings
# from django.core.urlresolvers import reverse
# from django.http import HttpResponseRedirect
# from django.shortcuts import render
# from django.views.generic import TemplateView, ListView, DetailView, UpdateView


# # INTERNO ##############################################################
# # Zahtevek Osnova
# from .forms import ZahtevekCreateForm, ZahtevekUpdateForm, ZahtevekIzbiraForm
# from .models import Zahtevek

# # Zahtevek Škodni Dogodek
# from .forms import ZahtevekSkodniDogodekUpdateForm
# from .models import ZahtevekSkodniDogodek

# # Zahtevek Sestanek
# from .forms import ZahtevekSestanekCreateForm, ZahtevekSestanekUpdateForm
# from .models import ZahtevekSestanek

# # Zahtevek Izvedba Del
# from .forms import ZahtevekIzvedbaDelCreateForm, ZahtevekIzvedbaDelUpdateForm
# from .models import ZahtevekIzvedbaDela


# # UVOŽENO ##############################################################
# # Arhiv
# from eda5.arhiv.forms import ArhiviranjeZahtevekForm
# from eda5.arhiv.models import Arhiviranje, ArhivMesto

# # Delovni Nalogi
# from eda5.delovninalogi.forms import OpraviloCreateForm, OpraviloElementUpdateForm
# from eda5.delovninalogi.models import Opravilo

# # Moduli
# from eda5.moduli.models import Zavihek

# # Zaznamki
# from eda5.zaznamki.forms import ZaznamekForm
# from eda5.zaznamki.models import Zaznamek



# class ZahtevekUpdateSkodniView(UpdateView):
#     model = ZahtevekSkodniDogodek
#     form_class = ZahtevekSkodniDogodekUpdateForm
#     template_name = "zahtevki/zahtevek/update_zahtevek_skodni.html"