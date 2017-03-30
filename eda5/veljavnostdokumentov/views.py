from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView


# Veljavnost dokumentov
from .forms import VeljavnostDokumentaCreateForm, VeljavnostDokumentaUpdateForm
from .models import VeljavnostDokumenta


# Arhiv
from eda5.arhiv.models import Arhiviranje

# Moduli
from eda5.moduli.models import Zavihek


class VeljavnostDokumentaCreateView(UpdateView):
    model = Arhiviranje
    template_name = "veljavnostdokumentov/veljavnostdokumenta/create.html"
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):
        context = super(VeljavnostDokumentaCreateView, self).get_context_data(*args, **kwargs)

        # opravilo
        context['veljavnost_dokumenta_create_form'] = VeljavnostDokumentaCreateForm

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_DETAIL")
        context['modul_zavihek'] = modul_zavihek


        return context

    def post(self, request, *args, **kwargs):

        # object
        arhiviranje = Arhiviranje.objects.get(id=self.get_object().id)

        # forms
        veljavnost_dokumenta_create_form = VeljavnostDokumentaCreateForm(request.POST or None)

        # zavihek
        # modul_zavihek = Zavihek.objects.get(oznaka="VELJAVNOST_DOKUMENTA_CREATE")

        # izdelamo opravilo (!!!elemente opravilu dodamo kasneje)
        if veljavnost_dokumenta_create_form.is_valid():
            velja_od = veljavnost_dokumenta_create_form.cleaned_data['velja_od']
            velja_do = veljavnost_dokumenta_create_form.cleaned_data['velja_do']

            veljavnost_dokumenta_data = VeljavnostDokumenta.objects.create_veljavnost_dokumenta(
                arhiviranje=arhiviranje,
                velja_od=velja_od,
                velja_do=velja_do,
            )

            veljavnost_dokumenta_object = VeljavnostDokumenta.objects.get(id=veljavnost_dokumenta_data.pk)

        else:
            return render(request, self.template_name, {
                'veljavnost_dokumenta_create_form': veljavnost_dokumenta_create_form,
                # 'modul_zavihek': modul_zavihek,
                }
            )

        # če je dokument likvidiran pod delovnim nalogom:
        if arhiviranje.delovninalog:
            return HttpResponseRedirect(reverse('moduli:delovninalogi:dn_detail', kwargs={'pk': arhiviranje.delovninalog.pk}))

        else:
            return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': arhiviranje.zahtevek.pk}))


class VeljavnostDokumentaUpdateView(UpdateView):
    model = VeljavnostDokumenta
    form_class = VeljavnostDokumentaUpdateForm
    template_name = "veljavnostdokumentov/veljavnostdokumenta/update.html"

    def get_context_data(self, *args, **kwargs):
        context = super(VeljavnostDokumentaUpdateView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context