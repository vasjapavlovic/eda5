from django.shortcuts import render
from django.db.models import Q

from django.views.generic import TemplateView, DetailView, ListView

from eda5.deli.models import DelStavbe
from eda5.etaznalastnina.models import LastniskaEnotaInterna, LastniskaSkupina
from eda5.narocila.models import Narocilo
from eda5.partnerji.models import Partner, Oseba
from eda5.razdelilnik.models import StrosekLE
from eda5.users.models import User

from eda5.lastnistvo.models import PredajaLastnine

from eda5.moduli.models import Zavihek



class PorocanjeUpravnikaDetailView(DetailView):
    model = User
    template_name = "porocanjeupravnika/user/detail/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PorocanjeUpravnikaDetailView, self).get_context_data(*args, **kwargs)

        modul_zavihek = Zavihek.objects.get(oznaka="USER_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        # seznam lastniških enot v lasti
        oseba = Oseba.objects.get(user=self.request.user)
        partner = oseba.podjetje
        skupina_partnerjev_list = partner.skupinapartnerjev_set.all()

        lastniska_enota_interna_prodaja_list = []
        for skupina_partnerjev in skupina_partnerjev_list:
            try:
                predaja_lastnine = PredajaLastnine.objects.get(kupec=skupina_partnerjev)
                for prodaja in predaja_lastnine.prodajalastnine_set.all():
                    lastniska_enota_elaborat = prodaja.lastniska_enota

                    for lastniska_enota_interna in lastniska_enota_elaborat.lastniskaenotainterna_set.all():
                        lastniska_enota_interna_prodaja_list.append(lastniska_enota_interna)
            except:
                pass

        lastniska_enota_interna_najem_list = []
        for skupina_partnerjev in skupina_partnerjev_list:
            try:
                predaja_lastnine = PredajaLastnine.objects.get(kupec=skupina_partnerjev)
                for prodaja in predaja_lastnine.najemlastnine_set.all():
                    lastniska_enota_interna = prodaja.lastniska_enota
                    lastniska_enota_interna_najem_list.append(lastniska_enota_interna)

            except:
                pass


        context['lastniska_enota_interna_prodaja_list'] = lastniska_enota_interna_prodaja_list
        context['lastniska_enota_interna_najem_list'] = lastniska_enota_interna_najem_list



        return context






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
