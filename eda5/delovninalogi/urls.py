from django.conf.urls import url

from . import views



# HOME
urlpatterns = [
    url(r'^$', views.AppHomeView.as_view(), name="home"),
]


# DELOVNI NALOG
urlpatterns += [
    url(r'^dn/$', views.DelovniNalogList.as_view(), name="dn_list"),
    url(r'^dn/(?P<pk>\d+)/detail$', views.DelovniNalogDetailView.as_view(), name="dn_detail"),
    url(r'^dn/(?P<pk>\d+)/update/vcakanju$', views.DelovniNalogUpdateVcakanjuView.as_view(), name="dn_update_vcakanju"),
    url(r'^dn/(?P<pk>\d+)/update/vresevanju$', views.DelovniNalogUpdateVresevanjuView.as_view(), name="dn_update_vresevanju"),
]


# OPRAVILO
urlpatterns += [
    url(r'^opravila/$', views.OpraviloListView.as_view(), name="opravilo_list"),
    url(r'^opravila/(?P<pk>\d+)/detail$', views.OpraviloDetailView.as_view(), name="opravilo_detail"),
    url(r'^opravila/(?P<pk>\d+)/update$', views.OpraviloUpdateView.as_view(), name="opravilo_update"),

]