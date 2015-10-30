from django.conf.urls import url, include

from . import views


urlpatterns = [
    url(r'^$', views.PorocanjeHomeView.as_view(), name="home"),
    url(r'^prejeti-racuni/', include("eda5.porocanjeupravnika.urls_prejetiracuni", namespace="prejetiracuni")),
    url(r'^lastnina/', include("eda5.porocanjeupravnika.urls_lastnina", namespace="lastnina")),
]
