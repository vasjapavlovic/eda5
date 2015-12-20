from django.conf.urls import url

from . import views


# zahtevek
urlpatterns = [
    url(r'^zahtevek-create/$', views.ZahtevekCreateIzbira.as_view(), name="zahtevek_create"),
    url(r'^zahtevek-seznam/$', views.ZahtevekListView.as_view(), name="zahtevek_list"),

    url(r'^(?P<pk>\d+)/detail/$', views.ZahtevekDetailView.as_view(), name="zahtevek_detail"),
    url(r'^(?P<pk>\d+)/main/update/$', views.ZahtevekUpdateView.as_view(), name="zahtevek_update_main"),
]

# zahtevek škodni dogodek
urlpatterns += [
    url(r'^(?P<pk>\d+)/skodni/update/$', views.ZahtevekUpdateSkodniView.as_view(), name="zahtevek_update_skodni"),
]

# zahtevek sestanek
urlpatterns += [
    url(r'^zahtevek-sestanek/$', views.ZahtevekSestanekCreateView.as_view(), name="zahtevek_create_sestanek"),
    url(r'^podzahtevek-izvedba-del/$', views.PodzahtevekIzvedbaDelCreateView.as_view(),name="podzahtevek_create_izvedba_del"),
    url(r'^(?P<pk>\d+)/sestanek/update/$', views.ZahtevekUpdateSestanekView.as_view(), name="zahtevek_update_sestanek"),
]

# zahtevek izvedba del
urlpatterns += [
    url(r'^zahtevek-izvedba-del/$', views.ZahtevekIzvedbaDelCreateView.as_view(), name="zahtevek_create_izvedba_del"),
    url(r'^podzahtevek-izvedba-del/$', views.PodzahtevekIzvedbaDelCreateView.as_view(), name="podzahtevek_create_izvedba_del"),
    url(r'^(?P<pk>\d+)/izvedba/update/$', views.ZahtevekUpdateIzvedbaView.as_view(), name="zahtevek_update_izvedba"),
]

# opravilo
urlpatterns += [
    url(r'^opravilo-create/(?P<pk>\d+)$', views.OpraviloCreateView.as_view(), name="opravilo_create"),
]
