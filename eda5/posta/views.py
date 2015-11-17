from django.views.generic import CreateView, DetailView, ListView, TemplateView, FormView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy

from .forms import AktivnostCreateForm, DokumentCreateForm
from .models import Aktivnost, Dokument
# from .forms import PrejetaPostaCreateForm


class PostaHomeView(TemplateView):
    template_name = "posta/home.html"


class PostaArhiviranjeListView(ListView):
    model = Aktivnost
    template_name = "posta/posta/list/extended.html"


    def get_context_data(self, *args, **kwargs):
        context = super(PostaArhiviranjeListView, self).get_context_data(*args, **kwargs)
        context['aktivnost_form'] = AktivnostCreateForm
        context['dokument_form'] = DokumentCreateForm
        return context

    def post(self, request, *args, **kwargs):

        aktivnost_form = AktivnostCreateForm(request.POST or None)
        dokument_form = DokumentCreateForm(request.POST or None, request.FILES)

        # 

        if aktivnost_form.is_valid():

            izvajalec = aktivnost_form.cleaned_data['izvajalec']
            vrsta_aktivnosti = aktivnost_form.cleaned_data['vrsta_aktivnosti']
            datum = aktivnost_form.cleaned_data['datum']

            Aktivnost.objects.create_aktivnost(
                izvajalec=izvajalec,
                vrsta_aktivnosti=vrsta_aktivnosti,
                datum=datum,
            )

            # aktivnost = request.POST.get('id', '')
            print('TEST-->', aktivnost)



        if dokument_form.is_valid():


            vrsta_dokumenta = dokument_form.cleaned_data['vrsta_dokumenta']
            avtor = dokument_form.cleaned_data['avtor']
            naslovnik = dokument_form.cleaned_data['naslovnik']
            oznaka = dokument_form.cleaned_data['oznaka']
            naziv = dokument_form.cleaned_data['naziv']
            datum = dokument_form.cleaned_data['datum']
            priponka = dokument_form.cleaned_data['priponka']
            aktivnost = Aktivnost.objects.get(id=18)
            # aktivnost = dokument_form.cleaned_data['aktivnost']

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

        return HttpResponseRedirect(reverse('moduli:posta:posta_arhiviranje_list'))


class AktivnostCreateView(CreateView):
    model = Dokument
    template_name = "posta/dokument/create.html"
