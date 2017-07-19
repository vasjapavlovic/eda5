from django.conf.urls import url

from . import views

urlpatterns = [

]

# NALOGE
urlpatterns += [


    url(  # Izdelava naloge preko vmesnika
        r'^create/$',
        views.NalogaCreateView.as_view(),
        name="naloga_create"
    ),


    url(  # Izdelava naloge preko zahtevka
        r'^(?P<pk>\d+)/create-from-zahtevek/$',
        views.NalogaCreateFromZahtevekView.as_view(),
        name="naloga_create_from_zahtevek"
    ),


    url(  # Izbira naloge za dodelitev zahtevku
        r'^(?P<pk>\d+)/izbira/$',
        views.NalogaIzbiraFromZahtevek.as_view(),
        name="naloga_izbira_from_zahtevek"
    ),

    url(  # Izdelava naloge preko sestanka
        r'^(?P<pk>\d+)/create-from-sestanek/$',
        views.NalogaCreateFromSestanekView.as_view(),
        name="naloga_create_from_sestanek"
    ),
    


    url(  # Posodobitev naloge - update
        r'^(?P<pk>\d+)/naloga-update/$',
        views.NalogaUpdateView.as_view(),
        name="naloga_update"
    ),

    


    url(
        r'^seznam/$',
        views.NalogaListView.as_view(),
        name="naloga_list"
    ),


    url(
        r'^(?P<pk>\d+)/detail/$',
        views.NalogaDetailView.as_view(),
        name="naloga_detail"
    ),

]


