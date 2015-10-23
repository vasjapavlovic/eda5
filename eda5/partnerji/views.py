from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView

from .forms import PartnerCreateForm, PartnerUpdateForm
from .forms import OsebaCreateForm, OsebaUpdateForm, OsebaCreateWidget

from .models import Partner, Oseba

# mixins
from .viewmixins import PartnerSearchMixin


class PartnerHomeView(TemplateView):
    template_name="partnerji/home.html"


class PartnerListView(PartnerSearchMixin, ListView):
    model = Partner

    # order_by
    def get_queryset(self):
        queryset = super(PartnerListView, self).get_queryset()
        queryset = queryset.order_by('kratko_ime')
        return queryset


class PartnerDetailView(DetailView):
    model = Partner

    # subform "Dodaj Osebo"
    form_class = OsebaCreateWidget

    def get_context_data(self, *args, **kwargs):
        context = super(PartnerDetailView, self).get_context_data(*args, **kwargs)
        context['oseba_form'] = self.form_class
        return context


    def post(self, request, *args, **kwargs):
        oseba_form = OsebaCreateWidget(request.POST or None)
        trr_form = TrrCreateWidget(request.POST or None)

        podjetje = Partner.objects.get(id=self.get_object().id)

        if oseba_form.is_valid():
            ime = oseba_form.cleaned_data['ime']
            priimek = oseba_form.cleaned_data['priimek']
            status = oseba_form.cleaned_data['status']
            kvalifikacije = oseba_form.cleaned_data['kvalifikacije']

            Oseba.objects.create_oseba(
                priimek=priimek,
                ime=ime,
                status=status,
                kvalifikacije=kvalifikacije,
                podjetje=podjetje,
                )

            # obj_instance = oseba_form.save(commit=False)
            # obj_instance.priimek = oseba_form.cleaned_data['priimek']
            # obj_instance.ime = oseba_form.cleaned_data['ime']
            # obj_instance.status = oseba_form.cleaned_data['status']
            # obj_instance.podjetje = instance_partner
            # obj_instance.save()

            # object_instance.priimek = 
            #print(form.cleaned_data['priimek'])
            # form.cleaned_data['priimek']
            # <process form cleaned data>
        return HttpResponseRedirect('/moduli/partnerji/seznam/')

class PartnerCreateView(CreateView):
    model = Partner
    form_class = PartnerCreateForm


class PartnerUpdateView(UpdateView):
    model = Partner
    form_class = PartnerUpdateForm


class OsebaCreateView(CreateView):
    model = Oseba
    form_class = OsebaCreateForm


class OsebaUpdateView(CreateView):
    model = Oseba
    form_class = OsebaUpdateForm