# Splošno Django
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView

# mixins
from braces.views import LoginRequiredMixin

# Moduli
from eda5.moduli.models import Zavihek

# Pomanjkljivosti
from .forms import \
    PomanjkljivostCreateForm, \
    PomanjkljivostCreateFromZahtevekForm
    

from .forms import Pomanjkljivost

# Zahtevki
from eda5.zahtevki.models import Zahtevek


class PomanjkljivostiHomeView(TemplateView):
    template_name = "pomanjkljivosti/home.html"


''' Izdelava pomanjkljivosti preko vmesnika'''
class PomanjkljivostCreateView(LoginRequiredMixin, CreateView):
    model = Pomanjkljivost
    template_name = "pomanjkljivosti/pomanjkljivost/create/create.html"
    form_class = PomanjkljivostCreateForm

    def get_context_data(self, *args, **kwargs):
        context = super(PomanjkljivostCreateView, self).get_context_data(*args, **kwargs)
        # pridobimo instanco izbranega zavihka
        modul_zavihek = Zavihek.objects.get(oznaka="pomanjkljivost_create")
        context['modul_zavihek'] = modul_zavihek
        # vrnemo context
        return context


class PomanjkljivostListView(LoginRequiredMixin, ListView):

    model = Pomanjkljivost
    template_name = "pomanjkljivosti/pomanjkljivost/list/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PomanjkljivostListView, self).get_context_data(*args, **kwargs)

        # pridobimo instanco izbranega zavihka
        modul_zavihek = Zavihek.objects.get(oznaka="pomanjkljivost_list")
        context['modul_zavihek'] = modul_zavihek

        # seznam pomanjkljivosti, ki se že rešujejo
        pomanjkljivosti_vresevanju = Pomanjkljivost.objects.filter(zahtevek__isnull=False)
        context['pomanjkljivosti_vresevanju'] = pomanjkljivosti_vresevanju

        # vrnemo context
        return context

    def get_queryset(self):
        queryset = super(PomanjkljivostListView, self).get_queryset()
        # prikažemo samo ne-rešene pomanjkljivosti
        queryset = self.model.objects.filter(zahtevek__isnull=True)
        # vrnemo spremenjene podatke
        return queryset


class PomanjkljivostDetailView(LoginRequiredMixin, DetailView):
    model = Pomanjkljivost
    template_name = "pomanjkljivosti/pomanjkljivost/detail/base.html"


''' Izdelava pomanjkljivosti preko zahtevka'''
class PomanjkljivostCreateFromZahtevekView(LoginRequiredMixin, UpdateView):

    model = Zahtevek
    template_name = 'pomanjkljivosti/pomanjkljivost/create/create_from_zahtevek.html'
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):
        context = super(PomanjkljivostCreateFromZahtevekView, self).get_context_data(*args, **kwargs)
        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="pomanjkljivost_detail")
        context['modul_zavihek'] = modul_zavihek
        # pomanjkljivost
        context['pomanjkljivost_create_from_zahtevek_form'] = PomanjkljivostCreateFromZahtevekForm
        # vrnemo narejene podatke
        return context


    def post(self, request, *args, **kwargs):

        ''' Pridobimo instanco zahtevka kjer se pomanjkljivost dodaja '''
        zahtevek = Zahtevek.objects.get(id=self.get_object().id)

        ''' Pridobimo instanco Zavihka '''
        modul_zavihek = Zavihek.objects.get(oznaka="pomanjkljivost_detail")

        #FORMS
        pomanjkljivost_create_from_zahtevek_form = PomanjkljivostCreateFromZahtevekForm(request.POST or None)


        ''' Izdelamo pomanjkljivost iz zahtevka '''

        if pomanjkljivost_create_from_zahtevek_form.is_valid():
            oznaka = pomanjkljivost_create_from_zahtevek_form.cleaned_data['oznaka']
            naziv = pomanjkljivost_create_from_zahtevek_form.cleaned_data['naziv']
            prijavil_text = pomanjkljivost_create_from_zahtevek_form.cleaned_data['prijavil_text']
            prijava_dne = pomanjkljivost_create_from_zahtevek_form.cleaned_data['prijava_dne']
            element_text = pomanjkljivost_create_from_zahtevek_form.cleaned_data['element_text']
            etaza_text = pomanjkljivost_create_from_zahtevek_form.cleaned_data['etaza_text']
            lokacija_text = pomanjkljivost_create_from_zahtevek_form.cleaned_data['lokacija_text']
            element = pomanjkljivost_create_from_zahtevek_form.cleaned_data['element']
            prioriteta = pomanjkljivost_create_from_zahtevek_form.cleaned_data['prioriteta']

            Pomanjkljivost.objects.create_pomanjkljivost(
                oznaka=oznaka,
                naziv=naziv,
                prijavil_text=prijavil_text,
                prijava_dne=prijava_dne,
                prioriteta=prioriteta,
                element_text=element_text,
                etaza_text=etaza_text,
                lokacija_text=lokacija_text,
                element=element,
                zahtevek=zahtevek,
            )


        else:
            return render(request, self.template_name, {
                'pomanjkljivost_create_from_zahtevek_form': pomanjkljivost_create_from_zahtevek_form,
                'modul_zavihek': modul_zavihek,
                }
            )


        ''' po končanem vnosu se izvede preusmeritev '''

        return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk}))




