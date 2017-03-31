from django.conf.urls import url

from .views import ArhiviranjePopUpListView, ArhiviranjeCreateFromReklamacija, ArhiviranjeCreateFromZahtevek
from .views import ArhiviranjeCreateFromDelovniNalog, ArhiviranjeCreateFromDobava

# HOME
urlpatterns = [
]

# Arhiviranje
urlpatterns += [
    url(r'^arhiviranje/popup-list/?$', ArhiviranjePopUpListView.as_view(), name='arhiviranje_popup_list'),    


    url(
        r'^/zahtevek/(?P<pk>\d+)/arhiviranje-create/$', 
        ArhiviranjeCreateFromZahtevek.as_view(), 
        name="arhiviranje_create_from_zahtevek"
    ),

    url(
        r'^/reklamacija/(?P<pk>\d+)/arhiviranje-create/$', 
        ArhiviranjeCreateFromReklamacija.as_view(), 
        name="arhiviranje_create_from_reklamacija"
    ),

    url(
        r'^/delovninalog/(?P<pk>\d+)/arhiviranje-create/$', 
        ArhiviranjeCreateFromDelovniNalog.as_view(), 
        name="arhiviranje_create_from_delovninalog"
    ),

    url(
        r'^/dobava/(?P<pk>\d+)/arhiviranje-create/$', 
        ArhiviranjeCreateFromDobava.as_view(), 
        name="arhiviranje_create_from_dobava"
    ),


]




