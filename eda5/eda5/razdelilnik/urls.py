from django.conf.urls import url, include

from .views import razdelilnik_views, racunrazdelilnik_views

urlpatterns = [
    # Razdelilnik
    url(r'^razdelilnik-seznam/$', razdelilnik_views.RazdelilnikListView.as_view(), name="razdelilnik_list"),
    url(r'^(?P<pk>\d+)/detail/$', razdelilnik_views.RazdelilnikDetailView.as_view(), name="razdelilnik_detail"),

    # RacunRazdelilnik
    url(r'^racunrazdelilnik-create/(?P<pk>\d+)$', racunrazdelilnik_views.RacunRazdelilnikCreateView.as_view(), name="racunrazdelilnik_create"),
    url(r'^racunrazdelilnik-update/(?P<pk>\d+)$', racunrazdelilnik_views.RacunRazdelilnikUpdateView.as_view(), name="racunrazdelilnik_update"),
]