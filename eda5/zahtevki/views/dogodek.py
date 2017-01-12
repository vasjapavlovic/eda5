# # PYTHON ##############################################################
# import os


# # DJANGO ##############################################################
# from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, UpdateView


# # INTERNO ##############################################################
# # Zahtevek Osnova
# from .forms import ZahtevekCreateForm, ZahtevekUpdateForm, ZahtevekIzbiraForm
from eda5.zahtevki.models import Zahtevek

# # Zahtevek Škodni Dogodek
from eda5.dogodki.forms import DogodekCreateForm
from eda5.dogodki.models import Dogodek
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
from eda5.moduli.models import Zavihek

# # Zaznamki
# from eda5.zaznamki.forms import ZaznamekForm
# from eda5.zaznamki.models import Zaznamek



# class ZahtevekUpdateSkodniView(UpdateView):
#     model = ZahtevekSkodniDogodek
#     form_class = ZahtevekSkodniDogodekUpdateForm
#     template_name = "zahtevki/zahtevek/update_zahtevek_skodni.html"


class DogodekCreateView(UpdateView):
    model = Zahtevek
    template_name = "dogodki/dogodek/create_from_zahtevek.html"
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):
        context = super(DogodekCreateView, self).get_context_data(*args, **kwargs)

        # opravilo
        context['dogodek_create_form'] = DogodekCreateForm
        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="DOGODEK_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        # object
        zahtevek = Zahtevek.objects.get(id=self.get_object().id)
        # forms
        dogodek_create_form = DogodekCreateForm(request.POST or None)
        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="DOGODEK_CREATE")

        # izdelamo predajo
        if dogodek_create_form.is_valid():
            datum_dogodka = dogodek_create_form.cleaned_data['datum_dogodka']
            cas_dogodka = dogodek_create_form.cleaned_data['cas_dogodka']
            opis_dogodka = dogodek_create_form.cleaned_data['opis_dogodka']
            is_potrebna_prijava_policiji = dogodek_create_form.cleaned_data['is_potrebna_prijava_policiji']
            is_nastala_skoda = dogodek_create_form.cleaned_data['is_nastala_skoda']
            povzrocitelj = dogodek_create_form.cleaned_data['povzrocitelj']


            Dogodek.objects.create_dogodek(
                datum_dogodka=datum_dogodka,
                cas_dogodka=cas_dogodka,
                opis_dogodka=opis_dogodka,
                is_potrebna_prijava_policiji=is_potrebna_prijava_policiji,
                is_nastala_skoda=is_nastala_skoda,
                povzrocitelj=povzrocitelj,
                zahtevek=zahtevek
            )

        else:

            return render(request, self.template_name, {
                'dogodek_create_form': dogodek_create_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk}))


