from django.conf.urls import url

from . import views


# HOME
urlpatterns = [
]


urlpatterns += [



    #  Pregled Opravila
    url(
        r'^(?P<pk>\d+)/specifikacija/create$',
        views.KontrolniListSpecifikacijaCreateView.as_view(),
        name="kontrolni_list_specifikacija_create"
    ),


]
