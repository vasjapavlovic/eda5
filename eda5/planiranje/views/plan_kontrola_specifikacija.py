
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


# Mixins
from braces.views import LoginRequiredMixin

# models
from ..models import PlanKontrolaSkupina, PlanKontrolaSpecifikacija

# forms
from ..forms import PlanKontrolaSpecifikacijaCreateForm



class PlanKontrolaSpecifikacijaCreateView(LoginRequiredMixin, UpdateView):
    model = PlanKontrolaSkupina
    template_name = 'planiranje/plan_kontrola_specifikacija/create.html'
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):
        context = super(PlanKontrolaSpecifikacijaCreateView, self).get_context_data(*args, **kwargs)

        plan_kontrola_skupina = PlanKontrolaSkupina.objects.get(id=self.get_object().pk)
        context['plan_kontrola_specifikacija_create_form'] = PlanKontrolaSpecifikacijaCreateForm()


        return context


    def post(self, request, *args, **kwargs):
        # tukaj napišem funkcijo za dodajanje kontrol skupin preko formseta
        plan_kontrola_skupina = PlanKontrolaSkupina.objects.get(pk=self.get_object().pk)

        plan_kontrola_specifikacija_create_form = PlanKontrolaSpecifikacijaCreateForm(self.request.POST or None)

        if plan_kontrola_specifikacija_create_form.is_valid():

            oznaka = plan_kontrola_specifikacija_create_form.cleaned_data['oznaka']
            naziv = plan_kontrola_specifikacija_create_form.cleaned_data['naziv']
            opis = plan_kontrola_specifikacija_create_form.cleaned_data['opis']
            vrednost_vrsta = plan_kontrola_specifikacija_create_form.cleaned_data['vrednost_vrsta']
            projektno_mesto = plan_kontrola_specifikacija_create_form.cleaned_data['projektno_mesto']
            zap_st = plan_kontrola_specifikacija_create_form.cleaned_data['zap_st']
            status = plan_kontrola_specifikacija_create_form.cleaned_data['status']


            plan_kontrola_specifikacija = PlanKontrolaSpecifikacija.objects.create(
                oznaka=oznaka,
                naziv=naziv,
                opis=opis,
                vrednost_vrsta=vrednost_vrsta,
                plan_kontrola_skupina=plan_kontrola_skupina,
                zap_st=zap_st,
                status=status,
            )

            plan_kontrola_specifikacija.projektno_mesto = projektno_mesto
            plan_kontrola_specifikacija.save()

            return HttpResponseRedirect(reverse('moduli:planiranje:plan_aktivnost_detail', kwargs={'pk': plan_kontrola_skupina.plan_aktivnost.pk}))


        else:
            return render(
                request,
                self.template_name,
                {
                'plan_kontrola_specifikacija_create_form': plan_kontrola_specifikacija_create_form,
                },
            )

class PlanKontrolaSpecifikacijaUpdateView(LoginRequiredMixin, UpdateView):
    model = PlanKontrolaSpecifikacija
    form_class = PlanKontrolaSpecifikacijaCreateForm
    template_name = 'planiranje/plan_kontrola_specifikacija/update.html'
