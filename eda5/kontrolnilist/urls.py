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


]
