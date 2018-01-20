
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


# Mixins
from braces.views import LoginRequiredMixin

# models
from ..models import PlanKontrolaSpecifikacija, PlanKontrolaSpecifikacijaOpcijaSelect

# forms
from ..forms import PlanKontrolaSpecifikacijaOpcijaSelectCreateForm



class PlanKontrolaSpecifikacijaOpcijaSelectCreateView(LoginRequiredMixin, UpdateView):
    model = PlanKontrolaSpecifikacija
    template_name = 'planiranje/plan_kontrola_specifikacija_opcija_select/create.html'
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):
        context = super(PlanKontrolaSpecifikacijaOpcijaSelectCreateView, self).get_context_data(*args, **kwargs)

        plan_kontrola_specifikacija = PlanKontrolaSpecifikacija.objects.get(id=self.get_object().pk)
        context['plan_kontrola_specifikacija_opcija_select_create_form'] = PlanKontrolaSpecifikacijaOpcijaSelectCreateForm()


        return context


    def post(self, request, *args, **kwargs):
        # tukaj napišem funkcijo za dodajanje kontrol skupin preko formseta
        plan_kontrola_specifikacija = PlanKontrolaSpecifikacija.objects.get(pk=self.get_object().pk)

        plan_kontrola_specifikacija_opcija_select_create_form = PlanKontrolaSpecifikacijaOpcijaSelectCreateForm(self.request.POST or None)

        if plan_kontrola_specifikacija_opcija_select_create_form.is_valid():

            naziv = plan_kontrola_specifikacija_opcija_select_create_form.cleaned_data['naziv']
            zap_st = plan_kontrola_specifikacija_opcija_select_create_form.cleaned_data['zap_st']
            status = plan_kontrola_specifikacija_opcija_select_create_form.cleaned_data['status']

            plan_kontrola_specifikacija_opcija_select = PlanKontrolaSpecifikacijaOpcijaSelect.objects.create(
                naziv=naziv,
                plan_kontrola_specifikacija=plan_kontrola_specifikacija,
                zap_st=zap_st,
                status=status,
            )

            plan_kontrola_specifikacija_opcija_select.save()

            return HttpResponseRedirect(reverse('moduli:planiranje:plan_aktivnost_detail', kwargs={'pk': plan_kontrola_specifikacija.plan_kontrola_skupina.plan_aktivnost.pk}))


        else:
            return render(
                request,
                self.template_name,
                {
                'plan_kontrola_specifikacija_opcija_select_create_form': plan_kontrola_specifikacija_opcija_select_create_form,
                },
            )

class PlanKontrolaSpecifikacijaOpcijaSelectUpdateView(LoginRequiredMixin, UpdateView):
    model = PlanKontrolaSpecifikacijaOpcijaSelect
    form_class = PlanKontrolaSpecifikacijaOpcijaSelectCreateForm
    template_name = 'planiranje/plan_kontrola_specifikacija_opcija_select/update.html'
