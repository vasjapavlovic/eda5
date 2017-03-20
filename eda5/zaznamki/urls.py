from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        r'^(?P<pk>\d+)/zaznamek-update/$', 
        views.ZaznamekUpdateFromZahtevekView.as_view(), 
        name="zaznamek_update"
    ),

    url(
        r'^(?P<pk>\d+)/zaznamek-create/$', 
        views.ZaznamekCreateFromZahtevek.as_view(), 
        name="zaznamek_create_from_zahtevek"
    ),


]