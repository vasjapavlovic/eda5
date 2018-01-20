
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


# Mixins
from braces.views import LoginRequiredMixin

# models
from ..models import PlanAktivnost, PlanKontrolaSkupina

# form
from ..forms import PlanKontrolaSkupinaCreateForm



class PlanKontrolaSkupinaCreateView(LoginRequiredMixin, UpdateView):
    model = PlanAktivnost
    template_name = 'planiranje/plan_kontrola_skupina/create.html'
    fields = ('id', )

    def get_context_data(self, *args, **kwargs):
        context = super(PlanKontrolaSkupinaCreateView, self).get_context_data(*args, **kwargs)
        # tukaj prikažem formset za vnos

        plan_aktivnost = PlanAktivnost.objects.get(id=self.get_object().pk)
        context['plan_kontrola_skupina_create_form'] = PlanKontrolaSkupinaCreateForm()


        return context


    def post(self, request, *args, **kwargs):
        # tukaj napišem funkcijo za dodajanje kontrol skupin preko formseta
        plan_aktivnost = PlanAktivnost.objects.get(pk=self.get_object().pk)

        plan_kontrola_skupina_create_form = PlanKontrolaSkupinaCreateForm(self.request.POST or None)

        if plan_kontrola_skupina_create_form.is_valid():

            naziv = plan_kontrola_skupina_create_form.cleaned_data['naziv']
            zap_st = plan_kontrola_skupina_create_form.cleaned_data['zap_st']
            status = plan_kontrola_skupina_create_form.cleaned_data['status']

            plan_kontrola_skupina = PlanKontrolaSkupina.objects.create(
                naziv=naziv,
                plan_aktivnost=plan_aktivnost,
                zap_st=zap_st,
                status=status,
            )

            plan_kontrola_skupina.save()

            return HttpResponseRedirect(reverse('moduli:planiranje:plan_aktivnost_detail', kwargs={'pk': plan_aktivnost.pk}))


        else:
            return render(
                request,
                self.template_name,
                {
                'plan_kontrola_skupina_create_form': plan_kontrola_skupina_create_form,
                },
            )

class PlanKontrolaSkupinaUpdateView(LoginRequiredMixin, UpdateView):
    model = PlanKontrolaSkupina
    form_class = PlanKontrolaSkupinaCreateForm
    template_name = 'planiranje/plan_kontrola_skupina/update.html'
