# DJANGO ##############################################################
from django.core.urlresolvers import reverse
from django.db.models import F, Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DetailView, UpdateView

# Mixins
from braces.views import LoginRequiredMixin

# Models
from .models import Parameter
from eda5.kontrolnilist.models import KontrolaVrednost
from eda5.moduli.models import \
    Zavihek

class ParameterDetailView(LoginRequiredMixin, DetailView):

    model = Parameter
    template_name = "servisnaknjiga/parameter/detail.html"


    def get_context_data(self, *args, **kwargs):
        context = super(ParameterDetailView, self).get_context_data(*args, **kwargs)
        modul_zavihek = Zavihek.objects.get(oznaka="ELEMENT_DETAIL")
        context['modul_zavihek'] = modul_zavihek

        parameter = Parameter.objects.get(id=self.get_object().id)

        parameter_kontrola_vrednost_list = KontrolaVrednost.objects.filter(
            projektno_mesto=parameter.projektno_mesto,
            kontrola_specifikacija__plan_kontrola_specifikacija = parameter.plan_kontrola_specifikacija
        )

        parameter_kontrola_vrednost_list = parameter_kontrola_vrednost_list.order_by(
            'delovni_nalog__datum_start',

        )

        context['parameter_kontrola_vrednost_list'] = parameter_kontrola_vrednost_list

        return context
