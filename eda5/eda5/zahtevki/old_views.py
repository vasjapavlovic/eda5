# PYTHON ##############################################################
import os


# DJANGO ##############################################################
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, UpdateView


# INTERNO ##############################################################
# Zahtevek Osnova
from .forms import ZahtevekCreateForm, ZahtevekUpdateForm, ZahtevekIzbiraForm
from .models import Zahtevek

# Zahtevek Škodni Dogodek
from .forms import ZahtevekSkodniDogodekUpdateForm
from .models import ZahtevekSkodniDogodek

# Zahtevek Sestanek
from .forms import ZahtevekSestanekCreateForm, ZahtevekSestanekUpdateForm
from .models import ZahtevekSestanek

# Zahtevek Izvedba Del
from .forms import ZahtevekIzvedbaDelCreateForm, ZahtevekIzvedbaDelUpdateForm
from .models import ZahtevekIzvedbaDela


# UVOŽENO ##############################################################
# Arhiv
from eda5.arhiv.forms import ArhiviranjeZahtevekForm
from eda5.arhiv.models import Arhiviranje, ArhivMesto

# Delovni Nalogi
from eda5.delovninalogi.forms import OpraviloCreateForm, OpraviloElementUpdateForm
from eda5.delovninalogi.models import Opravilo

# Moduli
from eda5.moduli.models import Zavihek

# Zaznamki
from eda5.zaznamki.forms import ZaznamekForm
from eda5.zaznamki.models import Zaznamek


class ZahtevekListView(ListView):
    model = Zahtevek
    template_name = "zahtevki/zahtevek/list/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ZahtevekListView, self).get_context_data(*args, **kwargs)

        # content
        context['zahtevki_vresevanju_list'] = self.model.objects.zahtevki_vresevanju()
        context['zahtevki_zakljuceni_list'] = self.model.objects.zahtevki_zakljuceni()

        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_LIST")
        context['modul_zavihek'] = modul_zavihek

        return context


# sem spremenil v TemplateView ker se avtomatsko doda tudi ArhivskoMesto (drugače je bil CreateView)
class ZahtevekCreateView(TemplateView):
    model = Zahtevek
    form_class = ZahtevekCreateForm
    template_name = "zahtevki/zahtevek/create.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ZahtevekCreateView, self).get_context_data(*args, **kwargs)

        context['zahtevek_form'] = ZahtevekCreateForm

        return context

    def post(self, request, *args, **kwargs):

        zahtevek_form = ZahtevekCreateForm(request.POST or None)

        if zahtevek_form.is_valid():

            oznaka = zahtevek_form.cleaned_data['oznaka']
            vrsta = zahtevek_form.cleaned_data['vrsta']
            naziv = zahtevek_form.cleaned_data['naziv']
            rok_izvedbe = zahtevek_form.cleaned_data['rok_izvedbe']
            narocilo = zahtevek_form.cleaned_data['narocilo']
            nosilec = zahtevek_form.cleaned_data['nosilec']

            Zahtevek.objects.create_zahtevek(
                oznaka=oznaka,
                vrsta=vrsta,
                naziv=naziv,
                rok_izvedbe=rok_izvedbe,
                narocilo=narocilo,
                nosilec=nosilec,
            )

            zahtevek = Zahtevek.objects.get(oznaka=oznaka)  # bolje bi bilo na ID ampak neznam
            # arhiv = Arhiv.objects.get(id=1)  # v končni fazi bo arhiv == objektu


            # ArhivMesto.objects.create_arhiv_mesto(
            #     arhiv=arhiv,
            #     zahtevek=zahtevek,
            #     oznaka=zahtevek.oznaka,
            #     naziv=zahtevek.naziv,
            # )
            
        return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk}))


class ZahtevekUpdateView(UpdateView):
    model = Zahtevek
    form_class = ZahtevekUpdateForm
    template_name = "zahtevki/zahtevek/update_zahtevek_main.html"


class ZahtevekUpdateSkodniView(UpdateView):
    model = ZahtevekSkodniDogodek
    form_class = ZahtevekSkodniDogodekUpdateForm
    template_name = "zahtevki/zahtevek/update_zahtevek_skodni.html"


class ZahtevekUpdateSestanekView(UpdateView):
    model = ZahtevekSestanek
    form_class = ZahtevekSestanekUpdateForm
    template_name = "zahtevki/zahtevek/update_zahtevek_sestanek.html"


class ZahtevekUpdateIzvedbaView(UpdateView):
    model = ZahtevekIzvedbaDela
    form_class = ZahtevekIzvedbaDelUpdateForm
    template_name = "zahtevki/zahtevek/update_zahtevek_izvedba.html"


# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# class ZahtevekUpdateDokumentFormView(UpdateView):
#     model = Zahtevek
#     form_class = ZahtevekUpdateDokumentForm
#     template_name = "zahtevki/zahtevek/update_dokument.html"


class ZahtevekDetailView(DetailView):
    model = Zahtevek
    template_name = "zahtevki/zahtevek/detail/base.html"



    def get_context_data(self, *args, **kwargs):
        context = super(ZahtevekDetailView, self).get_context_data(*args, **kwargs)

        # opravilo
        context['opravilo_form'] = OpraviloCreateForm
        context['opravilo_list'] = Opravilo.objects.filter(zahtevek=self.object.id)

        # zaznamek
        context['zaznamek_form'] = ZaznamekForm
        context['zaznamek_list'] = Zaznamek.objects.filter(zahtevek=self.object.id)

        # zahtevek - child
        context['zahtevek_create_form'] = ZahtevekIzbiraForm
        context['zahtevek_child_list'] = Zahtevek.objects.filter(zahtevek_parent=self.object.id)

        context['arhiviranje_form'] = ArhiviranjeZahtevekForm

        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):
        # opravilo_form = OpraviloCreateForm(request.POST or None)
        zaznamek_form = ZaznamekForm(request.POST or None)
        zahtevek_create_form = ZahtevekIzbiraForm(request.POST or None)
        arhiviranje_form = ArhiviranjeZahtevekForm(request.POST or None)

        zahtevek = Zahtevek.objects.get(id=self.get_object().id)

        opravilo_list = Opravilo.objects.filter(zahtevek=zahtevek)
        zaznamek_list = Zaznamek.objects.filter(zahtevek=zahtevek)
        zahtevek_child_list = Zahtevek.objects.filter(zahtevek_parent=zahtevek)

        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_DETAIL")

        # if opravilo_form.is_valid():
        #     oznaka = opravilo_form.cleaned_data['oznaka']
        #     naziv = opravilo_form.cleaned_data['naziv']
        #     rok_izvedbe = opravilo_form.cleaned_data['rok_izvedbe']
        #     narocilo = opravilo_form.cleaned_data['narocilo']
        #     nadzornik = opravilo_form.cleaned_data['nadzornik']
        #     # element = opravilo_form.cleaned_data['element']

        #     Opravilo.objects.create_opravilo(oznaka=oznaka,
        #                                      naziv=naziv,
        #                                      rok_izvedbe=rok_izvedbe,
        #                                      narocilo=narocilo,
        #                                      zahtevek=zahtevek,
        #                                      nadzornik=nadzornik
        #                                      # element=element,
        #                                      )

            # return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk}))

        if zaznamek_form.is_valid():
            tekst = zaznamek_form.cleaned_data['tekst']
            datum = zaznamek_form.cleaned_data['datum']
            ura = zaznamek_form.cleaned_data['ura']

            Zaznamek.objects.create_zaznamek(tekst=tekst,
                                             datum=datum,
                                             ura=ura,
                                             zahtevek=zahtevek,
                                             )

            return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk}))

        if zahtevek_create_form.is_valid():

            vrsta_zahtevka = zahtevek_create_form.cleaned_data['vrsta_zahtevka']

            if vrsta_zahtevka == '1':
                return HttpResponseRedirect(reverse('moduli:zahtevki:podzahtevek_create_sestanek', kwargs={'pk': zahtevek.pk}))
            if vrsta_zahtevka == '2':
                return HttpResponseRedirect(reverse('moduli:zahtevki:podzahtevek_create_izvedba_del', kwargs={'pk': zahtevek.pk}))

        # ARHIVIRANJE

        if arhiviranje_form.is_valid():

            dokument = arhiviranje_form.cleaned_data['dokument']
            arhiviral = arhiviranje_form.cleaned_data['arhiviral']
            elektronski = arhiviranje_form.cleaned_data['elektronski']
            fizicni = arhiviranje_form.cleaned_data['fizicni']
            lokacija_hrambe = ArhivMesto.objects.get(oznaka=zahtevek.oznaka)

            Arhiviranje.objects.create_arhiviranje(
                zahtevek=zahtevek,
                dokument=dokument,
                arhiviral=arhiviral,
                elektronski=elektronski,
                fizicni=fizicni,
                lokacija_hrambe=lokacija_hrambe,
            )

            return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk}))

        # IF NOT VALID
        return render(request, self.template_name, {
            'object': zahtevek,
            # 'opravilo_form': opravilo_form,
            'opravilo_list': opravilo_list,
            'zaznamek_form': zaznamek_form,
            'zaznamek_list': zaznamek_list,
            'zahtevek_create_form': zahtevek_create_form,
            'zahtevek_child_list': zahtevek_child_list,
            'arhiviranje_form': arhiviranje_form,
            'modul_zavihek': modul_zavihek,
            }
        )


