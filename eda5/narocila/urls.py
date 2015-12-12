from django.conf.urls import url

from . import views



# HOME
urlpatterns = [
    url(r'^$', views.NarocilaHomeView.as_view(), name="home"),
]


# NAROCILO
urlpatterns += [
    url(r'^narocilo-telefon/$', views.NarociloTelefonCreateView.as_view(), name="narocilo_create_telefon"),
]
