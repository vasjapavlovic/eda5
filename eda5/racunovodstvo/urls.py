from django.conf.urls import url

from . import views


# Racun
urlpatterns = [
    url(r'^racun-create/$', views.RacunCreateView.as_view(), name="racun_create"),
    url(r'^racun-seznam/$', views.RacunListView.as_view(), name="racun_list"),
    url(r'^racun/(?P<pk>\d+)/detail/$', views.RacunDetailView.as_view(), name="racun_detail"),
]
