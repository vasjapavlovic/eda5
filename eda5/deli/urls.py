from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.DelHomeView.as_view(), name="home"),
    url(r'^create/$', views.DelCreateView.as_view(), name="del_create"),
    url(r'^reload_controls.html$', views.reload_controls_view, name='reload_controls'),
    url(r'^seznam/$', views.DelListView.as_view(), name="del_list"),
    url(r'^del/(?P<pk>\d+)/detail/$', views.DelDetailView.as_view(), name="del_detail"),
    url(r'^del/(?P<pk>\d+)/update/$', views.DelUpdateView.as_view(), name="del_update"),
    url(r'^element/(?P<pk>\d+)/detail/$', views.ElementDetailView.as_view(), name="element_detail"),
]

# Projektno Mesto
urlpatterns += [
    url(r'^projektno-mesto-create/$', views.ProjektnoMestoCreateView.as_view(), name="projektno_mesto_create"),
]
