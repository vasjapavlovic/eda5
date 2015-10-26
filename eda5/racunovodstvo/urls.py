from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.RacunovodstvoHomeView.as_view(),
        name='home'
    ),
    url(
        regex=r'^(?P<pk>\d+)/detail/$',
        view=views.RacunovodstvoRacunDetail.as_view(),
        name='detail'
    ),
    url(
        regex=r'^likvidacija/$',
        view=views.RacunovodstvoRacuniLikvidacija.as_view(),
        name='list_likvidacija'
    ),
    url(
        regex=r'^likvidirano/$',
        view=views.RacunovodstvoRacuniList.as_view(),
        name='list_likvidirano'
    ),
    url(
        regex=r'^(?P<pk>\d+)/detail/likvidacija/$',
        view=views.RacunovodstvoLikvidacijaDetail.as_view(),
        name='detail_likvidacija'
    ),
]
