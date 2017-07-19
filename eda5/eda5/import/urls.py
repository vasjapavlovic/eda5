from django.conf.urls import url

from .views import import_deli_views, import_lokacija_views


urlpatterns = [

]


urlpatterns += [

    # DELI
    url(r'^deli-uvoz-podatkov/$', 
        import_deli_views.DeliUvozPodatkovView.as_view(), 
        name='import_deli_view'),

    # LOKACIJA
    url(r'^lokacija-uvoz-podatkov/$', 
        import_lokacija_views.LokacijaUvozPodatkovView.as_view(), 
        name='import_lokacija_view'),

]
