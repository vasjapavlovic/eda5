from django.views.generic import CreateView, DetailView, ListView, TemplateView, FormView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy

from .forms import AktivnostCreateForm, DokumentCreateForm
from .models import Aktivnost, Dokument

from eda5.arhiv.forms import ArhiviranjeCreateForm
from eda5.arhiv.models import Arhiviranje


class PostaHomeView(TemplateView):
    template_name = "posta/home.html"


class PostaArhiviranjeListView(ListView):
    model = Dokument
    template_name = "posta/dokument/list/extended.html"

    def get_queryset(self):
        # prikaži samo nearhivirano pošto
        queryset = self.model.objects.filter(arhiviranje=None)  # arhiviranje lahko uporabiš ker je
        return queryset                                         # OneToOne relacija


class PostaDokumentDetailView(DetailView):

    model = Dokument
    template_name = 'posta/dokument/detail/base.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostaDokumentDetailView, self).get_context_data(*args, **kwargs)
        # custom context here
        context['arhiviranje_form'] = ArhiviranjeCreateForm
        return context

    def post(self, request, *args, **kwargs):

        arhiviranje_form = ArhiviranjeCreateForm(request.POST or None)

        if arhiviranje_form.is_valid():

            dokument = Dokument.objects.get(id=self.get_object().id)
            arhiviral = arhiviranje_form.cleaned_data['arhiviral']
            lokacija_hrambe = arhiviranje_form.cleaned_data['lokacija_hrambe']
            elektronski = arhiviranje_form.cleaned_data['elektronski']
            fizicni = arhiviranje_form.cleaned_data['fizicni']

            Arhiviranje.objects.create_arhiviranje(
                dokument=dokument,
                arhiviral=arhiviral,
                lokacija_hrambe=lokacija_hrambe,
                elektronski=elektronski,
                fizicni=fizicni,
            )

        return HttpResponseRedirect(reverse('moduli:posta:dokument_arhiviranje_list'))




class DokumentCreateView(TemplateView):
    template_name = "posta/dokument/create.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DokumentCreateView, self).get_context_data(*args, **kwargs)
        context['aktivnost_form'] = AktivnostCreateForm
        context['dokument_form'] = DokumentCreateForm
        return context

    def post(self, request, *args, **kwargs):

        aktivnost_form = AktivnostCreateForm(request.POST or None)
        dokument_form = DokumentCreateForm(request.POST or None, request.FILES)

        if aktivnost_form.is_valid():

            id_1 = aktivnost_form.cleaned_data['id_1']
            izvajalec = aktivnost_form.cleaned_data['izvajalec']
            vrsta_aktivnosti = aktivnost_form.cleaned_data['vrsta_aktivnosti']
            datum = aktivnost_form.cleaned_data['datum']

            Aktivnost.objects.create_aktivnost(
                id_1=id_1,
                izvajalec=izvajalec,
                vrsta_aktivnosti=vrsta_aktivnosti,
                datum=datum,
            )

            aktivnost_id = request.POST.get('id_1', '')
            aktivnost = Aktivnost.objects.get(id_1=aktivnost_id)

        if dokument_form.is_valid():

            vrsta_dokumenta = dokument_form.cleaned_data['vrsta_dokumenta']
            avtor = dokument_form.cleaned_data['avtor']
            naslovnik = dokument_form.cleaned_data['naslovnik']
            oznaka = dokument_form.cleaned_data['oznaka']
            naziv = dokument_form.cleaned_data['naziv']
            datum = dokument_form.cleaned_data['datum']
            priponka = dokument_form.cleaned_data['priponka']

            Dokument.objects.create_dokument(
                vrsta_dokumenta=vrsta_dokumenta,
                avtor=avtor,
                naslovnik=naslovnik,
                oznaka=oznaka,
                naziv=naziv,
                datum=datum,
                priponka=priponka,
                aktivnost=aktivnost,
            )

        return HttpResponseRedirect(reverse('moduli:posta:dokument_arhiviranje_list'))
