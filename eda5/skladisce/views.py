from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy

from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView

from .forms import \
    DobavaCreateForm, \
    DnevnikDobavaCreateForm, \
    SkladisceDnevnikFromDelovniNalogCreateForm, \
    SkladisceDnevnikUpdateForm

from .models import Dobava, Dnevnik


# Delovninalogi
from eda5.delovninalogi.models import DelovniNalog
from eda5.delovninalogi.mixins import MessagesActionMixin

# Moduli
from eda5.moduli.models import Zavihek

# Skladisce
from eda5.skladisce.models import Dnevnik




class SkladisceHomeView(TemplateView):
    template_name = "skladisce/home.html"


class DobavaListView(ListView):
    model = Dobava
    template_name = "skladisce/dobava/list/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DobavaListView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="DOBAVA_LIST")
        context['modul_zavihek'] = modul_zavihek

        return context


class DobavaCreateView(CreateView):
    model = Dobava
    template_name = "skladisce/dobava/create.html"
    form_class = DobavaCreateForm

    def get_context_data(self, *args, **kwargs):
        context = super(DobavaCreateView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="DOBAVA_CREATE")
        context['modul_zavihek'] = modul_zavihek

        return context


class DobavaDetailView(DetailView):
    model = Dobava
    template_name = "skladisce/dobava/detail/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DobavaDetailView, self).get_context_data(*args, **kwargs)
        context['dnevnik_dobava_form'] = DnevnikDobavaCreateForm

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="DOBAVA_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        dobava = Dobava.objects.get(id=self.get_object().id)

        dnevnik_dobava_form = DnevnikDobavaCreateForm(request.POST or None)

        if dnevnik_dobava_form.is_valid():

            artikel = dnevnik_dobava_form.cleaned_data['artikel']
            likvidiral = dnevnik_dobava_form.cleaned_data['likvidiral']
            kom = dnevnik_dobava_form.cleaned_data['kom']
            cena = dnevnik_dobava_form.cleaned_data['cena']
            stopnja_ddv = dnevnik_dobava_form.cleaned_data['stopnja_ddv']

            Dnevnik.objects.create_dnevnik(
                dobava=dobava,
                artikel=artikel,
                likvidiral=likvidiral,
                kom=kom,
                cena=cena,
                stopnja_ddv=stopnja_ddv,
            )

        return HttpResponseRedirect(reverse('moduli:skladisce:dobava_detail', kwargs={"pk": dobava.pk}))


class DnevnikListView(ListView):
    model = Dnevnik
    template_name = "skladisce/dnevnik/list/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DnevnikListView, self).get_context_data(*args, **kwargs)

        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="DNEVNIK_LIST")
        context['modul_zavihek'] = modul_zavihek

        return context


class SkladisceDnevnikCreateFromDelovniNalogView(MessagesActionMixin, UpdateView):
    model = DelovniNalog
    template_name = "skladisce/dnevnik/create_from_delovninalog.html"
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):
        context = super(SkladisceDnevnikCreateFromDelovniNalogView, self).get_context_data(*args, **kwargs)

        # opravilo
        context['skladisce_dnevnik_create_from_delovninalog_form'] = SkladisceDnevnikFromDelovniNalogCreateForm
        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="DN_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context


    def post(self, request, *args, **kwargs):

        # Delovni nalog s katerim imamo opravka (instanca)
        delovninalog = DelovniNalog.objects.get(id=self.get_object().id)

        # FORMS
        skladisce_dnevnik_create_from_delovninalog_form = SkladisceDnevnikFromDelovniNalogCreateForm(request.POST or None)


        # PODATKI IZ FORMS*********************************************
        if skladisce_dnevnik_create_from_delovninalog_form.is_valid():

            artikel = skladisce_dnevnik_create_from_delovninalog_form.cleaned_data['artikel']
            likvidiral = skladisce_dnevnik_create_from_delovninalog_form.cleaned_data['likvidiral']
            kom = skladisce_dnevnik_create_from_delovninalog_form.cleaned_data['kom']

            # VALIDACIJE **************************************************

            # VNOS V BAZO **************************************************
            # Izdelamo delo
            Dnevnik.objects.create_dnevnik(
                delovninalog=delovninalog,
                artikel=artikel,
                likvidiral=likvidiral,
                kom=kom,
            )

            # ob izdelavi dela sporočimo uporabniku
            messages.success(request, 'Material je bil uspešno dodan.')

            # ter izvedemo preusmeritev na obstoječi delovni nalog
            return HttpResponseRedirect(reverse('moduli:delovninalogi:dn_detail', kwargs={'pk': delovninalog.pk}))


class SkladisceDnevnikUpdateView(MessagesActionMixin, UpdateView):
    model = Dnevnik
    form_class = SkladisceDnevnikUpdateForm
    template_name = "delovninalogi/delo/update_from_delovninalog.html"
    success_msg = "Material je uspešno posodobljen."

    def get_context_data(self, *args, **kwargs):
        context = super(SkladisceDnevnikUpdateView, self).get_context_data(*args, **kwargs)

        # Zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="DN_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context

    def get_success_url(self, **kwargs): 
        return reverse('moduli:delovninalogi:dn_detail', kwargs={'pk': self.object.delovninalog.pk})
