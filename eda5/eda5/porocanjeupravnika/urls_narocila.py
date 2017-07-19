from django.conf.urls import url, include

from . import views


urlpatterns = [
    url(r'^$', views.NarociloHomeView.as_view(), name="home"),
    url(r'^seznam/$', views.NarociloListView.as_view(), name="list"),
]
