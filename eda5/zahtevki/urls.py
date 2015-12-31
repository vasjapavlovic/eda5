from django.conf.urls import url

from .views import splosno, sestanek, izvedba_dela


# zahtevek
urlpatterns = [
    url(r'^zahtevek-create/$', splosno.ZahtevekCreateIzbiraView.as_view(), name="zahtevek_create"),
    url(r'^zahtevek-seznam/$', splosno.ZahtevekListView.as_view(), name="zahtevek_list"),
    url(r'^reload_controls_element_podskupina.html$', splosno.reload_controls_element_podskupina_view, name='reload_controls_element_podskupina'),
    url(r'^reload_controls_element_del_stavbe.html$', splosno.reload_controls_element_del_stavbe_view, name='reload_controls_element_del_stavbe'),
    url(r'^reload_controls_element_element.html$', splosno.reload_controls_element_element_view, name='reload_controls_element_element'),

    url(r'^(?P<pk>\d+)/detail/$', splosno.ZahtevekDetailView.as_view(), name="zahtevek_detail"),
    url(r'^(?P<pk>\d+)/main/update/$', splosno.ZahtevekUpdateView.as_view(), name="zahtevek_update_main"),
]

# zahtevek škodni dogodek
# urlpatterns += [
#     url(r'^(?P<pk>\d+)/skodni/update/$', skodni_dogodek.ZahtevekUpdateSkodniView.as_view(), name="zahtevek_update_skodni"),
# ]

# zahtevek sestanek
urlpatterns += [
    url(r'^zahtevek-sestanek/$', sestanek.ZahtevekSestanekCreateView.as_view(), name="zahtevek_create_sestanek"),
    url(r'^reload_controls.html$', sestanek.reload_controls_view, name='reload_controls'),
    url(r'^(?P<pk>\d+)/podzahtevek-sestanek-create/$', sestanek.PodzahtevekSestanekCreateView.as_view(), name="podzahtevek_create_sestanek"),
    url(r'^(?P<pk>\d+)/sestanek/update/$', sestanek.ZahtevekUpdateSestanekView.as_view(), name="zahtevek_update_sestanek"),
]

# zahtevek izvedba del
urlpatterns += [
    url(r'^zahtevek-izvedba-del/$', izvedba_dela.ZahtevekIzvedbaDelCreateView.as_view(), name="zahtevek_create_izvedba_del"),
    url(r'^(?P<pk>\d+)/podzahtevek-izvedba-del-create/$', izvedba_dela.PodzahtevekIzvedbaDelCreateView.as_view(),name="podzahtevek_create_izvedba_del"),
    url(r'^(?P<pk>\d+)/izvedba/update/$', izvedba_dela.ZahtevekUpdateIzvedbaView.as_view(), name="zahtevek_update_izvedba"),
]

# opravilo
urlpatterns += [
    url(r'^opravilo-create/(?P<pk>\d+)$', splosno.OpraviloCreateView.as_view(), name="opravilo_create"),
]
