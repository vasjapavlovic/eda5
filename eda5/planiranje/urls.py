from django.conf.urls import url

from .views import plan
from .views import planirano_opravilo as po


# Plan
urlpatterns = [
    url(r'^plan-create/$', plan.PlanCreateView.as_view(), name="plan_create"),
    url(r'^plan-seznam/$', plan.PlanListView.as_view(), name="plan_list"),
    url(r'^plan/(?P<pk>\d+)/detail/$', plan.PlanDetailView.as_view(), name="plan_detail"),
]

# PlaniranoOpravilo
urlpatterns += [
    url(r'^planirano-create/(?P<pk>\d+)$', po.PlaniranoOpraviloCreateView.as_view(), name="planirano_opravilo_create"),
    url(r'^(?P<pk>\d+)/vzorec-opravila-create/$', po.VzorecOpravilaCreateView.as_view(), name="vzorec_opravila_create"),
    url(r'^planirano-opravilo/(?P<pk>\d+)/detail/$', po.PlaniranoOpraviloDetailView.as_view(), name="planirano_opravilo_detail"),
]
