# from django.shortcuts import render
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

from .forms import ZahtevekCreateForm, PodzahtevekCreateForm,\
                   ZahtevekUpdateForm, ZahtevekSkodniDogodekUpdateForm, ZahtevekSestanekUpdateForm,\
                   ZahtevekIzvedbaDelUpdateForm, ZahtevekIzvedbaDelaCreateForm, PodzahtevekForm

from .forms import ZahtevekSestanekCreateForm


from .models import Zahtevek, ZahtevekSkodniDogodek, ZahtevekSestanek, ZahtevekIzvedbaDela

from eda5.delovninalogi.forms import OpraviloCreateForm
from eda5.delovninalogi.models import Opravilo

from eda5.zaznamki.forms import ZaznamekForm
from eda5.zaznamki.models import Zaznamek

from eda5.arhiv.forms import ArhiviranjeZahtevekForm
from eda5.arhiv.models import Arhiv, ArhivMesto, Arhiviranje

from eda5.moduli.models import Zavihek


class ZahtevekHomeView(TemplateView):
    template_name = "zahtevki/home.html"


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
        context['zahtevek_create_form'] = PodzahtevekForm
        context['zahtevek_child_list'] = Zahtevek.objects.filter(zahtevek_parent=self.object.id)

        context['arhiviranje_form'] = ArhiviranjeZahtevekForm

        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):
        opravilo_form = OpraviloCreateForm(request.POST or None)
        zaznamek_form = ZaznamekForm(request.POST or None)
        zahtevek_create_form = PodzahtevekForm(request.POST or None)
        arhiviranje_form = ArhiviranjeZahtevekForm(request.POST or None)

        zahtevek = Zahtevek.objects.get(id=self.get_object().id)

        opravilo_list = Opravilo.objects.filter(zahtevek=zahtevek)
        zaznamek_list = Zaznamek.objects.filter(zahtevek=zahtevek)
        zahtevek_child_list = Zahtevek.objects.filter(zahtevek_parent=zahtevek)

        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_DETAIL")

        if opravilo_form.is_valid():
            oznaka = opravilo_form.cleaned_data['oznaka']
            naziv = opravilo_form.cleaned_data['naziv']
            rok_izvedbe = opravilo_form.cleaned_data['rok_izvedbe']
            narocilo = opravilo_form.cleaned_data['narocilo']
            nadzornik = opravilo_form.cleaned_data['nadzornik']
            # element = opravilo_form.cleaned_data['element']

            Opravilo.objects.create_opravilo(oznaka=oznaka,
                                             naziv=naziv,
                                             rok_izvedbe=rok_izvedbe,
                                             narocilo=narocilo,
                                             zahtevek=zahtevek,
                                             nadzornik=nadzornik
                                             # element=element,
                                             )

            return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk}))

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
                return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_create_sestanek'))
            if vrsta_zahtevka == '2':
                return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_create_izvedba_del'))

        # ARHIVIRANJE

        if arhiviranje_form.is_valid():

            dokument = arhiviranje_form.cleaned_data['dokument']
            arhiviral = arhiviranje_form.cleaned_data['arhiviral']
            elektronski = arhiviranje_form.cleaned_data['elektronski']
            fizicni = arhiviranje_form.cleaned_data['fizicni']
            lokacija_hrambe = arhiviranje_form.cleaned_data['lokacija_hrambe']

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
            'opravilo_form': opravilo_form,
            'opravilo_list': opravilo_list,
            'zaznamek_form': zaznamek_form,
            'zaznamek_list': zaznamek_list,
            'zahtevek_create_form': zahtevek_create_form,
            'zahtevek_child_list': zahtevek_child_list,
            'arhiviranje_form': arhiviranje_form,
            'modul_zavihek': modul_zavihek,
            }
        )

            # DATOTEKO PRENESEMO V ARHIVSKO MESTO!
            # '''Za račune poskrbimo varnostno kopijo pod Dokumenti/Računovodstvo'''

            # old_path = str(dokument.priponka)
            # filename = old_path.split('/')[2]

            # new_path = ('Dokumentacija/Arhivirano', lokacija_hrambe.oznaka, filename)

            # new_path = '/'.join(new_path)
            # dokument.priponka = new_path
            # dokument.save()

            # # izdelamo direktorjih arhivskega mesta
            # mapa = os.path.dirname(settings.MEDIA_ROOT + "/" + new_path)
            # if not os.path.exists(mapa):
            #     os.makedirs(mapa)

            # # prenos datoteke v arhivsko mesto
            # os.rename(settings.MEDIA_ROOT + "/" + old_path, settings.MEDIA_ROOT + "/" + new_path)


class ZahtevekCreateIzbira():
    pass


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
        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_SESTANEK_CREATE")

        if zahtevek_splosno_form.is_valid():
            oznaka = zahtevek_splosno_form.cleaned_data['oznaka']
            naziv = zahtevek_splosno_form.cleaned_data['naziv']
            vrsta = zahtevek_splosno_form.cleaned_data['vrsta']
            rok_izvedbe = zahtevek_splosno_form.cleaned_data['rok_izvedbe']
            narocilo = zahtevek_splosno_form.cleaned_data['narocilo']
            nosilec = zahtevek_splosno_form.cleaned_data['nosilec']

            zahtevek_splosno_data = Zahtevek.objects.create_zahtevek(
                oznaka=oznaka,
                vrsta=vrsta,
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

        return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_list'))


class ZahtevekIzvedbaDelCreateView(TemplateView):
    template_name = "zahtevki/zahtevek/create_izvedba_del.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ZahtevekIzvedbaDelCreateView, self).get_context_data(*args, **kwargs)
        context['zahtevek_splosno_form'] = ZahtevekCreateForm
        context['zahtevek_izvedba_del_form'] = ZahtevekIzvedbaDelaCreateForm

        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_IZVEDBA_DEL_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *Args, **kwargs):

        zahtevek_splosno_form = ZahtevekCreateForm(request.POST or None)
        zahtevek_izvedba_del_form = ZahtevekIzvedbaDelaCreateForm(request.POST or None)
        modul_zavihek = Zavihek.objects.get(oznaka="ZAHTEVEK_IZVEDBA_DEL_CREATE")

        if zahtevek_splosno_form.is_valid():
            oznaka = zahtevek_splosno_form.cleaned_data['oznaka']
            naziv = zahtevek_splosno_form.cleaned_data['naziv']
            vrsta = zahtevek_splosno_form.cleaned_data['vrsta']
            rok_izvedbe = zahtevek_splosno_form.cleaned_data['rok_izvedbe']
            narocilo = zahtevek_splosno_form.cleaned_data['narocilo']
            nosilec = zahtevek_splosno_form.cleaned_data['nosilec']

            zahtevek_splosno_data = Zahtevek.objects.create_zahtevek(
                oznaka=oznaka,
                vrsta=vrsta,
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

        return HttpResponseRedirect(reverse('moduli:home'))
