# PYTHON ##############################################################


# DJANGO ##############################################################
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
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
from eda5.delovninalogi.models import Opravilo


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
            narocilo = zahtevek_splosno_form.cleaned_data['narocilo']
            nosilec = zahtevek_splosno_form.cleaned_data['nosilec']

            zahtevek_splosno_data = Zahtevek.objects.create_zahtevek(
                oznaka=oznaka,
                vrsta=3,
                naziv=naziv,
                rok_izvedbe=rok_izvedbe,
                narocilo=narocilo,
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
            narocilo = zahtevek_splosno_form.cleaned_data['narocilo']
            nosilec = zahtevek_splosno_form.cleaned_data['nosilec']

            zahtevek_splosno_data = Zahtevek.objects.create_zahtevek(
                oznaka=oznaka,
                vrsta=3,
                naziv=naziv,
                rok_izvedbe=rok_izvedbe,
                narocilo=narocilo,
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


class OpraviloCreateFromVzorecView(UpdateView):
    model = Zahtevek
    template_name = "delovninalogi/opravilo/create_from_vzorec_opravila.html"
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):
        context = super(OpraviloCreateFromVzorecView, self).get_context_data(*args, **kwargs)

        # vzorec opravila
        context['vzorec_opravila_izbira_form'] = VzorecOpravilaIzbiraForm

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="OPRAVILO_FROM_VZOREC_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        # object
        zahtevek = Zahtevek.objects.get(id=self.get_object().id)

        # forms
        vzorec_opravila_izbira_form = VzorecOpravilaIzbiraForm(request.POST or None)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="OPRAVILO_FROM_VZOREC_CREATE")

        # izdelamo opravilo (!!!elemente opravilu dodamo kasneje)
        if vzorec_opravila_izbira_form.is_valid():
            vzorec_opravila = vzorec_opravila_izbira_form.cleaned_data['vzorec_opravila']

            # nova oznaka opravila
            try:
                leto = timezone.now().date().year
                zap_st = Opravilo.objects.all().count()
                zap_st = zap_st + 1
            except:
                zap_st = 1

            nova_oznaka = "OPR-%s-%s" % (leto, zap_st)  #

            # iz VzorecOpravila poberemo podatke
            oznaka = nova_oznaka
            naziv = vzorec_opravila.naziv
            rok_izvedbe = timezone.now().date()  # rok izvedbe izhaja iz zadnjega dodanega + perioda
            narocilo = vzorec_opravila.narocilo
            nosilec = vzorec_opravila.nosilec
            planirano_opravilo = vzorec_opravila.planirano_opravilo
            element_list = vzorec_opravila.element.all()
            print(element_list)

            opravilo_data = Opravilo.objects.create_opravilo(
                oznaka=oznaka,
                naziv=naziv,
                rok_izvedbe=rok_izvedbe,
                narocilo=narocilo,
                zahtevek=zahtevek,
                nosilec=nosilec,
                planirano_opravilo=planirano_opravilo,
            )

            opravilo_object = Opravilo.objects.get(id=opravilo_data.pk)

            # shranimo še elemente, ki so v ManyToMany relaciji z opravilom
            opravilo_object.element = element_list
            opravilo_object.save()

        else:
            return render(request, self.template_name, {
                'vzorec_opravila_izbira_form': vzorec_opravila_izbira_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk}))
