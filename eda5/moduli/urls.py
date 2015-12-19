from django.conf.urls import include, url

from . import views

urlpatterns = [
    # registracija MODULOV (urlji)
    url(r'^deli/', include("eda5.deli.urls", namespace="deli")),
    url(r'^delovninalogi/', include("eda5.delovninalogi.urls", namespace="delovninalogi")),
    url(r'^etaznalastnina/', include("eda5.etaznalastnina.urls", namespace="etaznalastnina")),
    url(r'^uvoz/', include("eda5.import.urls", namespace="import")),
    url(r'^katalog/', include("eda5.katalog.urls", namespace="katalog")),
    url(r'^narocila/', include("eda5.narocila.urls", namespace="narocila")),
    url(r'^partnerji/', include("eda5.partnerji.urls", namespace="partnerji")),
    url(r'^posta/', include("eda5.posta.urls", namespace="posta")),
    url(r'^pomanjkljivosti/', include("eda5.pomanjkljivosti.urls", namespace="pomanjkljivosti")),
    url(r'^predaja-lastnine/', include("eda5.predaja_lastnine.urls", namespace="predaja_lastnine")),
    url(r'^racunovodstvo/', include("eda5.racunovodstvo.urls", namespace="racunovodstvo")),
    url(r'^razdelilnik/', include("eda5.razdelilnik.urls", namespace="razdelilnik")),
    url(r'^skladisce/', include("eda5.skladisce.urls", namespace="skladisce")),
    url(r'^stevci/', include("eda5.stevci.urls", namespace="stevci")),
    url(r'^zahtevki/', include("eda5.zahtevki.urls", namespace="zahtevki")),
]

# Glavni URL za modul
urlpatterns += [
    url(r'^$', views.ModulHomeView.as_view(), name="home"),
    url(r'^(?P<pk>\d+)/detail$', views.ModulDetailView.as_view(), name="detail"),
]
