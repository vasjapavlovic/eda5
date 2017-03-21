from django.conf.urls import url


from .views import reklamacija_views


# HOME
urlpatterns = [
]


# DELOVNI NALOG
urlpatterns += [

    url(r'^(?P<pk>\d+)/reklamacija/create/$', 
        reklamacija_views.ReklamacijaCreateFromZahtevekView.as_view(), 
        name="reklamacija_create_from_zahtevek"
    ),

]