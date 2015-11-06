from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.DelHomeView.as_view(), name="home"),
    url(r'^seznam/$', views.DelListView.as_view(), name="list"),
    url(r'^del/(?P<pk>\d+)/detail/$', views.DelDetailView.as_view(), name="del_detail"),
    url(r'^element/(?P<pk>\d+)/detail/$', views.ElementDetailView.as_view(), name="element_detail"),
]