from django.conf.urls import url

from .views import racun_views, strosek_views


# Racun
urlpatterns = [
    url(r'^racun-create/$', racun_views.RacunCreateView.as_view(), name="racun_create"),
    url(r'^racun-seznam/$', racun_views.RacunListView.as_view(), name="racun_list"),
    url(r'^racun/(?P<pk>\d+)/detail/$', racun_views.RacunDetailView.as_view(), name="racun_detail"),
]

# Strosek
urlpatterns += [
    url(r'^(?P<pk>\d+)/strosek-from-racun-create/$', strosek_views.StrosekCreateView.as_view(), name="strosek_from_racun_create"),
]
