from django.conf.urls import url, include

from . import views


urlpatterns = [
    url(r'^$', views.PorocanjePrejetiracuniHomeView.as_view(), name="home"),
]
