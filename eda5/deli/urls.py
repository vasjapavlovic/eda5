from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.DelHomeView.as_view(), name="home"),
    url(r'^create/$', views.DelCreateView.as_view(), name="del_create"),
    url(r'^reload_controls.html$', views.reload_controls_view, name='reload_controls'),
    url(r'^seznam/$', views.DelListView.as_view(), name="del_list"),
    url(r'^del/(?P<pk>\d+)/detail/$', views.DelDetailView.as_view(), name="del_detail"),
    url(r'^del/(?P<pk>\d+)/update/$', views.DelUpdateView.as_view(), name="del_update"),
    
]

# Projektno Mesto
urlpatterns += [
    url(r'^projektno-mesto-create/$', views.ProjektnoMestoCreateView.as_view(), name="projektno_mesto_create"),
    url(r'^projektno-mesto/(?P<pk>\d+)/detail/$', views.ProjektnoMestoDetailView.as_view(), name="projektnomesto_detail"),

        # IZBIRA PROJEKTNEGA MESTA (ELEMENTA)
    # Filtriranje glede na izbrano skupino delov stavbe
    url(r'^reload_controls_element_podskupina.html$', 
        views.reload_controls_element_podskupina_view, 
        name='reload_controls_element_podskupina'),

    # Filtriranje glede na izbrano podskupino delov stavbe
    url(r'^reload_controls_element_del_stavbe.html$', 
        views.reload_controls_element_del_stavbe_view, 
        name='reload_controls_element_del_stavbe'),

    # Filtriranje glede na izbran del stavbe
    url(r'^reload_controls_element_element.html$', 
        views.reload_controls_element_element_view, 
        name='reload_controls_element_element'),


    
]
