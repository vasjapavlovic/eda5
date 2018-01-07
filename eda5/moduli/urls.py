from django.conf.urls import include, url

from . import views

urlpatterns = [
    # registracija MODULOV (urlji)
    url(r'^arhiv/', include("eda5.arhiv.urls", namespace="arhiv")),
    url(r'^deli/', include("eda5.deli.urls", namespace="deli")),
    url(r'^delovninalogi/', include("eda5.delovninalogi.urls", namespace="delovninalogi")),
    url(r'^dogodki/', include("eda5.dogodki.urls", namespace="dogodki")),
    url(r'^etaznalastnina/', include("eda5.etaznalastnina.urls", namespace="etaznalastnina")),
    url(r'^uvoz/', include("eda5.import.urls", namespace="import")),
    url(r'^katalog/', include("eda5.katalog.urls", namespace="katalog")),
    url(r'^kl/', include("eda5.kontrolnilist.urls", namespace="kontrolni_list")),
    url(r'^kljuci/', include("eda5.kljuci.urls", namespace="kljuci")),
    url(r'^lastnistvo/', include("eda5.lastnistvo.urls", namespace="lastnistvo")),
    url(r'^lokacija/', include("eda5.lokacija.urls", namespace="lokacija")),
    url(r'^nadzorna-plosca/', include("eda5.nadzornaplosca.urls", namespace="nadzornaplosca")),
    url(r'^naloge/', include("eda5.naloge.urls", namespace="naloge")),
    url(r'^narocila/', include("eda5.narocila.urls", namespace="narocila")),
    url(r'^obvestila/', include("eda5.obvestila.urls", namespace="obvestila")),
    url(r'^obrazci/', include("eda5.obrazci.urls", namespace="obrazci")),
    url(r'^partnerji/', include("eda5.partnerji.urls", namespace="partnerji")),
    url(r'^planiranje/', include("eda5.planiranje.urls", namespace="planiranje")),
    url(r'^posta/', include("eda5.posta.urls", namespace="posta")),
    url(r'^pomanjkljivosti/', include("eda5.pomanjkljivosti.urls", namespace="pomanjkljivosti")),
    url(r'^porocanje-upravnika/', include("eda5.porocanjeupravnika.urls", namespace="porocanjeupravnika")),
    url(r'^povprasevanje/', include("eda5.povprasevanje.urls", namespace="povprasevanje")),
    url(r'^racunovodstvo/', include("eda5.racunovodstvo.urls", namespace="racunovodstvo")),
    url(r'^razdelilnik/', include("eda5.razdelilnik.urls", namespace="razdelilnik")),
    url(r'^reklamacije/', include("eda5.reklamacije.urls", namespace="reklamacije")),
    url(r'^reports/', include("eda5.reports.urls", namespace="reports")),
    url(r'^sestanki/', include("eda5.sestanki.urls", namespace="sestanki")),
    url(r'^skladisce/', include("eda5.skladisce.urls", namespace="skladisce")),
    url(r'^stevcno-stanje/', include("eda5.stevcnostanje.urls", namespace="stevcnostanje")),
    url(r'^veljavnost-dokumentov/', include("eda5.veljavnostdokumentov.urls", namespace="veljavnostdokumentov")),
    url(r'^zahtevki/', include("eda5.zahtevki.urls", namespace="zahtevki")),
    url(r'^zaznamki/', include("eda5.zaznamki.urls", namespace="zaznamki")),
]

# Glavni URL za modul
urlpatterns += [
    url(r'^$', views.ModulHomeView.as_view(), name="home"),
    url(r'^(?P<pk>\d+)/detail$', views.ModulDetailView.as_view(), name="detail"),
]
