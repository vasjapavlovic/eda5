from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from django.views.generic import TemplateView, FormView

from . import forms
from .models import NarociloTelefon, NarociloPogodba, Narocilo


class NarocilaHomeView(TemplateView):
    template_name = "narocila/home.html"


class NarociloVrstaIzbiraView(FormView):
    form_class = forms.NarociloIzbiraForm


class NarociloTelefonCreateView(TemplateView):
    template_name = "narocila/narocilo/create_telefon.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NarociloTelefonCreateView, self).get_context_data(*args, **kwargs)
        context['narocilo_splosno_form'] = forms.NarociloSplosnoCreateForm
        context['narocilo_telefon_form'] = forms.NarociloTelefonCreateForm
        return context

    def post(self, request, *args, **kwargs):
        narocilo_splosno_form = forms.NarociloSplosnoCreateForm(request.POST or None)
        narocilo_telefon_form = forms.NarociloTelefonCreateForm(request.POST or None)

        if narocilo_telefon_form.is_valid():
            oseba = narocilo_telefon_form.cleaned_data['oseba']
            telefonska_stevilka = narocilo_telefon_form.cleaned_data['telefonska_stevilka']
            datum_klica = narocilo_telefon_form.cleaned_data['datum_klica']
            cas_klica = narocilo_telefon_form.cleaned_data['cas_klica']
            telefonsko_sporocilo = narocilo_telefon_form.cleaned_data['telefonsko_sporocilo']

            narocilo_telefon_data = NarociloTelefon.objects.create_narocilo_telefon(
                oseba=oseba,
                telefonska_stevilka=telefonska_stevilka,
                datum_klica=datum_klica,
                cas_klica=cas_klica,
                telefonsko_sporocilo=telefonsko_sporocilo,
            )
            narocilo_telefon = NarociloTelefon.objects.get(id=narocilo_telefon_data.pk)

        if narocilo_splosno_form.is_valid():
            narocnik = narocilo_splosno_form.cleaned_data['narocnik']
            izvajalec = narocilo_splosno_form.cleaned_data['izvajalec']
            oznaka = narocilo_splosno_form.cleaned_data['oznaka']
            predmet = narocilo_splosno_form.cleaned_data['predmet']
            datum_narocila = narocilo_splosno_form.cleaned_data['datum_narocila']
            datum_veljavnosti = narocilo_splosno_form.cleaned_data['datum_veljavnosti']
            vrednost = narocilo_splosno_form.cleaned_data['vrednost']

            Narocilo.objects.create_narocilo(
                narocilo_telefon=narocilo_telefon,
                narocnik=narocnik,
                izvajalec=izvajalec,
                oznaka=oznaka,
                predmet=predmet,
                datum_narocila=datum_narocila,
                datum_veljavnosti=datum_veljavnosti,
                vrednost=vrednost,
            )

        return HttpResponseRedirect(reverse('moduli:narocila:home'))


class NarociloPogodbaCreateView(TemplateView):
    template_name = "narocila/narocilo/create_pogodba.html"
