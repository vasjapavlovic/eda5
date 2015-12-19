from django.conf.urls import url

from . import views



# HOME
urlpatterns = [
    url(r'^$', views.NarocilaHomeView.as_view(), name="home"),
]


# NAROCILO
urlpatterns += [
    url(r'^dn/(?P<pk>\d+)/detail$', views.NarociloDetailView.as_view(), name="narocilo_detail"),
    url(r'^narocilo-telefon/$', views.NarociloTelefonCreateView.as_view(), name="narocilo_create_telefon"),
]
