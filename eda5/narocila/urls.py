from django.conf.urls import url

from . import views



# HOME
urlpatterns = [
    url(r'^$', views.NarocilaHomeView.as_view(), name="home"),
]


# NAROCILO
urlpatterns += [
    url(
        r'^from-zahtevek/(?P<pk>\d+)/narocilo-create/$', 
        views.NarociloCreateIzbiraView.as_view(), 
        name="narocilo_create"
    ),

    url(
        r'^from-zahtevek/(?P<pk>\d+)/narocilo-create-telefon/$', 
        views.NarociloTelefonCreateView.as_view(), 
        name="narocilo_create_telefon"
    ),

    url(
        r'^from-zahtevek/(?P<pk>\d+)/narocilo-create-dokument/$', 
        views.NarociloDokumentCreateView.as_view(), 
        name="narocilo_create_dokument"
    ),

    url(
        r'^from-zahtevek/(?P<pk>\d+)/narocilo-update-dokument/$', 
        views.NarociloDokumentUpdateView.as_view(), 
        name="narocilo_update_dokument"
    ),


    url(r'^seznam/$', 
        views.NarociloListView.as_view(), 
        name="narocilo_list"
        ),

    url(r'^(?P<pk>\d+)/detail$', 
        views.NarociloDetailView.as_view(), 
        name="narocilo_detail"
        ),

    # ##########################################################
    # FILTRIRANJE
    # ##########################################################

    # Pri izbiri naročila naj bodo na razpolago samo nosilci, ki so v partnerjih kot
    # naročnik in izvajalec
    url(r'^reload_controls_narocilo_osebe.html$', 
        views.reload_controls_narocilo_osebe_view, 
        name='reload_controls_narocilo_osebe'
        ),
]
