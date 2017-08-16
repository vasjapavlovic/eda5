# Python
# Django
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
# Models
from .models import VeljavnostDokumenta
from eda5.arhiv.models import Arhiviranje
from eda5.moduli.models import Zavihek
# Managers
# Forms
from .forms import VeljavnostDokumentaCreateForm, VeljavnostDokumentaUpdateForm
from eda5.racunovodstvo.forms.vrsta_stroska_forms import VrstaStroskaIzbiraVeljavnostDokumentovForm


class VeljavnostDokumentaCreateView(UpdateView):
    model = Arhiviranje
    template_name = "veljavnostdokumentov/veljavnostdokumenta/create.html"
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):
        context = super(VeljavnostDokumentaCreateView, self).get_context_data(*args, **kwargs)

        context['veljavnost_dokumenta_create_form'] = VeljavnostDokumentaCreateForm
        context['vrsta_stroska_izbira_form'] = VrstaStroskaIzbiraVeljavnostDokumentovForm

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        sledenje_dokumentaciji_seznam = VeljavnostDokumenta.objects.all()
        context['sledenje_dokumentaciji_seznam'] = sledenje_dokumentaciji_seznam


        return context

    def post(self, request, *args, **kwargs):

        # object
        arhiviranje = Arhiviranje.objects.get(id=self.get_object().id)

        # forms
        veljavnost_dokumenta_create_form = VeljavnostDokumentaCreateForm(request.POST or None)
        vrsta_stroska_izbira_form = VrstaStroskaIzbiraVeljavnostDokumentovForm(request.POST or None)


        if vrsta_stroska_izbira_form.is_valid():
            vrsta_stroska = vrsta_stroska_izbira_form.cleaned_data['vrsta_stroska']

        else:
            return render(request, self.template_name, {
                'veljavnost_dokumenta_create_form': veljavnost_dokumenta_create_form,
                'vrsta_stroska_izbira_form': vrsta_stroska_izbira_form,
                }
            )

        if veljavnost_dokumenta_create_form.is_valid():
            stavba = veljavnost_dokumenta_create_form.cleaned_data['stavba']
            velja_od = veljavnost_dokumenta_create_form.cleaned_data['velja_od']
            velja_do = veljavnost_dokumenta_create_form.cleaned_data['velja_do']

            veljavnost_dokumenta_data = VeljavnostDokumenta.objects.create_veljavnost_dokumenta(
                arhiviranje=arhiviranje,
                stavba=stavba,
                vrsta_stroska=vrsta_stroska,
                velja_od=velja_od,
                velja_do=velja_do,
            )

            veljavnost_dokumenta_object = VeljavnostDokumenta.objects.get(id=veljavnost_dokumenta_data.pk)

        else:
            return render(request, self.template_name, {
                'veljavnost_dokumenta_create_form': veljavnost_dokumenta_create_form,
                'vrsta_stroska_izbira_form': vrsta_stroska_izbira_form,
                # 'modul_zavihek': modul_zavihek,
                }
            )




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