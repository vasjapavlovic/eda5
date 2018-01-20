

from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


# Mixins
from braces.views import LoginRequiredMixin

# models
from ..models import PlanAktivnost, PlanKontrolaSkupina, Plan, PlanKontrolaSpecifikacija

# form
from ..forms import PlanAktivnostCreateForm



class PlanAktivnostCreateView(LoginRequiredMixin, UpdateView):
    model = Plan
    template_name = 'planiranje/plan_aktivnost/create.html'
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):
        context = super(PlanAktivnostCreateView, self).get_context_data(*args, **kwargs)
        # tukaj prikažem formset za vnos

        plan = Plan.objects.get(id=self.get_object().pk)
        context['plan_aktivnost_create_form'] = PlanAktivnostCreateForm()

        return context


    def post(self, request, *args, **kwargs):
        # tukaj napišem funkcijo za dodajanje kontrol skupin preko formseta
        plan = Plan.objects.get(pk=self.get_object().pk)

        plan_aktivnost_create_form = PlanAktivnostCreateForm(self.request.POST or None)

        if plan_aktivnost_create_form.is_valid():


            oznaka = plan_aktivnost_create_form.cleaned_data['oznaka']
            naziv = plan_aktivnost_create_form.cleaned_data['naziv']
            opis = plan_aktivnost_create_form.cleaned_data['opis']
            perioda_enota = plan_aktivnost_create_form.cleaned_data['perioda_enota']
            perioda_enota_kolicina = plan_aktivnost_create_form.cleaned_data['perioda_enota_kolicina']
            perioda_kolicina_na_enoto = plan_aktivnost_create_form.cleaned_data['perioda_kolicina_na_enoto']

            plan_aktivnost = PlanAktivnost.objects.create(
                oznaka=oznaka,
                naziv=naziv,
                opis=opis,
                perioda_enota=perioda_enota,
                perioda_enota_kolicina=perioda_enota_kolicina,
                perioda_kolicina_na_enoto=perioda_kolicina_na_enoto,
                plan=plan,
            )

            plan_aktivnost.save()

            return HttpResponseRedirect(reverse('moduli:planiranje:plan_update', kwargs={'pk': plan.pk}))


        else:
            return render(
                request,
                self.template_name,
                {
                'plan_aktivnost_create_form': plan_aktivnost_create_form,
                },
            )


class PlanAktivnostDetailView(LoginRequiredMixin, DetailView):
    model = PlanAktivnost
    template_name = 'planiranje/plan_aktivnost/detail.html'
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):
        context = super(PlanAktivnostDetailView, self).get_context_data(*args, **kwargs)
        # tukaj prikažem formset za vnos

        plan_aktivnost = PlanAktivnost.objects.get(id=self.get_object().pk)

        plan_kontrola_skupina = PlanKontrolaSkupina.objects.filter(plan_aktivnost=plan_aktivnost)

        plan_kontrola_skupina = plan_kontrola_skupina.order_by(
            'zap_st',
            'oznaka',  # če so zaporedne številke enake razporedi še po oznaki
            'plankontrolaspecifikacija__zap_st',
            'plankontrolaspecifikacija__oznaka',  # če so zaporedne številke enake razporedi še po oznaki
        )
        plan_kontrola_skupina = plan_kontrola_skupina.values(
            'id',
            'plankontrolaspecifikacija',
        )


        plan_kontrola_skupina_list = []
        for pksk in plan_kontrola_skupina:
            try:
                plan_kontrola_skupina = PlanKontrolaSkupina.objects.get(id=pksk['id'])
            except:
                plan_kontrola_skupina = None

            try:
                plan_kontrola_specifikacija = PlanKontrolaSpecifikacija.objects.get(id=pksk['plankontrolaspecifikacija'])
            except:
                plan_kontrola_specifikacija = None


            plan_kontrola_skupina_list.append(
                {
                    'plan_kontrola_skupina': plan_kontrola_skupina,
                    'plan_kontrola_specifikacija': plan_kontrola_specifikacija,
                }
            )


        context['plan_kontrola_skupina_list'] = plan_kontrola_skupina_list

        return context


class PlanAktivnostUpdateView(LoginRequiredMixin, UpdateView):
    model = PlanAktivnost
    form_class = PlanAktivnostCreateForm
    template_name = 'planiranje/plan_aktivnost/update.html'
