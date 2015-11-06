from django.conf.urls import include, url

from . import views

urlpatterns = [
    # registracija MODULOV (urlji)
    url(r'^deli/', include("eda5.deli.urls", namespace="deli")),
    url(r'^delovninalogi/', include("eda5.delovninalogi.urls", namespace="delovninalogi")),
    url(r'^lastnina/', include("eda5.etaznalastnina.urls", namespace="lastnina")),
    url(r'^katalog/', include("eda5.katalog.urls", namespace="katalog")),
    url(r'^partnerji/', include("eda5.partnerji.urls", namespace="partnerji")),
    url(r'^posta/', include("eda5.posta.urls", namespace="posta")),
    url(r'^racunovodstvo/', include("eda5.racunovodstvo.urls", namespace="racunovodstvo")),
    url(r'^razdelilnik/', include("eda5.razdelilnik.urls", namespace="razdelilnik")),
    url(r'^stevci/', include("eda5.stevci.urls", namespace="stevci")),
    # url(r'^stores/', include("eda5.stores.urls", namespace="stores")),
    url(r'^zahtevki/', include("eda5.zahtevki.urls", namespace="zahtevki")),
]

# Glavni URL za modul
urlpatterns += [
    url(r'^$', views.ModulHomeView.as_view(), name="home"),
]
