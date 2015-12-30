from django.conf.urls import url

from . import views



# HOME
urlpatterns = [
    url(r'^$', views.NarocilaHomeView.as_view(), name="home"),
]


# NAROCILO
urlpatterns += [
    url(r'^narocilo-create/$', views.NarociloCreateIzbiraView.as_view(), name="narocilo_create"),
    url(r'^narocilo-create-telefon/$', views.NarociloTelefonCreateView.as_view(), name="narocilo_create_telefon"),
    url(r'^reload_controls.html$', views.reload_controls_view, name='reload_controls'),
    url(r'^seznam/$', views.NarociloListView.as_view(), name="narocilo_list"),
    url(r'^(?P<pk>\d+)/detail$', views.NarociloDetailView.as_view(), name="narocilo_detail"),
]
