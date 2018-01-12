from django.conf.urls import url

from . import views


# HOME
urlpatterns = [
]


urlpatterns += [



    #  Pregled Opravila
    url(
        r'^opravilo/(?P<pk>\d+)/aktivnost/create$',
        views.KontrolniListSpecifikacijaCreateView.as_view(),
        name="kontrolni_list_aktivnost_create"
    ),

    url(
        r'^aktivnost/(?P<pk>\d+)/update$',
        views.KontrolniListAktivnostUpdateView.as_view(),
        name="kontrolni_list_aktivnost_update"
    ),

    url(
        r'^dn/(?P<pk>\d+)/kontrola-vrednost-create$',
        views.KontrolaVrednostCreateView.as_view(),
        name="kontrola_vrednost_create"
    ),

    url(
        r'^(?P<pk>\d+)/kontrolni-list-update-oblika01$',
        views.KontrolniListUpdateOblika01View.as_view(),
        name="kontrolni_list_update_oblika01"
    ),


    url(
        r'^(?P<pk>\d+)/kontrolni-list-update-oblika02$',
        views.KontrolniListUpdateOblika02View.as_view(),
        name="kontrolni_list_update_oblika02"
    ),


    url(
        r'^(?P<pk>\d+)/kontrolni-list-print-oblika01$',
        views.KontrolniListPrintOblika01View.as_view(),
        name="kontrolni_list_print_oblika01"
    ),


]
