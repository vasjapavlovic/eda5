from django.conf.urls import url

from . import views


# Plan
urlpatterns = [
    url(r'^plan-create/$', views.PlanCreateView.as_view(), name="plan_create"),
    url(r'^plan-seznam/$', views.PlanListView.as_view(), name="plan_list"),
    url(r'^plan/(?P<pk>\d+)/detail/$', views.PlanDetailView.as_view(), name="plan_detail"),
]

# PlaniranoOpravilo
urlpatterns += [
    url(r'^planirano-create/(?P<pk>\d+)$', views.PlaniranoOpraviloCreateView.as_view(), name="planirano_opravilo_create"),
    url(r'^planirano-opravilo/(?P<pk>\d+)/detail/$', views.PlaniranoOpraviloDetailView.as_view(), name="planirano_opravilo_detail"),
]
