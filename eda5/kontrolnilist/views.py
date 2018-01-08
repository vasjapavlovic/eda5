from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import UpdateView
from django.db import transaction
from django.core.urlresolvers import reverse




# Mixins
from braces.views import LoginRequiredMixin

# Models
from eda5.delovninalogi.models import Opravilo
from eda5.moduli.models import Zavihek

# Forms
from .forms import AktivnostCreateForm
from .forms import KontrolaSpecifikacijaFormSet



class KontrolniListSpecifikacijaCreateView(LoginRequiredMixin, UpdateView):
    '''
    View za izdelavo specifikacije kontrolnega lista iz OPRAVILA
    '''

    model = Opravilo
    template_name = "kontrolnilist/create.html"
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):
        context = super(KontrolniListSpecifikacijaCreateView, self).get_context_data(*args, **kwargs)

        opravilo = Opravilo.objects.get(id=self.object.id)
        context['opravilo'] = opravilo

        if self.request.POST:
            context['aktivnost_create_form'] = AktivnostCreateForm(self.request.POST)
            context['kontrolni_list_create_formset'] = KontrolaSpecifikacijaFormSet(self.request.POST)
        else:
            context['aktivnost_create_form'] = AktivnostCreateForm()
            context['kontrolni_list_create_formset'] = KontrolaSpecifikacijaFormSet()


        # # Zavihek
        # modul_zavihek = Zavihek.objects.get(oznaka="DN_DETAIL")
        # context['modul_zavihek'] = modul_zavihek

        return context


    def post(self, request, *args, **kwargs):

        opravilo = Opravilo.objects.get(pk=self.get_object().pk)

        aktivnost_create_form = AktivnostCreateForm(self.request.POST)
        kontrolni_list_create_formset = KontrolaSpecifikacijaFormSet(self.request.POST)


        if aktivnost_create_form.is_valid():
            # transaction.atomic() --> če je karkoli narobe se stanje v bazi povrne v prvotno stanje
            with transaction.atomic():
                aktivnost_create_form.instance.opravilo = opravilo
                aktivnost_create_form_saved = aktivnost_create_form.save()

                if kontrolni_list_create_formset.is_valid():
                    kontrolni_list_create_formset.instance = aktivnost_create_form_saved
                    kontrolni_list_create_formset.save()

            return HttpResponseRedirect(reverse('moduli:delovninalogi:opravilo_detail', kwargs={'pk': opravilo.pk}))


        else:
            return render(
                request,
                self.template_name,
                {
                'aktivnost_create_form': aktivnost_create_form,
                'kontrolni_list_create_formset': kontrolni_list_create_formset,
                },
            )
