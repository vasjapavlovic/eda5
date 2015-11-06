from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.AppHomeView.as_view(), name="home"),
    url(r'^seznam/$', views.OpraviloListView.as_view(), name="opravilo_list"),
    url(r'^(?P<pk>\d+)/detail$', views.OpraviloDetailView.as_view(), name="opravilo_detail"),
    url(r'^(?P<pk>\d+)/update$', views.OpraviloUpdateView.as_view(), name="opravilo_update"),

]
