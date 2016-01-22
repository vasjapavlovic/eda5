from django.conf.urls import include, url

from . import views

urlpatterns = [
    # registracija MODULOV (urlji)
    url(r'^deli/', include("eda5.deli.urls", namespace="deli")),
    url(r'^delovninalogi/', include("eda5.delovninalogi.urls", namespace="delovninalogi")),
    url(r'^etaznalastnina/', include("eda5.etaznalastnina.urls", namespace="etaznalastnina")),
    url(r'^uvoz/', include("eda5.import.urls", namespace="import")),
    url(r'^katalog/', include("eda5.katalog.urls", namespace="katalog")),
    url(r'^kljuci/', include("eda5.kljuci.urls", namespace="kljuci")),
    url(r'^narocila/', include("eda5.narocila.urls", namespace="narocila")),
    url(r'^partnerji/', include("eda5.partnerji.urls", namespace="partnerji")),
    url(r'^planiranje/', include("eda5.planiranje.urls", namespace="planiranje")),
    url(r'^posta/', include("eda5.posta.urls", namespace="posta")),
    url(r'^pomanjkljivosti/', include("eda5.pomanjkljivosti.urls", namespace="pomanjkljivosti")),
    url(r'^porocanje-upravnika/', include("eda5.porocanjeupravnika.urls", namespace="porocanjeupravnika")),
    url(r'^racunovodstvo/', include("eda5.racunovodstvo.urls", namespace="racunovodstvo")),
    url(r'^razdelilnik/', include("eda5.razdelilnik.urls", namespace="razdelilnik")),
    url(r'^reports/', include("eda5.reports.urls", namespace="reports")),
    url(r'^skladisce/', include("eda5.skladisce.urls", namespace="skladisce")),
    url(r'^stevcno-stanje/', include("eda5.stevcnostanje.urls", namespace="stevcnostanje")),
    url(r'^zahtevki/', include("eda5.zahtevki.urls", namespace="zahtevki")),
]

# Glavni URL za modul
urlpatterns += [
    url(r'^$', views.ModulHomeView.as_view(), name="home"),
    url(r'^(?P<pk>\d+)/detail$', views.ModulDetailView.as_view(), name="detail"),
]
