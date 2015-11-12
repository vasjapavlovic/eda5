from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ZahtevekHomeView.as_view(), name="home"),
    url(r'^seznam/$', views.ZahtevekListView.as_view(), name="zahtevek_list"),
    url(r'^(?P<pk>\d+)/detail/$', views.ZahtevekDetailView.as_view(), name="zahtevek_detail"),
    url(r'^create/$', views.ZahtevekCreateView.as_view(), name="zahtevek_create"),
    url(r'^(?P<pk>\d+)/update/$', views.ZahtevekUpdateView.as_view(), name="zahtevek_update"),
]
