from django.conf.urls import url


from .views import opravilo, delovninalog, delo

from eda5.deli.views.projektnomesto import ProjektnoMestoCreateView



# HOME
urlpatterns = [
]


# DELOVNI NALOG
urlpatterns += [

    url(r'^dn/popup-list/?$', delovninalog.DelovniNalogPopUpListView.as_view(), name='delovninalog_popup_list'),


    url(r'^dn/$',
        delovninalog.DelovniNalogList.as_view(),
        name="dn_list"),


    url(r'^dn/(?P<pk>\d+)/detail$',
        delovninalog.DelovniNalogDetailView.as_view(),
        name="dn_detail"),


    url(r'^dn/(?P<pk>\d+)/update/vcakanju$',
        delovninalog.DelovniNalogUpdateVcakanjuView.as_view(),
        name="dn_update_vcakanju"),


    url(r'^dn/(?P<pk>\d+)/update/vresevanju$',
        delovninalog.DelovniNalogUpdateVresevanjuView.as_view(),
        name="dn_update_vresevanju"),

]

# OPRAVILO
urlpatterns += [


    # Seznam opravil
    url(r'^opravila/$',
        opravilo.OpraviloListView.as_view(),
        name="opravilo_list"),


    #  Pregled Opravila
    url(r'^opravila/(?P<pk>\d+)/detail$',
        opravilo.OpraviloDetailView.as_view(),
        name="opravilo_detail"),


    # Posodobitev opravila
    url(r'^opravila/(?P<pk>\d+)/update$',
        opravilo.OpraviloUpdateView.as_view(),
        name="opravilo_update"),


    # Pregled vzorca opravila
    url(r'^vzorec-opravila/(?P<pk>\d+)/detail$',
        opravilo.OpraviloVzorecDetailView.as_view(),
        name="vzorec_opravila_detail"),


    # Izdelava splošnega opravila iz zahtevka
    url(r'^opravilo-create/(?P<pk>\d+)$',
        opravilo.OpraviloCreateFromZahtevekView.as_view(),
        name="opravilo_create_from_zahtevek"),


    # Izdelava opravila za likvidacijo pomanjkljivosti
    url(r'^opravilo-create-pomanjkljivosti/(?P<pk>\d+)$',
        opravilo.OpraviloCreatePomanjkljivosti.as_view(),
        name="opravilo_create_pomanjkljivosti"),


    # Izdelava opravila iz vzorca in zahtevkov
    url(r'^opravilo-from-vzorec-create/(?P<pk>\d+)$',
        opravilo.OpraviloCreateFromVzorecFromZahtevekView.as_view(),
        name="opravilo_create_from_vzorec_from_zahtevek"),





    # ##########################################################
    # FILTRIRANJE
    # ##########################################################

    # IZBIRA VZORCA OPRAVILA
    # Filtriranje glede na izbrano kategorijo planov
    url(r'^reload_controls_planiranje_skupina_planov.html$',
        opravilo.reload_controls_planiranje_skupina_planov_view,
        name='reload_controls_planiranje_skupina_planov'),

    # Filtriranje glede na izbrani plan
    url(r'^reload_controls_planiranje_plan.html$',
        opravilo.reload_controls_planiranje_plan_view,
        name='reload_controls_planiranje_plan'),

    # Filtriranje glede na izbrano opravilo
    url(r'^reload_controls_delovninalogi_planirano_opravilo.html$',
        opravilo.reload_controls_delovninalogi_planirano_opravilo_view,
        name='reload_controls_delovninalogi_planirano_opravilo'),


]


# DELO
urlpatterns += [


    url(r'^delo/(?P<pk>\d+)/create/$',
        delo.DeloCreateFromDelovniNalogView.as_view(),
        name="delo_create_from_delovninalog"),


    url(r'^delo/(?P<pk>\d+)/update/koncaj/$',
        delo.DeloKoncajUpdateView.as_view(),
        name="delo_koncaj_update"),


    url(r'^delo/(?P<pk>\d+)/update/$',
        delo.DeloUpdateView.as_view(),
        name="delo_update_from_delovninalog"),
]




