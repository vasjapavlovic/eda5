from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.PomanjkljivostiHomeView.as_view(), name="home")
]

# POMANJKLJIVOST
urlpatterns += [


    url(  # Izdelava pomanjkljivosti preko vmesnika
        r'^create/$',
        views.PomanjkljivostCreateView.as_view(),
        name="pomanjkljivost_create"
    ),


    url(  # Izdelava pomanjkljivosti preko zahtevka
        r'^(?P<pk>\d+)/create-from-zahtevek/$',
        views.PomanjkljivostCreateFromZahtevekView.as_view(),
        name="pomanjkljivost_create_from_zahtevek"
    ),


    url(
        r'^seznam/$',
        views.PomanjkljivostListView.as_view(),
        name="pomanjkljivost_list"
    ),


    url(
        r'^(?P<pk>\d+)/detail/$',
        views.PomanjkljivostDetailView.as_view(),
        name="pomanjkljivost_detail"
    ),

]