class ZahtevekCreateIzbiraView(TemplateView):
    model = Zahtevek
    template_name = "zahtevki/zahtevek/create_izbira.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ZahtevekCreateIzbiraView, self).get_context_data(*args, **kwargs)

        # zahtevek
        context['zahtevek_izbira_form'] = ZahtevekIzbiraForm

        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        zahtevek_izbira_form = ZahtevekIzbiraForm(request.POST or None)

        if zahtevek_izbira_form.is_valid():

            vrsta_zahtevka = zahtevek_izbira_form.cleaned_data['vrsta_zahtevka']

            if vrsta_zahtevka == '1':
                return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_create_sestanek'))
            if vrsta_zahtevka == '2':
                return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_create_izvedba_del'))


class ZahtevekSestanekCreateView(TemplateView):
    template_name = "zahtevki/zahtevek/create_sestanek.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ZahtevekSestanekCreateView, self).get_context_data(*args, **kwargs)
        context['zahtevek_splosno_form'] = ZahtevekCreateForm
        context['zahtevek_sestanek_form'] = ZahtevekSestanekCreateForm

        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_SESTANEK_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *Args, **kwargs):

        zahtevek_splosno_form = ZahtevekCreateForm(request.POST or None)
        zahtevek_sestanek_form = ZahtevekSestanekCreateForm(request.POST or None)
        zahtevek_sestanek_update_form = ZahtevekSestanekUpdateForm(request.POST or None)
        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_SESTANEK_CREATE")

        # izdelamo objekt splosni zahtevek
        if zahtevek_splosno_form.is_valid():
            oznaka = zahtevek_splosno_form.cleaned_data['oznaka']
            naziv = zahtevek_splosno_form.cleaned_data['naziv']
            rok_izvedbe = zahtevek_splosno_form.cleaned_data['rok_izvedbe']
            narocilo = zahtevek_splosno_form.cleaned_data['narocilo']
            nosilec = zahtevek_splosno_form.cleaned_data['nosilec']

            zahtevek_splosno_data = Zahtevek.objects.create_zahtevek(
                oznaka=oznaka,
                vrsta=2,
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
                'zahtevek_sestanek_form': zahtevek_sestanek_form,
                'modul_zavihek': modul_zavihek,
                'zahtevek_sestanek_update_form': zahtevek_sestanek_update_form,
                }
            )

        # izdelamo objekt sestanek
        if zahtevek_sestanek_form.is_valid():

            sklicatelj = zahtevek_sestanek_form.cleaned_data['sklicatelj']
            datum = zahtevek_sestanek_form.cleaned_data['datum']

            zahtevek_sestanek_data = ZahtevekSestanek.objects.create_zahtevek_sestanek(
                zahtevek=zahtevek,
                sklicatelj=sklicatelj,
                datum=datum,
            )
            zahtevek_sestanek_object = ZahtevekSestanek.objects.get(id=zahtevek_sestanek_data.pk)

        else:
            return render(request, self.template_name, {
                'zahtevek_splosno_form': zahtevek_splosno_form,
                'zahtevek_sestanek_form': zahtevek_sestanek_form,
                'modul_zavihek': modul_zavihek,
                'zahtevek_sestanek_update_form': zahtevek_sestanek_update_form,
                }
            )

        # dodamo udeležence (many-to-many, ki se lahko doda samo po tem ko je objekt že izdelan : sestanek)
        if zahtevek_sestanek_update_form.is_valid():
            udelezenci = zahtevek_sestanek_update_form.cleaned_data['udelezenci']

            zahtevek_sestanek_object.udelezenci = udelezenci
            zahtevek_sestanek_object.save()

        else:
            return render(request, self.template_name, {
                'zahtevek_splosno_form': zahtevek_splosno_form,
                'zahtevek_sestanek_form': zahtevek_sestanek_form,
                'zahtevek_sestanek_update_form': zahtevek_sestanek_update_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk}))


