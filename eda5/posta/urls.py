from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.PostaHomeView.as_view(), name="home"),
]

# DOKUMENT
urlpatterns += [
    url(r'^za-arhiviranje/$', views.PostaArhiviranjeListView.as_view(), name="dokument_arhiviranje_list"),
    url(r'^create/$', views.DokumentCreateView.as_view(), name="dokument_create"),
    url(r'^(?P<pk>\d+)/detail/$', views.PostaDokumentDetailView.as_view(), name="dokument_detail"),
]
