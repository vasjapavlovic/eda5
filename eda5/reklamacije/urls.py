from django.conf.urls import url


from .views import reklamacija_views


# HOME
urlpatterns = [
]


# Reklamacija
urlpatterns += [

    url(
    	r'^reklamacija/seznam/$',
    	reklamacija_views.ReklamacijaListView.as_view(),
    	name="reklamacija_list"
    ),

    url(
    	r'^(?P<pk>\d+)/detail/$',
    	reklamacija_views.ReklamacijaDetailView.as_view(),
    	name="reklamacija_detail"
    ),

    url(
    	r'^(?P<pk>\d+)/reklamacija/create/$',
        reklamacija_views.ReklamacijaCreateFromZahtevekView.as_view(),
        name="reklamacija_create_from_zahtevek"
    ),

    url(r'^(?P<pk>\d+)/reklamacija/update/$',
        reklamacija_views.ReklamacijaUpdateView.as_view(),
        name="reklamacija_update"
    ),

]
