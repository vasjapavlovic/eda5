from django.conf.urls import url

# importamo komplet views
from .views import filtriranje, skupina, podskupina, delstavbe, projektnomesto, element, deli_uvozpodatkov_views



urlpatterns = [
]

urlpatterns += [

    url(r'^create/$', 
        delstavbe.DelCreateView.as_view(), 
        name="del_create"),

    url(r'^seznam/$', 
        delstavbe.DelListView.as_view(), 
        name="del_list"),

    url(r'^del/(?P<pk>\d+)/detail/$', 
        delstavbe.DelDetailView.as_view(), 
        name="del_detail"),

    url(r'^del/(?P<pk>\d+)/update/$', 
        delstavbe.DelUpdateView.as_view(), 
        name="del_update"),
    
]

# Projektno Mesto
urlpatterns += [

    url(r'^projektno-mesto-create/$', 
        projektnomesto.ProjektnoMestoCreateView.as_view(), 
        name="projektno_mesto_create"),

    url(r'^projektno-mesto/(?P<pk>\d+)/detail/$', 
        projektnomesto.ProjektnoMestoDetailView.as_view(), 
        name="projektnomesto_detail"),

]


# Filtriranje
urlpatterns += [

    # filter seznam podskupin glede na izbrano skupino
    url(r'^filter_skupina_podskupina.html$', 
        filtriranje.filter_skupina_podskupina, 
        name='filter_skupina_podskupina'),

    # filter seznam delov stavbe glede na izbrano podskupino
    url(r'^filter_podskupina_delstavbe.html$', 
        filtriranje.filter_podskupina_delstavbe, 
        name='filter_podskupina_delstavbe'),

    # filter seznam projektnih mest glede na izbran del stavbe
    url(r'^filter_delstavbe_projektnomesto.html$', 
        filtriranje.filter_delstavbe_projektnomesto, 
        name='filter_delstavbe_projektnomesto'),

]

