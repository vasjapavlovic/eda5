from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        r'^(?P<pk>\d+)/zaznamek-update/$',
        views.ZaznamekUpdateFromZahtevekView.as_view(),
        name="zaznamek_update"
    ),

    url(
        r'^zahtevek/(?P<pk>\d+)/zaznamek-create/$',
        views.ZaznamekCreateFromZahtevek.as_view(),
        name="zaznamek_create_from_zahtevek"
    ),

    url(
        r'^razdelilnik/(?P<pk>\d+)/zaznamek-create/$',
        views.ZaznamekCreateFromRazdelilnik.as_view(),
        name="zaznamek_create_from_razdelilnik"
    ),

    url(
        r'^reklamacija/(?P<pk>\d+)/zaznamek-create/$',
        views.ZaznamekCreateFromReklamacija.as_view(),
        name="zaznamek_create_from_reklamacija"
    ),

    url(
        r'^delovninalog/(?P<pk>\d+)/zaznamek-create/$',
        views.ZaznamekCreateFromDelovniNalog.as_view(),
        name="zaznamek_create_from_delovninalog"
    ),

    url(
        r'^dobava/(?P<pk>\d+)/zaznamek-create/$',
        views.ZaznamekCreateFromDobava.as_view(),
        name="zaznamek_create_from_dobava"
    ),

    url(
        r'^sestanek/(?P<pk>\d+)/zaznamek-create/$',
        views.ZaznamekCreateFromSestanek.as_view(),
        name="zaznamek_create_from_sestanek"
    ),

    url(
        r'^povprasevanje/(?P<pk>\d+)/zaznamek-create/$',
        views.ZaznamekCreateFromPovprasevanje.as_view(),
        name="zaznamek_create_from_povprasevanje"
    ),

    url(
        r'^dogodek/(?P<pk>\d+)/zaznamek-create/$',
        views.ZaznamekCreateFromDogodek.as_view(),
        name="zaznamek_create_from_dogodek"
    ),

    url(
        r'^pomanjkljivost/(?P<pk>\d+)/zaznamek-create/$',
        views.ZaznamekCreateFromPomanjkljivost.as_view(),
        name="zaznamek_create_from_pomanjkljivost"
    ),

]
