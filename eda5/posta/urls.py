from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.PostaHomeView.as_view(), name="home"),
]

# POSTA
urlpatterns += [
    url(r'^za-arhiviranje/$', views.PostaArhiviranjeListView.as_view(), name="posta_arhiviranje_list"),
]

# AKTIVNOST
urlpatterns += [
    url(r'^create/$', views.AktivnostCreateView.as_view(), name="aktivnost_create"),
]