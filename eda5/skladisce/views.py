from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from django.views.generic import TemplateView, ListView, CreateView, DetailView

from .forms import DobavaCreateForm, DnevnikDobavaCreateForm
from .models import Dobava, Dnevnik

from eda5.moduli.models import Zavihek


class SkladisceHomeView(TemplateView):
    template_name = "skladisce/home.html"


class DobavaListView(ListView):
    model = Dobava
    template_name = "skladisce/dobava/list.html"


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
    template_name = "skladisce/dnevnik/list.html"
