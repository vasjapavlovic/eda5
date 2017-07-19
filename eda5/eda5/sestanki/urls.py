from django.conf.urls import url


from .views import sestanek_views


# HOME
urlpatterns = [
]


# Reklamacija
urlpatterns += [

    url(
        r'^sestanek/seznam/$', 
        sestanek_views.SestanekListView.as_view(), 
        name="sestanek_list"
    ),

    url(
        r'^(?P<pk>\d+)/detail/$', 
        sestanek_views.SestanekDetailView.as_view(), 
        name="sestanek_detail"
    ),

    url(
        r'^(?P<pk>\d+)/sestanek/create/$', 
        sestanek_views.SestanekCreateFromZahtevekView.as_view(), 
        name="sestanek_create_from_zahtevek"
    ),

    url(r'^(?P<pk>\d+)/sestanek/update/$', 
        sestanek_views.SestanekUpdateView.as_view(), 
        name="sestanek_update"
    ),

]