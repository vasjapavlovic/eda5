from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.LastninaHomeView.as_view(), name="home"),
    url(r'^lastnistvo/$', views.LastninaListView.as_view(), name="list"),
    url(r'^lastnistvo/(?P<pk>\d+)/detail$', views.LastniskaEnotaInternaDetailView.as_view(), name="detail"),
]