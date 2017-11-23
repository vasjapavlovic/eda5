from django.conf.urls import url

from .views.dogodek_views import DogodekCreateFromZahtevekView, DogodekUpdateFromZahtevekView


urlpatterns = [
]


urlpatterns += [


    url(r'^(?P<pk>\d+)/dogodek/create/$',
        DogodekCreateFromZahtevekView.as_view(),
        name="dogodek_create_from_zahtevek"
    ),


    url(r'^(?P<pk>\d+)/dogodek/update/$',
        DogodekUpdateFromZahtevekView.as_view(),
        name="dogodek_update_from_zahtevek"
    ),


]
