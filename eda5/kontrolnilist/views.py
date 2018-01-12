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
from eda5.deli.models import ProjektnoMesto
from eda5.delovninalogi.models import DelovniNalog
from eda5.delovninalogi.models import Opravilo
from eda5.moduli.models import Zavihek


# Forms
from .forms import AktivnostCreateForm
from .forms import KontrolaSpecifikacijaFormSet
from .forms import KontrolaVrednostUpdateFormSetOblika01
from .forms import KontrolaVrednostUpdateFormSetOblika02




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

        aktivnost_list = dn.opravilo.aktivnost_set.all()
        for aktivnost in aktivnost_list:
            ks_list = aktivnost.kontrolaspecifikacija_set.all()

            for ks in ks_list:
                 projektna_mesta_specifikacije = ks.aktivnost.projektno_mesto.all()
                 for pm in projektna_mesta_specifikacije:
                    vrednost = KontrolaVrednost.objects.create(
                            delovni_nalog=dn,
                            kontrola_specifikacija=ks,
                            projektno_mesto=pm,
                        )

        return HttpResponseRedirect(reverse('moduli:delovninalogi:dn_detail', kwargs={'pk': dn.pk}))



    def get_context_data(self, *args, **kwargs):
        context = super(KontrolaVrednostCreateView, self).get_context_data(*args, **kwargs)
        # new context data go here

        modul_zavihek = Zavihek.objects.get(oznaka="DN_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context


class KontrolniListUpdateOblika01View(LoginRequiredMixin, UpdateView):

    model = DelovniNalog
    template_name = 'kontrolnilist/update_oblika01.html'
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):
        context = super(KontrolniListUpdateOblika01View, self).get_context_data(*args, **kwargs)


        dn = DelovniNalog.objects.get(id=self.object.id)

        # Kontrolni List
        kontrola_vrednost_update_formset = KontrolaVrednostUpdateFormSetOblika01(delovninalog=dn)
        context['kontrola_vrednost_update_oblika01_formset'] = kontrola_vrednost_update_formset



        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="DN_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context


    def post(self, request, *args, **kwargs):

        dn = DelovniNalog.objects.get(id=self.get_object().id)
        formset = KontrolaVrednostUpdateFormSetOblika01(request.POST or None, delovninalog=dn)

        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect(reverse('moduli:delovninalogi:dn_detail', kwargs={'pk': dn.pk}))
        else:
            return render(
                request,
                self.template_name,
                {
                    'kontrola_vrednost_update_formset': kontrola_vrednost_update_formset,
                },
            )

class KontrolniListUpdateOblika02View(LoginRequiredMixin, UpdateView):

    model = DelovniNalog
    template_name = 'kontrolnilist/update_oblika02.html'
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):
        context = super(KontrolniListUpdateOblika02View, self).get_context_data(*args, **kwargs)


        dn = DelovniNalog.objects.get(id=self.object.id)

        # Kontrolni List
        kontrola_vrednost_update_formset = KontrolaVrednostUpdateFormSetOblika02(delovninalog=dn)
        context['kontrola_vrednost_update_oblika02_formset'] = kontrola_vrednost_update_formset



        # zavihek
        modul_zavihek = Zavihek.objects.get(oznaka="DN_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        return context

    def post(self, request, *args, **kwargs):

        dn = DelovniNalog.objects.get(id=self.get_object().id)

        formset = KontrolaVrednostUpdateFormSetOblika02(request.POST or None, delovninalog=dn)

        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect(reverse('moduli:delovninalogi:dn_detail', kwargs={'pk': dn.pk}))
        else:
            return render(
                request,
                self.template_name,
                {
                    'kontrola_vrednost_update_formset': kontrola_vrednost_update_formset,
                },
            )
