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
    url(r'^(?P<pk>\d+)/strosek/update/$', strosek_views.StrosekUpdateView.as_view(), name="strosek_update"),

    # filtriranje
    # filtriranje
    url(r'^reload_controls_vrsta_stroska_podkonto_view.html$', strosek_views.reload_controls_vrsta_stroska_podkonto_view, name='reload_controls_vrsta_stroska_podkonto_view'),
    url(r'^reload_controls_vrsta_stroska_skupinavrstestroska_view.html$', strosek_views.reload_controls_vrsta_stroska_skupinavrstestroska_view, name='reload_controls_vrsta_stroska_skupinavrstestroska_view'),
    url(r'^reload_controls_vrsta_stroska_view.html$', strosek_views.reload_controls_vrsta_stroska_view, name='reload_controls_vrsta_stroska_view'),
]
