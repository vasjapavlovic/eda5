from django.conf.urls import url

from . import views


# HOME
urlpatterns = [
    url(r'^$', views.SkladisceHomeView.as_view(), name="home"),
]

# DOBAVA
urlpatterns += [
    url(r'^dobava/create/$', views.DobavaCreateView.as_view(), name="dobava_create"),
    url(r'^dobava/seznam/$', views.DobavaListView.as_view(), name="dobava_list"),
    url(r'^dobava/(?P<pk>\d+)/detail/$', views.DobavaDetailView.as_view(), name="dobava_detail"),
]

# DNEVNIK
urlpatterns += [
    url(r'^dnevnik/seznam/$', views.DnevnikListView.as_view(), name="dnevnik_list"),
    url(r'^skladisce-dnevnik/(?P<pk>\d+)/create/$', views.SkladisceDnevnikCreateFromDelovniNalogView.as_view(), name="skladisce_dnevnik_create_from_delovninalog"),
    url(r'^skladisce-dnevnik/(?P<pk>\d+)/update/$', views.SkladisceDnevnikUpdateView.as_view(), name="skladisce_dnevnik_update_from_delovninalog"),
]

# ARTIKEL
urlpatterns += [
    url(r'^artikel/create/$', views.DnevnikListView.as_view(), name="artikel_create"),
    url(r'^artikel/seznam/$', views.DnevnikListView.as_view(), name="artikel_list"),
]
