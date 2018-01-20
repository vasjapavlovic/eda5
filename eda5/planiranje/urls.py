from django.conf.urls import url

from .views import plan, plan_aktivnost, plan_kontrola_skupina, plan_kontrola_specifikacija, plan_kontrola_specifikacija_opcija_select
from .views import planirano_opravilo as po


# Plan
urlpatterns = [
    url(r'^plan-create$', plan.PlanCreateView.as_view(), name="plan_create"),
    url(r'^plan-seznam$', plan.PlanListView.as_view(), name="plan_list"),
    url(r'^plan/(?P<pk>\d+)/detail$', plan.PlanDetailView.as_view(), name="plan_detail"),
    url(r'^plan/(?P<pk>\d+)/update$', plan.PlanUpdateView.as_view(), name="plan_update"),
    url(r'^plan/(?P<pk>\d+)/print$', plan.PlanPrintView.as_view(), name="plan_print"),

]

# PlaniranoOpravilo
urlpatterns += [
    url(r'^planirano-create/(?P<pk>\d+)$', po.PlaniranoOpraviloCreateView.as_view(), name="planirano_opravilo_create"),
    url(r'^(?P<pk>\d+)/vzorec-opravila-create/$', po.VzorecOpravilaCreateView.as_view(), name="vzorec_opravila_create"),
    url(r'^planirano-opravilo/(?P<pk>\d+)/detail/$', po.PlaniranoOpraviloDetailView.as_view(), name="planirano_opravilo_detail"),

    url(r'^plan/(?P<pk>\d+)/planirano-opravilo/create$', po.PlaniranoOpraviloAutoCreateView.as_view(), name="planirano_opravilo_auto_create"),


]


# PlanAktivnost
urlpatterns += [
    url(
        r'^plan/(?P<pk>\d+)/plan-aktivnost/create$',
        plan_aktivnost.PlanAktivnostCreateView.as_view(),
        name="plan_aktivnost_create"
        ),

    url(
        r'^plan-aktivnost/(?P<pk>\d+)/update$',
        plan_aktivnost.PlanAktivnostUpdateView.as_view(),
        name="plan_aktivnost_update"
        ),

    url(
        r'^plan-aktivnost/(?P<pk>\d+)/detail$',
        plan_aktivnost.PlanAktivnostDetailView.as_view(),
        name="plan_aktivnost_detail"
        ),

]

# PlanKontrolaSkupina
urlpatterns += [
    url(
        r'^plan-aktivnost/(?P<pk>\d+)/plan-kontrola-skupina/create$',
        plan_kontrola_skupina.PlanKontrolaSkupinaCreateView.as_view(),
        name="plan_kontrola_skupina_create"
        ),

    url(
        r'^plan-kontrola-skupina/(?P<pk>\d+)/update$',
        plan_kontrola_skupina.PlanKontrolaSkupinaUpdateView.as_view(),
        name="plan_kontrola_skupina_update"
        ),

]

# PlanKontrolaSpecifikacija
urlpatterns += [
    url(
        r'^plan-kontrola-skupina/(?P<pk>\d+)/plan-kontrola-specifikacija/create$',
        plan_kontrola_specifikacija.PlanKontrolaSpecifikacijaCreateView.as_view(),
        name="plan_kontrola_specifikacija_create"
        ),

    url(
        r'^plan-kontrola-specifikacija/(?P<pk>\d+)/update$',
        plan_kontrola_specifikacija.PlanKontrolaSpecifikacijaUpdateView.as_view(),
        name="plan_kontrola_specifikacija_update"
        ),

]


# PlanKontrolaSpecifikacijaOpcijaSelect
urlpatterns += [
    url(
        r'^plan-kontrola-specifikacija/(?P<pk>\d+)/plan-kontrola-specifikacija-opcija-select/create$',
        plan_kontrola_specifikacija_opcija_select.PlanKontrolaSpecifikacijaOpcijaSelectCreateView.as_view(),
        name="plan_kontrola_specifikacija_opcija_select_create"
        ),


    url(
        r'^plan-kontrola-specifikacija-opcija-select/(?P<pk>\d+)/update$',
        plan_kontrola_specifikacija_opcija_select.PlanKontrolaSpecifikacijaOpcijaSelectUpdateView.as_view(),
        name="plan_kontrola_specifikacija_opcija_select_update"
        ),
]
