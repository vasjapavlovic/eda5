from django.conf.urls import url

from . import views

# HOME
urlpatterns = [
]

# Arhiviranje
urlpatterns += [
    url(r'^arhiviranje/popup-list/?$', views.ArhiviranjePopUpListView.as_view(), name='arhiviranje_popup_list'),


    url(
        r'^zahtevek/(?P<pk>\d+)/arhiviranje-create/$',
        views.ArhiviranjeCreateFromZahtevek.as_view(),
        name="arhiviranje_create_from_zahtevek"
    ),

    url(
        r'^razdelilnik/(?P<pk>\d+)/arhiviranje-create/$',
        views.ArhiviranjeCreateFromRazdelilnik.as_view(),
        name="arhiviranje_create_from_razdelilnik"
    ),

    url(
        r'^reklamacija/(?P<pk>\d+)/arhiviranje-create/$',
        views.ArhiviranjeCreateFromReklamacija.as_view(),
        name="arhiviranje_create_from_reklamacija"
    ),

    url(
        r'^delovninalog/(?P<pk>\d+)/arhiviranje-create/$',
        views.ArhiviranjeCreateFromDelovniNalog.as_view(),
        name="arhiviranje_create_from_delovninalog"
    ),

    url(
        r'^dobava/(?P<pk>\d+)/arhiviranje-create/$',
        views.ArhiviranjeCreateFromDobava.as_view(),
        name="arhiviranje_create_from_dobava"
    ),

    url(
        r'^sestanek/(?P<pk>\d+)/arhiviranje-create/$',
        views.ArhiviranjeCreateFromSestanek.as_view(),
        name="arhiviranje_create_from_sestanek"
    ),

    url(
        r'^povprasevanje/(?P<pk>\d+)/arhiviranje-create/$',
        views.ArhiviranjeCreateFromPovprasevanje.as_view(),
        name="arhiviranje_create_from_povprasevanje"
    ),

    url(
        r'^dogodek/(?P<pk>\d+)/arhiviranje-create/$',
        views.ArhiviranjeCreateFromDogodek.as_view(),
        name="arhiviranje_create_from_dogodek"
    ),

    url(
        r'^pomanjkljivost/(?P<pk>\d+)/arhiviranje-create/$',
        views.ArhiviranjeCreateFromPomanjkljivost.as_view(),
        name="arhiviranje_create_from_pomanjkljivost"
    ),

]
