from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ZahtevekHomeView.as_view(), name="home"),
    url(r'^seznam/$', views.ZahtevekListView.as_view(), name="zahtevek_list"),
    url(r'^(?P<pk>\d+)/detail/$', views.ZahtevekDetailView.as_view(), name="zahtevek_detail"),
    url(r'^create/$', views.ZahtevekCreateView.as_view(), name="zahtevek_create"),
    # update zahtevek main
    url(r'^(?P<pk>\d+)/main/update/$', views.ZahtevekUpdateView.as_view(), name="zahtevek_update_main"),
    # update vrste zahtevka
    url(r'^(?P<pk>\d+)/skodni/update/$', views.ZahtevekUpdateSkodniView.as_view(), name="zahtevek_update_skodni"),
    url(r'^(?P<pk>\d+)/sestanek/update/$', views.ZahtevekUpdateSestanekView.as_view(), name="zahtevek_update_sestanek"),
    url(r'^(?P<pk>\d+)/izvedba/update/$', views.ZahtevekUpdateIzvedbaView.as_view(), name="zahtevek_update_izvedba"),

    url(r'^(?P<pk>\d+)/dokument/update/$', views.ZahtevekUpdateDokumentFormView.as_view(), name="zahtevek_update_dokument"),
]
