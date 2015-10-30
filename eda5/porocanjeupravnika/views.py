from django.shortcuts import render
from django.db.models import Q

from django.views.generic import TemplateView, DetailView, ListView

from eda5.deli.models import DelStavbe
from eda5.etaznalastnina.models import LastniskaEnotaInterna, LastniskaSkupina
from eda5.narocila.models import Narocilo
from eda5.partnerji.models import Partner
from eda5.razdelilnik.models import StrosekLE
from eda5.users.models import User


class PorocanjeHomeView(TemplateView):
    template_name = "porocanjeupravnika/home.html"


class PorocanjePrejetiracuniHomeView(TemplateView):
    template_name = "porocanjeupravnika/prejetiracuni/home.html"


class LastninaHomeView(TemplateView):
    template_name = "porocanjeupravnika/lastnina/home.html"


class LastninaListView(ListView):
    template_name = "porocanjeupravnika/lastnina/list.html"
    model = LastniskaEnotaInterna

    def get_context_data(self, *args, **kwargs):
        context = super(LastninaListView, self).get_context_data(*args, **kwargs)
        context['current_partner'] = Partner.objects.get(user=self.request.user.id)
        return context

    def get_queryset(self):
        queryset = super(LastninaListView, self).get_queryset()
        # iz modela Partner poberemo .id ki je enak logiranemu userju
        current_user = Partner.objects.get(user=self.request.user.id)
        # filtriramo vnose kjer je lastnik = logirani partner
        queryset = queryset.filter(Q(lastnik=current_user.id) | Q(najemnik=current_user.id))
        # queryset = queryset.filter(lastnik=current_user.id)  # self.user
        return queryset


class LastniskaEnotaInternaDetailView(DetailView):
    template_name = "porocanjeupravnika/lastnina/lastniskaenota_detail.html"
    model = LastniskaEnotaInterna


class NarociloHomeView(TemplateView):
    template_name = "porocanjeupravnika/narocila/home.html"


class NarociloListView(ListView):
    template_name = "porocanjeupravnika/narocila/narocilo_list.html"
    model = Narocilo

    def get_context_data(self, *args, **kwargs):
        context = super(NarociloListView, self).get_context_data(*args, **kwargs)
        context['current_partner'] = Partner.objects.get(user=self.request.user.id)
        return context

# class RazdelilnikListView(ListView):
#     model = StrosekLE
#     template_name = "porocanjeupravnika/prejetiracuni/razdelilnik_list.html"

#     def get_queryset(self):
#         queryset = super(views.RazdelilnikListView, self).get_queryset()
#         queryset = queryset.lastniska_enota.lastnik.filter(id=self.user.id)
#         return queryset
