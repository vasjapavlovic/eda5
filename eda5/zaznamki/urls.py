from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        r'^(?P<pk>\d+)/zaznamek-update/$', 
        views.ZaznamekUpdateFromZahtevekView.as_view(), 
        name="zaznamek_update"
    ),

    url(
        r'^/zahtevek/(?P<pk>\d+)/zaznamek-create/$', 
        views.ZaznamekCreateFromZahtevek.as_view(), 
        name="zaznamek_create_from_zahtevek"
    ),

    url(
        r'^/reklamacija/(?P<pk>\d+)/zaznamek-create/$', 
        views.ZaznamekCreateFromReklamacija.as_view(), 
        name="zaznamek_create_from_reklamacija"
    ),

    url(
        r'^/delovninalog/(?P<pk>\d+)/zaznamek-create/$', 
        views.ZaznamekCreateFromDelovniNalog.as_view(), 
        name="zaznamek_create_from_delovninalog"
    ),


]