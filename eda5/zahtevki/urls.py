from django.conf.urls import url

from .views import splosno, sestanek, izvedba_dela, predaja_lastnine, analiza, povprasevanje, reklamacija, dogodek

# zahtevek
urlpatterns = [
    url(r'^zahtevek/popup-list/?$', splosno.ZahtevekPopUpListView.as_view(), name='zahtevek_popup_list'),   

    url(r'^zahtevek-create/$', splosno.ZahtevekCreateIzbiraView.as_view(), name="zahtevek_create"),
    url(r'^zahtevek-seznam/$', splosno.ZahtevekListView.as_view(), name="zahtevek_list"),


    url(r'^(?P<pk>\d+)/detail/$', splosno.ZahtevekDetailView.as_view(), name="zahtevek_detail"),
    url(r'^(?P<pk>\d+)/main/update/$', splosno.ZahtevekUpdateView.as_view(), name="zahtevek_update_main"),

]



# zahtevek sestanek
urlpatterns += [
    url(r'^zahtevek-sestanek/$', sestanek.ZahtevekSestanekCreateView.as_view(), name="zahtevek_create_sestanek"),
    url(r'^(?P<pk>\d+)/podzahtevek-sestanek-create/$', sestanek.PodzahtevekSestanekCreateView.as_view(), name="podzahtevek_create_sestanek"),
    url(r'^(?P<pk>\d+)/sestanek/update/$', sestanek.ZahtevekUpdateSestanekView.as_view(), name="zahtevek_update_sestanek"),
    
]

# zahtevek izvedba del
urlpatterns += [
    url(r'^zahtevek-izvedba-del/$', izvedba_dela.ZahtevekIzvedbaDelCreateView.as_view(), name="zahtevek_create_izvedba_del"),
    url(r'^(?P<pk>\d+)/podzahtevek-izvedba-del-create/$', izvedba_dela.PodzahtevekIzvedbaDelCreateView.as_view(),name="podzahtevek_create_izvedba_del"),
    url(r'^(?P<pk>\d+)/izvedba/update/$', izvedba_dela.ZahtevekUpdateIzvedbaView.as_view(), name="zahtevek_update_izvedba"),

]


# Predaja Lastnine
urlpatterns += [
    url(r'^zahtevek-predaja-lastnine-create/$', predaja_lastnine.ZahtevekPredajaLastnineCreateView.as_view(), name="zahtevek_create_predaja_lastnine"),
    url(r'^(?P<pk>\d+)/prodaja-lastnine-create/$', predaja_lastnine.ProdajaLastnineCreateView.as_view(), name="prodaja_lastnine_create"),
    url(r'^(?P<pk>\d+)/prodaja-lastnine-update/$', predaja_lastnine.ProdajaLastnineUpdateView.as_view(), name="prodaja_lastnine_update"),
    url(r'^(?P<pk>\d+)/najem-lastnine-create/$', predaja_lastnine.NajemLastnineCreateView.as_view(), name="najem_lastnine_create"),
    url(r'^(?P<pk>\d+)/najem-lastnine-vracilo/$', predaja_lastnine.NajemLastnineVraciloView.as_view(), name="najem_lastnine_vracilo"),
    url(r'^(?P<pk>\d+)/predaja-kljuca-create/$', predaja_lastnine.PredajaKljucaCreateView.as_view(), name="predaja_kljuca_create"),
    url(r'^(?P<pk>\d+)/vracilo-kljuca-create/$', predaja_lastnine.VraciloKljucaUpdateView.as_view(), name="vracilo_kljuca_create"),
]



# zahtevek analiza
urlpatterns += [
    url(r'^zahtevek-analiza/$', analiza.ZahtevekAnalizaCreateView.as_view(), name="zahtevek_create_analiza"),
    # url(r'^reload_controls.html$', sestanek.reload_controls_view, name='reload_controls'),
    url(r'^(?P<pk>\d+)/podzahtevek-analiza-create/$', analiza.PodzahtevekAnalizaCreateView.as_view(), name="podzahtevek_create_analiza"),
]


# zahtevek povprasevanje
urlpatterns += [
    url(r'^zahtevek-povprasevanje/$', povprasevanje.ZahtevekPovprasevanjeCreateView.as_view(), name="zahtevek_create_povprasevanje"),
    # url(r'^reload_controls.html$', sestanek.reload_controls_view, name='reload_controls'),
    url(r'^(?P<pk>\d+)/podzahtevek-povprasevanje-create/$', povprasevanje.PodzahtevekPovprasevanjeCreateView.as_view(), name="podzahtevek_create_povprasevanje"), 
]


# zahtevek povprasevanje
urlpatterns += [
    url(r'^zahtevek-reklamacija/$', reklamacija.ZahtevekReklamacijaCreateView.as_view(), name="zahtevek_create_reklamacija"),
    # url(r'^reload_controls.html$', sestanek.reload_controls_view, name='reload_controls'),
    url(r'^(?P<pk>\d+)/podzahtevek-reklamacija-create/$', reklamacija.PodzahtevekReklamacijaCreateView.as_view(), name="podzahtevek_create_reklamacija"), 
]