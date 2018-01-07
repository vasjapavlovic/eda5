from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import UpdateView



# Mixins
from braces.views import LoginRequiredMixin

# Models
from eda5.delovninalogi.models import Opravilo
from eda5.moduli.models import Zavihek

# Forms
from .forms import AktivnostCreateForm
from .forms import KontrolaSpecifikacijaFormSet



class KontrolniListSpecifikacijaCreateView(UpdateView):
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

        context = self.get_context_data()
        kontrolni_list_create_formset = context['kontrolni_list_create_formset']
        aktivnost_create_form = context['aktivnost_create_form']

        # aktivnost_create_form_is_valid = False
        # kontrolni_list_create_formset_is_valid = False
        #
        # aktivnost_create_form_is_valid = False



        if kontrolni_list_create_formset.is_valid():
            kontrola_specifikacija = kontrolni_list_create_formset['kontrola_specifikacija']

        with transaction.atomic():

            #form.instance.updated_by = self.request.user
            self.object = kontrolni_list_create_formset.save()

            if kontrola_specifikacija.is_valid():
                kontrola_specifikacija.instance = self.object
                kontrola_specifikacija.save()



        if kontrolni_list_create_formset.is_valid():
            return HttpResponseRedirect(reverse('moduli:zahtevki:zahtevek_detail', kwargs={'pk': zahtevek.pk}))

        # če zgornji formi niso ustrezno izpolnjeni

        else:
            return render(request, self.template_name, {
                'kontrolni_list_create_formset': kontrolni_list_create_formset,
                }
            )
