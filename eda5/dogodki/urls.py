from django.conf.urls import url

from .views import dogodek_views


urlpatterns = [
]


urlpatterns += [

    url(
        r'^dogodki/seznam/$',
        dogodek_views.DogodekListView.as_view(),
        name="dogodek_list"
    ),


    url(r'^(?P<pk>\d+)/dogodki/create/$',
        dogodek_views.DogodekCreateFromZahtevekView.as_view(),
        name="dogodek_create_from_zahtevek"
    ),


    url(r'^(?P<pk>\d+)/dogodki/update/$',
        dogodek_views.DogodekUpdateFromZahtevekView.as_view(),
        name="dogodek_update_from_zahtevek"
    ),


    url(
        r'^(?P<pk>\d+)/detail/$',
        dogodek_views.DogodekDetailView.as_view(),
        name="dogodek_detail"
    ),

]
