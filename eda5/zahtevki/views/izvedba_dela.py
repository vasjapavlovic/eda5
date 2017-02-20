# PYTHON ##############################################################


# DJANGO ##############################################################
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView
from django.utils import timezone


# INTERNO ##############################################################
# Zahtevek Osnova
from ..forms import ZahtevekCreateForm
from ..models import Zahtevek

# Zahtevek Izvedba Del
from ..forms import ZahtevekIzvedbaDelCreateForm, ZahtevekIzvedbaDelUpdateForm
from ..models import ZahtevekIzvedbaDela


# UVOŽENO ##############################################################

# Moduli
from eda5.moduli.models import Zavihek

# Delovni Nalogi
from eda5.delovninalogi.forms import VzorecOpravilaIzbiraForm
from eda5.delovninalogi.models import Opravilo, VzorecOpravila

# Planiranje
from eda5.planiranje.models import SkupinaPlanov, Plan, PlaniranoOpravilo


class ZahtevekIzvedbaDelCreateView(TemplateView):
    template_name = "zahtevki/zahtevek/create_izvedba_del.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ZahtevekIzvedbaDelCreateView, self).get_context_data(*args, **kwargs)
        context['zahtevek_splosno_form'] = ZahtevekCreateForm
        context['zahtevek_izvedba_del_form'] = ZahtevekIzvedbaDelCreateForm

        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_IZVEDBA_DEL_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *Args, **kwargs):

        zahtevek_splosno_form = ZahtevekCreateForm(request.POST or None)
        zahtevek_izvedba_del_form = ZahtevekIzvedbaDelCreateForm(request.POST or None)
        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_IZVEDBA_DEL_CREATE")

        if zahtevek_splosno_form.is_valid():
            oznaka = zahtevek_splosno_form.cleaned_data['oznaka']
            naziv = zahtevek_splosno_form.cleaned_data['naziv']
            rok_izvedbe = zahtevek_splosno_form.cleaned_data['rok_izvedbe']
            nosilec = zahtevek_splosno_form.cleaned_data['nosilec']

            zahtevek_splosno_data = Zahtevek.objects.create_zahtevek(
                oznaka=oznaka,
                vrsta=3,
                naziv=naziv,
                rok_izvedbe=rok_izvedbe,
                nosilec=nosilec,
                status=3,
            )
            zahtevek = Zahtevek.objects.get(id=zahtevek_splosno_data.pk)

        else:
            return render(request, self.template_name, {
                'zahtevek_splosno_form': zahtevek_splosno_form,
                'zahtevek_izvedba_del_form': zahtevek_izvedba_del_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        if zahtevek_izvedba_del_form.is_valid():

            is_zakonska_obveza = zahtevek_izvedba_del_form.cleaned_data['is_zakonska_obveza']

            ZahtevekIzvedbaDela.objects.create_zahtevek_sestanek(
                zahtevek=zahtevek,
                is_zakonska_obveza=is_zakonska_obveza,
            )
        else:
            return render(request, self.template_name, {
                'zahtevek_splosno_form': zahtevek_splosno_form,
                'zahtevek_izvedba_del_form': zahtevek_izvedba_del_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk}))


class PodzahtevekIzvedbaDelCreateView(UpdateView):
    model = Zahtevek
    fields = ('id', )
    template_name = "zahtevki/zahtevek/create_izvedba_del.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PodzahtevekIzvedbaDelCreateView, self).get_context_data(*args, **kwargs)
        context['zahtevek_splosno_form'] = ZahtevekCreateForm
        context['zahtevek_izvedba_del_form'] = ZahtevekIzvedbaDelCreateForm

        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_IZVEDBA_DEL_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *Args, **kwargs):

        zahtevek_parent = Zahtevek.objects.get(id=self.get_object().id)

        zahtevek_splosno_form = ZahtevekCreateForm(request.POST or None)
        zahtevek_izvedba_del_form = ZahtevekIzvedbaDelCreateForm(request.POST or None)
        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_IZVEDBA_DEL_CREATE")

        if zahtevek_splosno_form.is_valid():
            oznaka = zahtevek_splosno_form.cleaned_data['oznaka']
            naziv = zahtevek_splosno_form.cleaned_data['naziv']
            rok_izvedbe = zahtevek_splosno_form.cleaned_data['rok_izvedbe']
            nosilec = zahtevek_splosno_form.cleaned_data['nosilec']

            zahtevek_splosno_data = Zahtevek.objects.create_zahtevek(
                oznaka=oznaka,
                vrsta=3,
                naziv=naziv,
                rok_izvedbe=rok_izvedbe,
                nosilec=nosilec,
                status=3,
                zahtevek_parent=zahtevek_parent
            )
            zahtevek = Zahtevek.objects.get(id=zahtevek_splosno_data.pk)

        else:
            return render(request, self.template_name, {
                'zahtevek_splosno_form': zahtevek_splosno_form,
                'zahtevek_izvedba_del_form': zahtevek_izvedba_del_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        if zahtevek_izvedba_del_form.is_valid():

            is_zakonska_obveza = zahtevek_izvedba_del_form.cleaned_data['is_zakonska_obveza']

            ZahtevekIzvedbaDela.objects.create_zahtevek_sestanek(
                zahtevek=zahtevek,
                is_zakonska_obveza=is_zakonska_obveza,
            )
        else:
            return render(request, self.template_name, {
                'zahtevek_splosno_form': zahtevek_splosno_form,
                'zahtevek_izvedba_del_form': zahtevek_izvedba_del_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk}))


class ZahtevekUpdateIzvedbaView(UpdateView):
    model = ZahtevekIzvedbaDela
    form_class = ZahtevekIzvedbaDelUpdateForm
    template_name = "zahtevki/zahtevek/update_zahtevek_izvedba.html"


