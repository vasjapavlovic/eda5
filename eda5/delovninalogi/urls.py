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
    url(r'^dn/(?P<pk>\d+)/update/vplanu$', views.DelovniNalogUpdateVplanuView.as_view(), name="dn_update_vplanu"),
    url(r'^dn/(?P<pk>\d+)/update/vresevanju$', views.DelovniNalogUpdateVresevanjuView.as_view(), name="dn_update_vresevanju"),
    # url(r'^dn/(?P<pk>\d+)/update/dokument$', views.DelovniNalogUpdateDokumentFormView.as_view(), name="dn_update_dokument"),
]

# OPRAVILO
urlpatterns += [
    url(r'^opravila/$', views.OpraviloListView.as_view(), name="opravilo_list"),
    url(r'^opravila/(?P<pk>\d+)/detail$', views.OpraviloDetailView.as_view(), name="opravilo_detail"),
    url(r'^opravila/(?P<pk>\d+)/update$', views.OpraviloUpdateView.as_view(), name="opravilo_update"),
]

# VZOREC OPRAVILA
urlpatterns += [
    url(r'^vzorec-opravila/(?P<pk>\d+)/detail$', views.VzorecOpravilaDetailView.as_view(), name="vzorec_opravila_detail"),
]


# DELO
urlpatterns += [
    url(r'^delo/(?P<pk>\d+)/update/$', views.DeloZacetoUpdateView.as_view(), name="delo_update"),
]




