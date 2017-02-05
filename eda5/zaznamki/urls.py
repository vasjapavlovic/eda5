from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        r'^(?P<pk>\d+)/zaznamek-update/$', 
        views.ZaznamekUpdateFromZahtevekView.as_view(), 
        name="zaznamek_update"),


]