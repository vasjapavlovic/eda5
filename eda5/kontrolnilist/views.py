from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import UpdateView
from django.db import transaction
from django.core.urlresolvers import reverse




# Mixins
from braces.views import LoginRequiredMixin

# Models
from .models import Aktivnost
from .models import KontrolaSpecifikacija
from .models import KontrolaVrednost
from eda5.delovninalogi.models import DelovniNalog
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

class KontrolniListAktivnostUpdateView(LoginRequiredMixin, UpdateView):
    '''
    View za update aktivnosti
    '''

    model = Aktivnost
    template_name = "kontrolnilist/create.html"
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):
        context = super(KontrolniListAktivnostUpdateView, self).get_context_data(*args, **kwargs)

        aktivnost = Aktivnost.objects.get(id=self.object.id)
        context['aktivnost'] = aktivnost

        if self.request.POST:
            context['aktivnost_create_form'] = AktivnostCreateForm(self.request.POST, instance=aktivnost)
            context['kontrolni_list_create_formset'] = KontrolaSpecifikacijaFormSet(self.request.POST, instance=aktivnost)
        else:
            context['aktivnost_create_form'] = AktivnostCreateForm(instance=aktivnost)
            context['kontrolni_list_create_formset'] = KontrolaSpecifikacijaFormSet(instance=aktivnost)


        # # Zavihek
        # modul_zavihek = Zavihek.objects.get(oznaka="DN_DETAIL")
        # context['modul_zavihek'] = modul_zavihek

        return context


    def post(self, request, *args, **kwargs):

        aktivnost = Aktivnost.objects.get(pk=self.get_object().pk)

        aktivnost_create_form = AktivnostCreateForm(self.request.POST, instance=aktivnost)
        kontrolni_list_create_formset = KontrolaSpecifikacijaFormSet(self.request.POST, instance=aktivnost)


        if aktivnost_create_form.is_valid():
            # transaction.atomic() --> če je karkoli narobe se stanje v bazi povrne v prvotno stanje
            with transaction.atomic():
                aktivnost_create_form.instance = aktivnost
                aktivnost_create_form_saved = aktivnost_create_form.save()

                if kontrolni_list_create_formset.is_valid():
                    kontrolni_list_create_formset.instance = aktivnost_create_form_saved
                    kontrolni_list_create_formset.save()

            return HttpResponseRedirect(reverse('moduli:delovninalogi:opravilo_detail', kwargs={'pk': aktivnost.opravilo.pk}))


        else:
            return render(
                request,
                self.template_name,
                {
                'aktivnost_create_form': aktivnost_create_form,
                'kontrolni_list_create_formset': kontrolni_list_create_formset,
                },
            )


class KontrolaVrednostCreateView(LoginRequiredMixin, UpdateView):
    model = DelovniNalog
    template_name = 'kontrolnilist/kontrola_vrednost_create.html'
    fields = ('id', )


    def post(self, request, *args, **kwawrgs):

        dn = DelovniNalog.objects.get(id=self.get_object().id)


        # logika za izdelavo vrednosti specificiranih kontrol
        # pridobimo kontrole, ki so izdelane v dn.opravilo
        kontrola_list = KontrolaSpecifikacija.objects.filter(aktivnost__opravilo=dn.opravilo)

        for kontrola in kontrola_list:
            kontrola_vrednost_vnos = KontrolaVrednost.objects.create(
                delovni_nalog=dn,
                kontrola_specifikacija=kontrola,
                # projektno_mesto se doda naknadno
            )
            kontrola_vrednost_vnos.save()


            projektno_mesto_list = kontrola.aktivnost.projektno_mesto.all()
            kontrola_vrednost_vnos.projektno_mesto = projektno_mesto_list
            kontrola_vrednost_vnos.save()



        return HttpResponseRedirect(reverse('moduli:delovninalogi:dn_detail', kwargs={'pk': dn.pk}))



    def get_context_data(self, *args, **kwargs):
        context = super(KontrolaVrednostCreateView, self).get_context_data(*args, **kwargs)
        # new context data go here

        modul_zavihek = Zavihek.objects.get(oznaka="DN_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context
