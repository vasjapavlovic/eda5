from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.DelHomeView.as_view(), name="home"),
    url(r'^seznam/$', views.DelListView.as_view(), name="list"),
    url(r'^(?P<pk>\d+)/detail/$', views.DelDetailView.as_view(), name="detail"),
]