class PodzahtevekSestanekCreateView(UpdateView):
    model = Zahtevek
    fields = ('id', )
    template_name = "zahtevki/zahtevek/create_sestanek.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PodzahtevekSestanekCreateView, self).get_context_data(*args, **kwargs)
        context['zahtevek_splosno_form'] = ZahtevekCreateForm
        context['zahtevek_sestanek_form'] = ZahtevekSestanekCreateForm

        modul_zavihek = Zavihek.objects.get(oznaka="PODZAHTEVEK_SESTANEK_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *Args, **kwargs):

        # object
        zahtevek_parent = Zahtevek.objects.get(id=self.get_object().id)

        zahtevek_splosno_form = ZahtevekCreateForm(request.POST or None)
        zahtevek_sestanek_form = ZahtevekSestanekCreateForm(request.POST or None)
        modul_zavihek = Zavihek.objects.get(oznaka="PODZAHTEVEK_SESTANEK_CREATE")

        if zahtevek_splosno_form.is_valid():
            oznaka = zahtevek_splosno_form.cleaned_data['oznaka']
            naziv = zahtevek_splosno_form.cleaned_data['naziv']
            rok_izvedbe = zahtevek_splosno_form.cleaned_data['rok_izvedbe']
            narocilo = zahtevek_splosno_form.cleaned_data['narocilo']
            nosilec = zahtevek_splosno_form.cleaned_data['nosilec']

            zahtevek_splosno_data = Zahtevek.objects.create_zahtevek(
                oznaka=oznaka,
                vrsta=2,
                naziv=naziv,
                rok_izvedbe=rok_izvedbe,
                narocilo=narocilo,
                nosilec=nosilec,
                status=3,
                zahtevek_parent=zahtevek_parent,
            )
            zahtevek = Zahtevek.objects.get(id=zahtevek_splosno_data.pk)

        else:
            return render(request, self.template_name, {
                'zahtevek_splosno_form': zahtevek_splosno_form,
                'zahtevek_sestanek_form': zahtevek_sestanek_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        if zahtevek_sestanek_form.is_valid():

            sklicatelj = zahtevek_sestanek_form.cleaned_data['sklicatelj']
            # udelezenci = zahtevek_sestanek_form.cleaned_data['udelezenci']
            datum = zahtevek_sestanek_form.cleaned_data['datum']

            ZahtevekSestanek.objects.create_zahtevek_sestanek(
                zahtevek=zahtevek,
                sklicatelj=sklicatelj,
                # udelezenci=udelezenci,
                datum=datum,
            )

        else:
            return render(request, self.template_name, {
                'zahtevek_splosno_form': zahtevek_splosno_form,
                'zahtevek_sestanek_form': zahtevek_sestanek_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk}))


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


class OpraviloCreateView(UpdateView):
    model = Zahtevek
    template_name = "delovninalogi/opravilo/create_from_zahtevek.html"
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):
        context = super(OpraviloCreateView, self).get_context_data(*args, **kwargs)

        # opravilo
        context['opravilo_create_form'] = OpraviloCreateForm
        context['opravilo_element_update_form'] = OpraviloElementUpdateForm

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="OPRAVILO_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        # object
        zahtevek = Zahtevek.objects.get(id=self.get_object().id)

        # forms
        opravilo_create_form = OpraviloCreateForm(request.POST or None)
        opravilo_element_update_form = OpraviloElementUpdateForm(request.POST or None)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="OPRAVILO_CREATE")

        # izdelamo opravilo (!!!elemente opravilu dodamo kasneje)
        if opravilo_create_form.is_valid():
            oznaka = opravilo_create_form.cleaned_data['oznaka']
            naziv = opravilo_create_form.cleaned_data['naziv']
            rok_izvedbe = opravilo_create_form.cleaned_data['rok_izvedbe']
            narocilo = opravilo_create_form.cleaned_data['narocilo']
            nadzornik = opravilo_create_form.cleaned_data['nadzornik']
            planirano_opravilo = opravilo_create_form.cleaned_data['planirano_opravilo']

            opravilo_data = Opravilo.objects.create_opravilo(
                oznaka=oznaka,
                naziv=naziv,
                rok_izvedbe=rok_izvedbe,
                narocilo=narocilo,
                zahtevek=zahtevek,
                nadzornik=nadzornik,
                planirano_opravilo=planirano_opravilo,
            )

            opravilo_object = Opravilo.objects.get(id=opravilo_data.pk)

        else:
            return render(request, self.template_name, {
                'opravilo_create_form': opravilo_create_form,
                'opravilo_element_update_form': opravilo_element_update_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        if opravilo_element_update_form.is_valid():
            element = opravilo_element_update_form.cleaned_data['element']

            opravilo_object.element = element
            opravilo_object.save()

        else:
            return render(request, self.template_name, {
                'opravilo_create_form': opravilo_create_form,
                'opravilo_element_update_form': opravilo_element_update_form,
                'modul_zavihek': modul_zavihek,
                }
            )

        return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk}))
