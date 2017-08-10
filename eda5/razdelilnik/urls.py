from django.conf.urls import url, include

from .views import razdelilnik_views, strosekrazdelilnik_views

urlpatterns = [
    # Razdelilnik
    url(r'^razdelilnik-create/(?P<pk>\d+)$', razdelilnik_views.RazdelilnikCreateFromZahtevekView.as_view(), name="razdelilnik_create_from_zahtevek"),
    url(r'^razdelilnik-seznam/$', razdelilnik_views.RazdelilnikListView.as_view(), name="razdelilnik_list"),
    url(r'^(?P<pk>\d+)/detail/$', razdelilnik_views.RazdelilnikDetailView.as_view(), name="razdelilnik_detail"),

    # RacunRazdelilnik
    #url(r'^racunrazdelilnik-create/(?P<pk>\d+)$', racunrazdelilnik_views.RacunRazdelilnikCreateView.as_view(), name="racunrazdelilnik_create"),
    #url(r'^racunrazdelilnik-update/(?P<pk>\d+)$', racunrazdelilnik_views.RacunRazdelilnikUpdateView.as_view(), name="racunrazdelilnik_update"),

    # RacunRazdelilnik
    url(r'^strosekrazdelilnik-create/(?P<pk>\d+)$', strosekrazdelilnik_views.StrosekRazdelilnikCreateView.as_view(), name="strosekrazdelilnik_create"),
    url(r'^strosekrazdelilnik-razdeli/(?P<pk>\d+)$', strosekrazdelilnik_views.StrosekRazdelilnikUpdateRazdeliView.as_view(), name="strosekrazdelilnik_update_razdeli"),
]